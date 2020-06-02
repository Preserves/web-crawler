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
print("下載各類初任人員每人每月平均經常性薪資壓縮擋...")
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
#讀取檔案
def read_data():
    with open('107年各教育程度別初任人員每人每月經常性薪資─按大職類分.json', 'r') as f:
        jdata = f.read()
        data = json.loads(jdata)
        return data


career = input('請輸入搜尋的產業(工業/礦業/製造業/營建/服務業:')
eduaction = input('請輸入教育程度(專科/大學/研究所):')

#分析並印出結果
def analysis(data, career, eduaction):
    for line in data:
            if career in line['大職業別']:
                if eduaction == '專科':
                    if line['專科-薪資'] == '—' or line['專科-薪資'] == '…':
                        line['專科-薪資'] = '查無資料'
                        print(line['大職業別'], ':', line['專科-薪資'], sep='')
                    else:
                        print(line['大職業別'], ':', line['專科-薪資'], '元', sep='')
                elif eduaction == '大學':
                    if line['大學-薪資'] == '—' or line['大學-薪資'] == '…':
                        line['大學-薪資'] = '查無資料'
                        print(line['大職業別'], ':', line['大學-薪資'], sep='')
                    else:
                        print(line['大職業別'], ':', line['大學-薪資'], '元', sep='')
                elif eduaction == '研究所':
                    if line['研究所-薪資'] == '—' or line['研究所-薪資'] == '…':
                        line['研究所-薪資'] = '查無資料'
                        print(line['大職業別'], ':', line['研究所-薪資'], sep='')
                    else:
                        print(line['大職業別'], ':', line['研究所-薪資'], '元', sep='')
def main():
    data = read_data()
    analysis(data, career, eduaction)


main()