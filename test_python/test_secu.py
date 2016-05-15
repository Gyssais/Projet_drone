import dcapi
import time

dcapi.init()

try:
    dcapi.enable_control(1)
    print 'ch1:' + str(dcapi.read_ch1())
    print 'enable:' + str(dcapi.ENABLE_STATE)
    
    print str(dcapi.calibration_acc())
    time.sleep(3)
    print str(dcapi.arm())
    time.sleep(3)
    print str(dcapi.disarm())
    time.sleep(3)
    
    while dcapi.read_button() == 0:
        time.sleep(1)
        print str(dcapi.write_channel(11,200,1))


finally:                      # quand on quitte, normalement ou pas
    dcapi.enable_control(0)
    print "script termine, controle rendu"
    dcapi.free_pi()
