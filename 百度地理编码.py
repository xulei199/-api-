#xulei,2022.08.09
#pycharm 2022.1.3
import json
import pandas as pd
from urllib import request
#读取地址坐标#

dz = open(r'D:\####################',encoding='utf-8').read().splitlines()#设置txt读取的位置，一个地址占一行
ak='#########################################'#设置百度ak
url = 'https://api.map.baidu.com/geocoding/v3/?address={0}&output=json&ak={1}'#请求链接
rus=[]#空列表
lon1=[]#空列表
lat1=[]#空列表
ID=0#计数器
biaotou=['lon','lat']


for line in dz:#你猜
    location=line.split()
    html=request.urlopen(url.format(str(location),str(ak))).read()
    js=json.loads(html)
    js2 = json.loads(html)

    jiaoyan=js['status']
    if jiaoyan == 0:#你猜
        lons = js2['result']["location"]['lng']
        lats = js2['result']["location"]['lat']
        conf = js2['result']["confidence"]
        comper = js2['result']["comprehension"]
        lon1.append(str(lons))
        lat1.append(str(lats))
        rus.append(str(lons) + ";" + str(lats)+ ";" +str(conf) + ";" + str(comper))
        ID += 1
        print('正在爬取第{0}个坐标！，请耐心等待！该坐标正常！'.format(ID))
    if jiaoyan == 1:#你猜
        lons = '00000'
        lats = '00000'
        conf = '00000'
        comper = '00000'
        lon1.append(str(lons))
        lat1.append(str(lats))
        rus.append(str(lons) + ";" + str(lats)+ ";" +str(conf) + ";" + str(comper))
        ID += 1
        print('正在爬取第{0}个坐标！，请耐心等待！该坐标异常！！！'.format(ID))
    
    output = open(r'C:\####################', 'w')#txt输出到这个路径
    
    output.write('lon;lat;confidence;comprehension\n')#表头
    for russ in rus:
        output.write(russ+'\n')
    output.close()#关
df = pd.DataFrame({'lon':lon1,'lat':lat1})
df.to_csv('C:\\####################')#csv输出到这个路径

print('共爬取{0}个坐标！'.format(ID))#计数器！！

