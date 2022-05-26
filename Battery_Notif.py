import psutil
from plyer import notification
import time

battery = psutil.sensors_battery()
percent = battery.percent
while(percent!=83):
    battery = psutil.sensors_battery()
    percent = battery.percent

battery = psutil.sensors_battery()
percent = battery.percent
	
notification.notify(
	title="Battery Percentage",
    message=str(percent)+"% Battery remaining",
	timeout=10
)
	
# after every 60 mins it will show the
# battery percentage
# time.sleep(60*60)
