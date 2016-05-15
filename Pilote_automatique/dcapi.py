import pigpio
import time


    # definition des pins I/O
P1 = 17 # ppm signal low polarity, i.e idle level is high
P2 = 22 # ppm signal high polarity, i.e idle level is low
ENABLE_PIN = 9 # permet d'accepter ou de rendre le controle par le Raspberry
BUTTON_PIN = 23 # boutton poussoir de la carte, idle low
RADIO_1 = 5 # signal logique, commande le mux ** bug
RADIO_2 = 6 # signal logique  ** bug
LED_PIN = 4 # led user de la carte  



    # Code d'erreur
OK = 0
CH1_FALLING = -1 
CHANNEL_ERROR = -2 # numero de channel en dehors de 1-12
CONTROL_ERROR = -3 # tentative d'envoyer des ordres au drone sans avoir le controle
WAVE_ERROR = -4  #erreur lors de la generation du signal PPM

    
UPDATE_NOW = 1
UPDATE_LATER = 0


    # longueurs des pulse    
MAX_LENGHT = 1500
MIN_LENGHT = 500
TOTAL_LENGHT = 30000

    #Valeur max et min
MAX_IN = 260
MIN_IN = 0
AVR_IN = 131
OFFSET = 39


    #Channel assignment
ROLL = 2
NICK = 1
THROTTLE = 3
YAW = 4
ALTI = 5
GPS = 6

    # mode GPS
GPS_OFF = MIN_IN
GPS_HOLD = AVR_IN
GPS_RETURN_HOME = MAX_IN

    # mode altitude
ALTI_OFF = MIN_IN
ALTI_HOLD = MAX_IN

NBR_CHANNEL = 12



A = (MAX_LENGHT-MIN_LENGHT)/MAX_IN
B = MIN_LENGHT

DEFAULT_DATA = [AVR_IN, AVR_IN, AVR_IN, AVR_IN, ALTI_HOLD, GPS_HOLD, AVR_IN, AVR_IN, AVR_IN, AVR_IN, AVR_IN, AVR_IN]
CURRENT_DATA = DEFAULT_DATA

FLAG = 0  # variable de com avec une ISR
ENABLE_STATE = 0 # valeur de ENABLE_PIN

pi = pigpio.pi() #init lib pigpio

def init():
    print 'initialisation ..'
    FLAG = OK
    pi.callback(RADIO_1, pigpio.FALLING_EDGE, flag_isr)
    
    pi.set_mode(P1, pigpio.OUTPUT)
    pi.set_mode(P2, pigpio.OUTPUT)
    pi.set_mode(ENABLE_PIN, pigpio.OUTPUT)
    pi.set_mode(LED_PIN, pigpio.OUTPUT)
    #pi.set_mode(RADIO_1, pigpio.INPUT)
    #pi.set_mode(RADIO_2, pigpio.INPUT)
    pi.set_mode(BUTTON_PIN, pigpio.INPUT)

    pi.set_PWM_frequency(LED_PIN, 1)
    pi.set_PWM_dutycycle(LED_PIN, 128)
    time.sleep(2)    #fait clignoter la led user pendant 2s
    r = ppm_update(DEFAULT_DATA)
    if(r != OK):
        pi.set_PWM_dutycycle(LED_PIN,0)
        print ('Erreur ppm_update() : ' + str(r))
    else:
      pi.set_PWM_dutycycle(LED_PIN,255)    # on allume la LED si le signal ppm est ok
    



#genere le signal PPM. Le signal est emis indefiniment. Renvoie un code d'erreur
def ppm_update(data):

    trame = []
    transit =0;
    result = OK
    
#                              ON     OFF  DELAY   
    trame.append(pigpio.pulse(1<<P2,1<<P1,500)) # niveau bas de start
    current_lenght = 500;            
    
    for i in range(NBR_CHANNEL):
        if data[i] <= MAX_IN and data[i] >= MIN_IN:
            transit=(A*(data[i]+OFFSET)+B)
            trame.append(pigpio.pulse(1<<P1,1<<P2,transit))
            current_lenght+=transit
        else:
            transit=(A*(DEFAULT_DATA[i]+OFFSET)+B)
            trame.append(pigpio.pulse(1<<P1,1<<P2,transit))
            current_lenght+=transit
            result = i # memorise quelle channel a leve l'erreur 
                
        trame.append(pigpio.pulse(1<<P2,1<<P1,500))# niveau bas entre 2 channel
        current_lenght+=500;

    # fin boucle 
    trame.append(pigpio.pulse(1<<P1,1<<P2,(TOTAL_LENGHT-current_lenght))) # delai final
    #print TOTAL_LENGHT-current_lenght
    # trame terminee
    
        
    pi.wave_clear() # on lance le nouveau signal PPM en etant sur de pas avoir coupe le precedent
    pi.wave_add_generic(trame)
    id_trame=pi.wave_create()
    if(id_trame >= 0):
        pi.wave_send_using_mode(id_trame, pigpio.WAVE_MODE_REPEAT_SYNC)
        print "PPM signal updated"
    else:
        result = WAVE_ERROR
    return result


