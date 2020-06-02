# 下載與解壓縮 財政部財政資訊中心-全國營業(稅籍)登記資料集 http://data.gov.tw/node/9400
import zipfile #zipfile.ZipFile
import gzip, json
import urllib.request as req 
def crawler():
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
    return download_link


# 檔案下載
def download_file(download_link):
    print("下載107年各教育程度別初任人員每人每月經常性薪資...")
    downloadurl = req.urlopen(download_link)
    zipcontent= downloadurl.read()
    with open("壓縮檔.zip", 'wb') as f:
            f.write(zipcontent)
    print("下載完成!")
    # 解壓縮檔案
    print("資料解壓縮...")
    with zipfile.ZipFile(open('壓縮檔.zip', 'rb')) as f:
        f.extractall()  
    print('解壓縮完成')


#讀取檔案
def read_data(filename):
    with open(filename, 'r') as f:
        jdata = f.read()
        data = json.loads(jdata)
        return data


#輸入並檢查是否正確
def input_data():
    career = input('請輸入搜尋的產業(工業/礦業/製造業/營建/服務業):')
    while True:
        if career == '工業' or career == '礦業' or career == '製造業' or career == '營建' or career == '服務業' :
            break
        else:
            career = input('請輸入"正確"的產業(工業/礦業/製造業/營建/服務業):')
    eduaction = input('請輸入教育程度(專科/大學/研究所):')
    while True:
        if eduaction == '專科' or eduaction == '大學' or eduaction == '研究所':
            break
        else:
            eduaction = input('請輸入"正確"教育程度(專科/大學/研究所):')
    return career, eduaction


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


#分析的主程式
def main():
    download_link = crawler()
    download_file(download_link)
    data = read_data('107年各教育程度別初任人員每人每月經常性薪資─按大職類分.json')
    career, eduaction = input_data()
    analysis(data, career, eduaction)
    
main()