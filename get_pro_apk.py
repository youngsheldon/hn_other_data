#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2016-12-09 18:01:56
# @Last Modified by:   anchen
# @Last Modified time: 2016-12-09 18:08:06
import os 
apk_path_root = '/opt/smmc/data_backup/apk/'

pro_apk_list = []
with open('problem_apk.txt', 'r') as f:
    for line in f:
        v = line.strip()
        pro_apk_list.append(v)

for md5 in pro_apk_list:
    pro_apk_path = apk_path_root + md5 + '.apk'
    cmd = 'cp ' + pro_apk_path + ' data/'
    os.system(cmd)