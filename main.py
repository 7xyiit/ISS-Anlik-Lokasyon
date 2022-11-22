import pandas as pd
import plotly.express as px
import time

json_info = 'http://api.open-notify.org/iss-now.json'

def ISSizleyici():
    yorunge = pd.read_json(json_info)
    yorunge['latitude'] = yorunge.loc['latitude', 'iss_position']
    yorunge['longitude'] = yorunge.loc['longitude', 'iss_position']
    harita = px.scatter_geo(yorunge, lat='latitude', lon='longitude')
    harita.show()
    
ISSizleyici()