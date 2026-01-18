from contextlib import redirect_stderr
from datetime   import datetime
from json       import loads
from core       import env
from requests   import get

class API:
    "Application Programming Interface"

    host = env["api"]["host"]
    port = env["api"]["port"]
    auth = env["api"]["auth"]
    zone = env["api"]["zone"]

    @classmethod
    def request(cls, path: str) -> dict:

        path = f"https://{cls.host}:{cls.port}/api/{path}"
        auth = {"headers":{"Authorization": cls.auth}, "verify":0}

        with redirect_stderr(None):
            
            if (response := get(path, **auth)).ok:
                return cls.tzoning(loads(response.text))
            else:
                raise ConnectionError(
                    f'{response.status_code} returned: \"{path}\"')

    @classmethod
    def tzoning(cls, data: dict) -> dict:
        
        for key, val in data.items():
            
            if   type(val) == dict: data[key] = cls.tzoning(val)
            elif type(val) == list: val = [cls.tzoning(i) for i in val]

            try: 
                data[key] = datetime.fromisoformat(f"{val}")\
                    .astimezone(cls.zone).isoformat()
            except:   
                data[key] = val
            
        return data