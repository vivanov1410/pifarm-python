import pifarm

api = pifarm.connect('slava@gmail.com', 'testishe')
pinaple = api.pinaples.get('53f5315ac948e35ad488434c')
temperature = pinaple.streams.get('53f53193c948e35ad488434e')
temperature.readings.add(value=1)
temperature.readings.add(value=2)
temperature.readings.add(value=3)