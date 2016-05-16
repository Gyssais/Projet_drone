import dcapi
import time


def demo_start_stop():
    button = 0
    try:
    dcapi.enable_control(1)

    print 'attente controle'
    while dcapi.read_ch1() == 0: # attente controle
        if dcapi.read_button() == 1:
            button = 1 
            break
        time.sleep(0.1)
        
    dcapi.led_blink()
    print str(dcapi.calibration_acc())
    dcapi.led_on()

    while button == 0:

        print 'attente arming'
        while dcapi.read_ch2() == 0: # attente ordre arming
            if dcapi.read_button() == 1:
                button = 1
                break
            time.sleep(0.1)

        if button == 0:
            dcapi.led_blink()
            print str(dcapi.arm())
            dcapi.led_on()

        print 'attente disarming'
        while dcapi.read_ch2() == 1: # attente ordre disarming
            if dcapi.read_button() == 1:
                button = 1
                break
            time.sleep(0.1)

        if button == 0:
            dcapi.led_blink()
            print str(dcapi.disarm())
            dcapi.led_on()


    finally:                      # quand on quitte, normalement ou pas
        dcapi.enable_control(0)
        print "script termine, controle rendu"
        dcapi.free_pi()


def test_switch():
    data_test = [120,120,120,120, 120,120,120,120,0,0,131,260]

    dcapi.init()
    dcapi.ppm_update(data_test)
    dcapi.enable_control(1)

    try:

        while dcapi.read_button() == 0:
            time.sleep(1)
            if dcapi.read_ch1() == 1 :
                print 'CH1 on'
            else:
                print 'CH1 off'

            if dcapi.read_ch2() == 1:
                 print 'CH2 on'
            else:
                print 'CH2 off'

        print "exiting.."

    finally:                      # quand on quitte, normalement ou pas
        dcapi.enable_control(0)
        print "script termine, controle rendu"
        dcapi.free_pi()
    


def test_ch():
    data_test = [127,127,127,127,127,127,127,127,127,127,127,127]
    channel=0
    try:
        dcapi.enable_control(1)
        while dcapi.read_button() == 0:
            channel = input ('Channel:')
            data_test [channel-1] = input ('Valeur:')
            ppm_update(data_test)
     finally:                      # quand on quitte, normalement ou pas
        dcapi.enable_control(0)
        print "script termine, controle rendu"
        dcapi.free_pi()
             





    
    
