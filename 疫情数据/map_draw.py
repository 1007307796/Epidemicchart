from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker


class Draw_map():
    def to_map_city(self,area,variate,province,update_time):
        pieces = [
            {"max": 99999999, 'min': 10000, 'label': '>10000', 'color': '#DD001B'},
            {"max": 9999, 'min': 1000, 'label': '1000-9999', 'color': '#D2932A'},
            {"max": 999, 'min': 100, 'label': '100-999', 'color': '#0CBF7B'},
            {"max": 99, 'min': 10, 'label': '10-99', 'color': '#FFF2CD'},
            {"max": 9, 'min': 0, 'label': '<10', 'color': '#FFFFFF'},
        ]
        c = (
            Map(init_opts=opts.InitOpts(width='1360px',height='600px'))
                .add("累计确诊人数", [list(z) for z in zip(area, variate)], province)
                .set_global_opts(
                title_opts=opts.TitleOpts(title="%s地区疫情分布图" % province,subtitle='截至%s' % update_time),
                visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True,pieces=pieces),
            )
                .render("{}疫情分布图.html".format(province))
        )

    def to_map_china(self,area,variate,update_time):
        pieces = [
            {"max":99999999,'min':10000,'label':'>10000','color':'#DD001B'},
            {"max":9999,'min':1000,'label':'1000-9999','color':'#D2932A'},
            {"max":999,'min':100,'label':'100-999','color':'#0CBF7B'},
            {"max":99,'min':10,'label':'10-99','color':'#FFF2CD'},
            {"max":9,'min':0,'label':'<10','color':'#FFFFFF'},
        ]
        c = (
            Map(init_opts=opts.InitOpts(width='1360px',height='600px'))
                .add("累计确诊人数", [list(z) for z in zip(area, variate)], "china")
                .set_global_opts(
                title_opts=opts.TitleOpts(title="中国疫情地图分布",subtitle='截至%s' % update_time,pos_left='center',pos_top='30px'),
                visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True,pieces=pieces),
            )
                .render("中国疫情地图.html")
        )