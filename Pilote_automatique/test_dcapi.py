import dcapi
import time

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
