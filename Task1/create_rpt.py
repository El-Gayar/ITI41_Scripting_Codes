#!/usr/bin/python3

import os
import re

path ="task_ws"


list_path=os.listdir("{0}/".format(path))

for i in list_path :
	rtl=0
	sdf=0
	scr=0
	other=0
	d_path=os.listdir("{0}/{1}".format(path,i)) 
	for d in d_path:
		if d.endswith(".v"):
			rtl=rtl+1
		elif d.endswith(".sdf"):
			sdf=sdf+1
		elif d.endswith(".sh") or d.endswith(".py"):
			scr=scr+1
		else:
			other=other+1
	print ("************Report of {0}*****************".format(i))
	print ("==>No. of total files: {0}".format(len(d_path)))
	if i == "directory_A" or i == "directory_B":
		print ("==>No. of rtl files: {0}".format(rtl))
		print ("==>No. of sdf files: {0}".format(sdf))
		print ("==>No. of scr files: {0}".format(scr))
		print ("==>No. of other files: {0}".format(other))


os.system("tree task_ws/")
