import time

import dcapi

dcapi.init()
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
