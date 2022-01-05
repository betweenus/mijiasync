# mijiasync.py

Simple Python 3 script for syncing Xiaomi smart bluetooth clocks, such as Xiaomi Mijia (LYWSD02) or MiaoMiaoCe (MHO-C303).

## Using

Update device list in script with mac-addresses of your devices and put "python /path/to/mijiasync.py" to crontab (everyday or everyweek).
```
devices = [  # list of clock devices (mac addresses)
    'e7:2e:00:00:00:00',    # LYWSD02
    'e7:50:59:00:00:00'     # MHO-C303
]
```
