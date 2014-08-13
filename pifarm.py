from datetime import datetime

def pinaple(id):
  return Pinaple(id)

class Pinaple:
  """docstring for Pinaple"""
  def __init__(self, id):
    self.id = id
    self.devices = DevicesRepository(id)

class DevicesRepository:
  """docstring for DevicesRepository"""
  def __init__(self, pinaple_id):
    self.pinaple_id = pinaple_id

  def get(self, name):
    return Device(name)
    
class Device:
  """docstring for Device"""
  def __init__(self, name):
    self.name = name
    self.readings = ReadingsRepository()

  def upload(self):
    print('starting uploading to api')
    for reading in self.readings.all():
      print("uploading reading for {0} with value {1} at {2}".format(reading.name, reading.value, reading.at))
    print('finished uploading {} reading to api'.format(self.readings.count()))

    self.readings = []  

class ReadingsRepository:
  """docstring for ReadingsRepository"""
  def __init__(self):
    self.readings = []

  def add(self, name, value, at=None):
    reading = Reading(name, value, at)
    self.readings.append(reading)

  def all(self):
    return self.readings

  def count(self):
    return len(self.readings)

class Reading:
  """docstring for Reading"""
  def __init__(self, name, value, at=None):
    if at is None:
      at = datetime.utcnow()
      
    self.name = name
    self.value = value
    self.at = at
    
    