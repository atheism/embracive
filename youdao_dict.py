#!/bin/env python
#coding=utf-8

import sys
import json
import urllib2
world = sys.argv[1]
#data = '{"type":"EN2ZH_CN","errorCode":0,"elapsedTime":79,"translateResult":[[{"src":"stale","tgt":"陈腐"}]],"smartResult":{"type":1,"entries":["","n. 尿","adj. 陈腐的；不新鲜的","vt. 使变旧；变得不新鲜"]}}'
data = urllib2.urlopen("http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict.top?type=AUTO&i=%s&doctype=json&xmlVersion=1.4&keyfrom=fanyi.web&ue=UTF-8&typoResult=true&flag=false" % world)

results = json.loads(data.read())

print results["translateResult"][0][0]["tgt"]
for i in range(len(results["smartResult"]["entries"])) :
	print u"" , results["smartResult"]["entries"][i]
