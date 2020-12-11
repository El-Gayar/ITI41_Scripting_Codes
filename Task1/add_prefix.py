#!/usr/bin/python3

import os
import shutil
import re
import sys

# path = "task_ws/Directory_C"
path=sys.argv[1]

path_list=os.listdir(path)

for file in path_list :
	if file.endswith(".v"):
		f1=open("{1}/{0}".format(file,path),"r")
		x=f1.read()
		m=re.search(r'(^)[^//]module\s+(\w+)',x,re.MULTILINE).group(2)
		x=re.sub("{0}".format(m),"{1}{0}".format(m,sys.argv[2]),x)
		if sys.argv[3] == "r":
			x=re.sub(r"\/\/[^directory].*","",x)
		f1=open("{1}/{0}".format(file,path),"w")
		f1.write(x)
	elif file.endswith(".sdf"):
		f2=open("{1}/{0}".format(file,path),"r")
		y=f2.read()
		y=re.sub("top","{0}top".format(sys.argv[2]),y)
		f2=open("{1}/{0}".format(file,path),"w")
		f2.write(y)



