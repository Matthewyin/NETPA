#!/usr/bin/evn python
# -*- conding:utf-8 -*-

from ncclient import manager

device = { "host" : "172.20.13.221",
           "port" : "56332",
           "username" : "ztc",
           "password" : "lottery",
           "hostkey_verify": False,
           "device_params" : {'name' : 'h3c'}}

mgntSw = manager.connect(**device)
config = mgntSw.get_config(source="running")
print(config)