def stop_ppm():
    pi.wave_tx_stop()
    pi.set_PWM_dutycycle(LED_PIN, 128)

def free_pi():
    stop_ppm()
    pi.set_PWM_dutycycle(LED_PIN, 0)
    pi.stop()


def write_channel(ch, value, update=0):
    result = OK
    if ch < NBR_CHANNEL and ch >= 0:
        CURRENT_DATA[ch] = value
        if(update == 1):
            result = ppm_update(CURRENT_DATA)
    else:
        result = CHANNEL_ERROR
    return result


    # value = 0 - 255
def yaw(value):
    return write_channel(YAW, value)

def throttle(value):
    return write_channel(THROTTLE, value)
    
def nick(value):
    return write_channel(NICK, value)

def roll(value):
    return write_channel(ROLL, value)

    # mode: voir variable plus haut
def gps(mode):
    return write_channel(GPS, mode)

def alti(mode):
    return write_channel(ALTI, mode)

def read_ch1():
    return pi.read(RADIO_1)

def read_ch2():
    return pi.read(RADIO_2)

def read_button():
    return pi.read(BUTTON_PIN)

def led_blink():
    pi.set_PWM_dutycycle(LED_PIN, 128)
    
def led_on():
    pi.set_PWM_dutycycle(LED_PIN, 255)
    
def led_off():
    pi.set_PWM_dutycycle(LED_PIN, 0)

def enable_control(mode):
    global ENABLE_STATE
    pi.write(ENABLE_PIN, mode)
    ENABLE_STATE = mode


    #calibre l'accelerometre du drone
def calibration_acc():

    global FLAG
    if check_control() == 0:
        print 'Unauthorized control. Calibration cancelled'
        return CONTROL_ERROR
    
    print 'calibration..'
    err = throttle(MAX_IN)
    err = yaw(MAX_IN)
    if err == OK:
        err = ppm_update(CURRENT_DATA)
    else:
        print 'Calibration avorted. error code:'+str(err)
        return err
    
    time.sleep(2)
    
    err = throttle(AVR_IN)
    err = yaw(AVR_IN)
    if err == OK:
        err = ppm_update(CURRENT_DATA)
    else:
        ppm_update(DEFAULT_DATA)
        print 'Calibration stopped. error code:'+str(err)
        return err

    time.sleep(2)
    
    if FLAG == OK: #verifie que le raspberry pi a toujours eu la main pendant la manip
        print 'Calibration done'
        return err
    else:
        print 'Calibration may have been interrupted'
        err = FLAG
        FLAG = OK
        return err

    # demarrage du drone
def arm():

    global FLAG
    
    if check_control() == 0:
        print 'Unauthorized control. Arming cancelled'
        return CONTROL_ERROR
    
    print 'arming..'
    err = throttle(MIN_IN)
    err = yaw(MIN_IN)
    err = nick(MIN_IN)
    err = roll(MIN_IN)

    if err == OK:
        err = ppm_update(CURRENT_DATA)
    else:
        print 'arming avorted. error code:'+str(err)
        return err

    time.sleep(3)
    err = ppm_update(DEFAULT_DATA)

    if FLAG == OK:
        print 'drone armed'
        return err
    else:
        print 'arming may have been interrupted'
        err = FLAG
        FLAG = OK
        return err

    # arret du drone 
def disarm():

    global FLAG
    if check_control() == 0:
        print 'Unauthorized control. Disarming canceled'
        return CONTROL_ERROR
    
    print 'disarming..'
    err = throttle(MIN_IN)
    err = yaw(MAX_IN)
    err = nick(MIN_IN)
    err = roll(MAX_IN)

    if err == OK:
        err = ppm_update(CURRENT_DATA)
    else:
        print 'disarming avorted. error code:'+str(err)
        return err

    time.sleep(3)
    err = ppm_update(DEFAULT_DATA)

    if FLAG == OK:
        print 'drone disarmed'
        return err
    else:
        print 'disarming may have been interrupted'
        err = FLAG
        FLAG = OK
        return err
    
def flag_isr(gpio, level, tick):
    global FLAG
    FLAG = CH1_FALLING

def check_control():
    if ENABLE_STATE == 1 and read_ch1() == 1:
        return 1
    else:
        return 0
