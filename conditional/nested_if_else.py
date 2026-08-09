device_status = "inactive"
temperature = 3.6
if device_status == "active":
    if temperature > 35:
        print(f"Warn : high temperature detected : {temperature}°C")
    else:
        print(f"temperature is normal : {temperature}°C")
else:
    print(f"device is offline, please check the device status : {device_status}")  

