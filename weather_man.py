#!/bin/env python
# -*- coding=utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from urllib import urlopen
from lxml import etree
#import xml.etree.ElementTree as etree


def get_factor(condition) :
	if condition.tag == "forecast_information" :
		for factor in condition :
			if factor.tag == "city" :
				print "%s" % factor.attrib['data'] 
			if factor.tag == "forecast_date" :
				print "%s" % factor.attrib['data'] 

	if condition.tag == "current_conditions" :
		for factor in condition :
			if factor.tag == "condition" :
				print u"当前天气：" + "%s" % factor.attrib['data'] 
			if factor.tag == "temp_c" :
				print u"    气温：" + "%s" % factor.attrib['data'] 
			if factor.tag == "humidity" :
				print "    %s" % factor.attrib['data'] 
			if factor.tag == "wind_condition" :
				print "    %s" % factor.attrib['data'] 

	if condition.tag == "forecast_conditions" :
		for factor in condition :
			if factor.tag == "day_of_week" :
				day_of_week = factor.attrib['data']
				#print "%s" % factor.attrib['data'] 
			if factor.tag == "low" :
				low = factor.attrib['data']
			if factor.tag == "high" :
				high = factor.attrib['data']
			if factor.tag == "condition" :
				cond = factor.attrib['data']
				#print u"天气：" + "%s" % factor.attrib['data'] 
		print day_of_week + u"：" + cond + u" 温度：" + low + "-" + high 

city = "beijing"

if len(sys.argv) > 1 :
	city = sys.argv[1]

url = "http://www.google.com/ig/api?hl=zh-cn&weather=%s,china" % city

webdata = urlopen(url).read()
utf8_webdata = webdata.decode('GBK')
#print utf8_webdata

root = etree.XML(utf8_webdata)
#tree = etree.parse("utf8.xml")
#
#root = tree.getroot()
#
for child in root :
	for condition in child :
		get_factor(condition)
	#	for factor in condition :
	#		if factor.attrib.has_key("data") > 0 :
	#			print "%s" % factor.attrib['data']

