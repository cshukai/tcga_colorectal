[shchang@lewis4-r630-login-node676 wholeslides]$ more uuid2barcode.py 
#python2
#import requests
import json
import os
import pandas
import grequests

    

uuids=os.listdir('coad')
file_endpt = 'https://api.gdc.cancer.gov/legacy/files/'
df=pandas.DataFrame(columns=['uuid', 'barcode'])

urls=[]
for i,uuid in enumerate(uuids) :
    urls.append(file_endpt + uuid)

rs = (grequests.get(u) for u in urls)
grequests.map(rs)
#        x=response.json()
#        y=x['data']['file_name']
#        barcode="-".join(y.split("-")[0:3])
#        df.loc[i]=uuid+barcode
df.to_csv(path="coad.barcode.csv")
