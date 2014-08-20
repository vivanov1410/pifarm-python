from datetime import datetime
import json
import requests

def connect(username, password):
  # TODO: add validation
  url = 'http://pifarm.apphb.com/v1/auth/login'
  headers = {'content-type': 'application/json'}
  payload = {'username': username, 'password': password}
  
  r = requests.post(url, data=json.dumps(payload), headers=headers)
  if r.status_code == requests.codes.ok:
    account = r.json()
    
    return Api(account)
  else:
    r.raise_for_status()


class Api:
  """docstring for Api"""
  def __init__(self, account):
    self.sessionToken = account['sessionToken']
    self.url = 'http://pifarm.apphb.com/v1'
    self.pinaples = PinaplesRepository(self)
    

class PinaplesRepository:
  """docstring for PinaplesRepository"""
  def __init__(self, api):
    self._api = api

  def get(self, id):
    # TODO: add validation
    url = '{0}/pinaples/{1}'.format(self._api.url, id)
    headers = {'content-type': 'application/json', 'X-Pifarm-Session': self._api.sessionToken}
    
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
      pinaple = r.json()
      
      return Pinaple(self._api, pinaple['id'], pinaple['name'], pinaple['description'])
    else:
      r.raise_for_status()
    


class Pinaple:
  """docstring for Pinaple"""
  def __init__(self, api, id, name, description):
    self.api = api
    self.id = id
    self.name = name
    self.description = description
    self.streams = StreamsRepository(api, id)


class StreamsRepository:
  """docstring for StreamsRepository"""
  def __init__(self, api, pinapleId):
    self._api = api
    self._pinapleId = pinapleId
            
  def get(self, id):
     # TODO: add validation
    url = '{0}/streams/{1}?pinapleId={2}'.format(self._api.url, id, self._pinapleId)
    headers = {'content-type': 'application/json', 'X-Pifarm-Session': self._api.sessionToken}
    
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
      stream = r.json()
      
      return Stream(self._api, stream['id'], stream['name'], stream['description'])
    else:
      r.raise_for_status()


class Stream:
  """docstring for Stream"""
  def __init__(self, api, id, name, description):
    self.api = api
    self.id = id
    self.name = name
    self.description = description
    self.readings = ReadingsRepository(api, id)

class ReadingsRepository:
  """docstring for ReadingsRepository"""
  def __init__(self, api, streamId):
    self._api = api
    self._streamId = streamId

  def add(self, value, at=None):
    # TODO: add validation
    if at is None:
      at = datetime.utcnow()

    url = '{0}/readings'.format(self._api.url)
    headers = {'content-type': 'application/json', 'X-Pifarm-Session': self._api.sessionToken}
    payload = {'streamId': self._streamId, 'value': value, 'at': str(at)}
    
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    if r.status_code == requests.codes.ok:
      return true
    else:
      r.raise_for_status()
    