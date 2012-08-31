#!/bin/env python
# -*- coding=utf-8 -*-

# copied and modified from http://dango-akachan.appspot.com/?p=98001 

import sys
reload(sys)
sys.setdefaultencoding("utf8")

import urllib2
from xml.dom.minidom import parseString

url="http://www.webxml.com.cn/webservices/weatherwebservice.asmx/getWeatherbyCityName?theCityName=北京"
request = urllib2.Request(url)
response = urllib2.urlopen(request);
#print response.geturl().decode('utf-8').encode('gbk')
xmlstring = response.read();
dom =parseString(xmlstring)

strings = dom.getElementsByTagName("string")

def getText(nodelist):
    rc = ""
    for node in nodelist:
	    if node.nodeType == node.TEXT_NODE:
		    rc = rc + node.data
    return rc

#今天的温度和天气
today_temperature = getText(strings[5].childNodes)
today_weather = getText(strings[6].childNodes)
today_wind = getText(strings[7].childNodes)

#实况
current_weather = getText(strings[10].childNodes)


#明天的温度和天气
tomorrow_temperature = getText(strings[12].childNodes)
tomorrow_weather = getText(strings[13].childNodes)
tomorrow_wind = getText(strings[14].childNodes)

#后天的温度和天气
the_day_after_tomorrow_temperature = getText(strings[17].childNodes)
the_day_after_tomorrow_weather = getText(strings[18].childNodes)
the_day_after_tomorrow_wind = getText(strings[19].childNodes)

#省份城市
province = getText(strings[0].childNodes)
city = getText(strings[1].childNodes)

today_weather_forecast = today_weather + " " + today_temperature + " " + today_wind 
tomorrow_weather_forecast = tomorrow_weather + " " + tomorrow_temperature + " " + tomorrow_wind
the_day_after_tomorrow_weather_forecast = the_day_after_tomorrow_weather + " " + the_day_after_tomorrow_temperature + " " + the_day_after_tomorrow_wind

weather = current_weather + "\n" + today_weather_forecast + "\n" + tomorrow_weather_forecast + "\n" + the_day_after_tomorrow_weather_forecast

print province, city
print weather
