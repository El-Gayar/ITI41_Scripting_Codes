#!/usr/bin/python3

import os
import shutil

path = "task_ws/Directory_C"

os.mkdir(path)

a=os.listdir("task_ws/directory_A")
b=os.listdir("task_ws/directory_B")
c=[]

for x in a:
	if x in b:
		z=x.rsplit(".")
		suffix="_B.".join(z)
		shutil.copyfile("task_ws/directory_B/{0}".format(x),"task_ws/Directory_C/{0}".format(suffix))
		
	else:
		e=x.rsplit(".",1)
		suffix2="_A.".join(e)
		shutil.copyfile("task_ws/directory_A/{0}".format(x),"task_ws/Directory_C/{0}".format(suffix2))
		