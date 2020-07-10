import requests
from lxml import etree
import json
import openpyxl

url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia'
response = requests.get(url)
response.encoding = 'utf-8'
html = etree.HTML(response.text)
result = html.xpath('//script[@type="application/json"]/text()')
result = result[0]
# json.loads 将字符串传唤为python数据类型
result = json.loads(result)
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "国内疫情"
ws.append(['省份','累计确诊','死亡','治愈','现有确诊','累计确诊增量','死亡增量','治愈增量','现有确诊增量'])
result_in = result['component'][0]['caseList']
result_out = result['component'][0]['globalList']
for each in result_in:
    temp_list = [each['area'],each['confirmed'],each['died'],each['crued'],each['curConfirm'],each['confirmedRelative'],
                 each['diedRelative'],each['curedRelative'],each['curConfirmRelative']]
    ws.append(temp_list)
for each in result_out:
    sheet_title = each['area']
    ws_out = wb.create_sheet(sheet_title)
    ws_out.append(['国家','累计确诊','死亡','治愈','现有确诊','累计确诊增量'])
    for country in each['subList']:
        temp_list = [country['country'],country['confirmed'],country['died'],country['crued'],country['curConfirm'],
                     country['confirmedRelative']]
        ws_out.append(temp_list)
wb.save('./data.xlsx')