import json
import map_draw
import data_get

with open('data.json','r') as file:
    data = file.read()
    data = json.loads(data)
map = map_draw.Draw_map()
datas = data_get.Get_data()
datas.get_data()
update_time = datas.get_time()
datas.parse_data()
def china_map():
    area = []
    confirmed = []
    for each in data:
        area.append(each['area'])
        confirmed.append(each['confirmed'])
    map.to_map_china(area,confirmed,update_time)


def province_map():
    for each in data:
        city = []
        confirmeds = []
        province = each['area']
        for each_city in each['subList']:
            city.append(each_city['city']+'市')
            confirmeds.append(each_city['confirmed'])
            map.to_map_city(city,confirmeds,province,update_time)
        if province == '上海' or '北京' or '天津' or '重庆':
            for each_city in each['subList']:
                city.append(each_city['city'])
                confirmeds.append(each_city['confirmed'])
                map.to_map_city(city, confirmeds, province, update_time)


china_map()
province_map()