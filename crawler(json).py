# 下載與解壓縮 財政部財政資訊中心-全國營業(稅籍)登記資料集 http://data.gov.tw/node/9400

import urllib.request #urllib2.urlopen 

import zipfile #zipfile.ZipFile

import gzip, json

# 檔案下載

print("下載全國營業(稅籍)登記資料集壓縮擋...")
downloadurl = urllib.request.urlopen('https://quality.data.gov.tw/dq_download_json.php?nid=6647&md5_url=4133da254dbcdba28a2097de48d8d606')
zipcontent= downloadurl.read()
with open("TWRAW.zip", 'wb') as f:
        f.write(zipcontent)
print("下載完成!")

# 解壓縮檔案

print("資料解壓縮...")
with zipfile.ZipFile(open('TWRAW.zip', 'rb')) as f:
    f.extractall()  

print('解壓縮完成')
print('印出json檔案')

with open('107年各教育程度別初任人員每人每月經常性薪資─按大職類分.json', 'r') as f:
    jdata = f.read()
    data = json.loads(jdata)
    print(data)


