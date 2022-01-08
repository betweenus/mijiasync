from bluepy.btle import Peripheral
import time
import struct
import syslog

devices = [  # list of clock devices (mac addresses)
    'e7:2e:00:00:00:00',    # LYWSD02
    'e7:50:59:00:00:00'     # MHO-C303
]

log2syslog = True

def tolog(device, msg):
    print(device, msg)
    if log2syslog:
        syslog.syslog(device + ': ' + msg)

def rawtime():
    gmtoff = time.localtime().tm_gmtoff
    
    gmtoffh = gmtoff // 3600
    gmtoffs = gmtoff % 3600
    
    ctime = round(time.time()) + gmtoffs
    
    return struct.pack('<Ib', ctime, gmtoffh)

for device in devices:
    try:
        per = Peripheral(device)
    except Exception as e:
        tolog(device, 'Error when connect to clock!')
        continue
    
    ch = []
    
    try:
        ch = per.getCharacteristics(uuid = 'ebe0ccb7-7a0a-4b0c-8a1a-6ff2997da3a6')
    except Exception as e:
        pass
    
    if len(ch) != 1:
        tolog(device, 'Error when get characteristics!')
        per.disconnect()
        continue
    
    if ch[0].read() != rawtime():
        tolog(device, 'Synchronizing...')
        ch[0].write(rawtime())
    else:
        tolog(device, 'No need to sync')
        
    per.disconnect()
