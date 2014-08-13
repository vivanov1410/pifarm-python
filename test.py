import pifarm
from datetime import datetime

pinaple = pifarm.pinaple('key')
print(pinaple.id)

device = pinaple.devices.get('device1');
print(device.name)

now = datetime.utcnow()
device.readings.add(name='temperature', value=10)
device.readings.add(name='humidity', value=15)
device.upload()