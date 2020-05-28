# 下載與解壓縮 財政部財政資訊中心-全國營業(稅籍)登記資料集 http://data.gov.tw/node/9400
import zipfile #zipfile.ZipFile
import gzip, json
import urllib.request as req 
url = "https://data.gov.tw/dataset/6647"         #開放平台網址 
#用headers模擬人為操作
request = req.Request(url, headers = { 
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
})
#用uft-8代碼讀取原始碼
with req.urlopen(request) as response: 
    data = response.read().decode("utf-8")
#解析原始碼
import bs4  
soup = bs4.BeautifulSoup(data, "html.parser")
#抓取json載點網址
a = []
for link in soup.find_all('a'):
    if 'json' in link.get('href'):
        a.append(link.get('href'))
download_link = ''.join(a)
# 檔案下載
print("下載全國營業(稅籍)登記資料集壓縮擋...")
downloadurl = req.urlopen(download_link)
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