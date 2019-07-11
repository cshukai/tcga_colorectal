#python2
import requests
import json
import os
import pandas

uuids=os.listdir('coad')
file_endpt = 'https://api.gdc.cancer.gov/legacy/files/'
df=pandas.DataFrame(columns=['uuid', 'barcode'])
for i,uuid in enumerate(uuids) :
        response = requests.get(file_endpt + uuid)
        x=response.json()
        y=x['data']['file_name']
        barcode="-".join(y.split("-")[0:3])
        df.loc[i]=uuid+barcode
df.to_csv(path="coad.barcode.csv")
