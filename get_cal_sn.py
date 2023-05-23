import requests
import json
import pandas as pd
PLATFORMTYPE = "&PLATFORM_TYPE=NAVIS_EBR"
BASE_URL = "https://db.whoifloatgroup.org"
#BASE_URL = "http://127.0.0.1:8000"

def get_cal(floatnum):
    floatnum = "FLOAT_SERIAL_NO=" + str(floatnum) + PLATFORMTYPE
    response = requests.get(BASE_URL+"/api/cal?"+floatnum)

    if response.status_code==200:
        return pd.DataFrame(json.loads(response.content))
    raise Exception('ERROR: ', response.status_code)