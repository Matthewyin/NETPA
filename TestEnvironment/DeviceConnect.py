#!/usr/bin/evn python
# -*- conding:utf-8 -*-

from ncclient import manager
import difflib
import sys
#带外管理交换机
mgntsw_dict = { "host" : "172.20.13.221",
           "port" : "56332",
           "username" : "ztc",
           "password" : "lottery",
           "hostkey_verify": False,
           "device_params" : {'name' : 'h3c'}}

mgntSw = manager.connect(**mgntsw_dict)
mgntSw_startupconfig = open('../Documention/mgntSw_startupconfig.xml','w')
mgntSw_config = mgntSw.get_config(source="running")
print(mgntSw_config, file=mgntSw_startupconfig)

#borderLeaf交换机
borderleaf_dict = { "host" : "172.20.13.222",
           "port" : "56332",
           "username" : "ztc",
           "password" : "lottery",
           "hostkey_verify": False,
           "device_params" : {'name' : 'h3c'}}
borderLeaf = manager.connect(**borderleaf_dict)
borderLeaf_config = borderLeaf.get_config(source="running")
borderLeaf_startupconfig = open('../Documention/borderLeaf_startupconfig.xml','w')
print(borderLeaf_config, file=borderLeaf_startupconfig)


#Spine交换机
Spine_dict = { "host" : "172.20.13.223",
           "port" : "56332",
           "username" : "ztc",
           "password" : "lottery",
           "hostkey_verify": False,
           "device_params" : {'name' : 'h3c'}}
Spine = manager.connect(**Spine_dict)
Spine_config = Spine.get_config(source="running")
Spine_startupconfig = open('../Documention/Spine_startupconfig.xml','w')
print(Spine_config, file=Spine_startupconfig)

#AccessLeaf交换机
accessleaf01_dict = { "host" : "172.20.13.224",
           "port" : "56332",
           "username" : "ztc",
           "password" : "lottery",
           "hostkey_verify": False,
           "device_params" : {'name' : 'h3c'}}
accessLeaf01 = manager.connect(**accessleaf01_dict)
accessLeaf01_config = accessLeaf01.get_config(source="running")
accessLeaf01_startupconfig = open('../Documention/accessLeaf01_startupconfig.xml','w')
print(accessLeaf01_config, file=accessLeaf01_startupconfig)

accessleaf02_dict = { "host" : "172.20.13.225",
           "port" : "56332",
           "username" : "ztc",
           "password" : "lottery",
           "hostkey_verify": False,
           "device_params" : {'name' : 'h3c'}}
accessLeaf02 = manager.connect(**accessleaf02_dict)
accessLeaf02_config = accessLeaf01.get_config(source="running")
accessLeaf02_startupconfig = open('../Documention/accessLeaf02_startupconfig.xml','w')
print(accessLeaf02_config, file=accessLeaf02_startupconfig)

#


mgntSw_startupconfig.close()
borderLeaf_startupconfig.close()
Spine_startupconfig.close()
accessLeaf01_startupconfig.close()
accessLeaf02_startupconfig.close()

def readFile(filename):
    fileHandle = open(filename, 'r')
    text = fileHandle.read().splitlines()
    fileHandle.close()
    return text

text1_line = readFile('../Documention/accessLeaf01_startupconfig.xml')
text2_line = readFile('../Documention/accessLeaf01_startupconfig.xml')

d = difflib.HtmlDiff()
compareFile = open('../Documention/comparefile.html','w')
print(d.make_file(text1_line, text2_line), file=(compareFile))