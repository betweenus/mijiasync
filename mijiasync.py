from bluepy.btle import Peripheral
import time
import struct

devices = [  # list of clock devices (mac addresses)
    'e7:2e:00:00:00:00',    # LYWSD02
    'e7:50:59:00:00:00'     # MHO-C303
]

def rawtime():
    gmtoff = time.localtime().tm_gmtoff
    
    gmtoffh = gmtoff // 3600
    gmtoffs = gmtoff % 3600
    
    ctime = round(time.time()) + gmtoffs
    
    return struct.pack('<Ib', ctime, gmtoffh)

for device in devices:
    ch = []
    
    for i in range(10):
        try:
            per = Peripheral(device)
            ch = per.getCharacteristics(uuid = 'ebe0ccb7-7a0a-4b0c-8a1a-6ff2997da3a6')
            break
        except BTLEDisconnectError:
            time.sleep(5)
            continue
    
    if len(ch) != 1:
        continue
    
    if ch[0].read() != rawtime():
        print(device, 'Syncing...')
        ch[0].write(rawtime())
    else:
        print(device, 'No need to sync.')
