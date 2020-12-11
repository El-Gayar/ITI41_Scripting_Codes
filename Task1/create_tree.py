#!/usr/bin/python3

import os
import shutil

path = "task_ws/Directory_C"
other = "task_ws/other"
rtl = "task_ws/rtl"
scr = "task_ws/scr"
sdf = "task_ws/sdf"

path_list=os.listdir(path)
os.mkdir(other)
os.mkdir(rtl)
os.mkdir(scr)
os.mkdir(sdf)

for file in path_list :
	if file.endswith(".v"):
		shutil.move("task_ws/Directory_C/{0}".format(file),"task_ws/rtl/{0}".format(file))
	elif file.endswith(".sh") or file.endswith(".py"):
		shutil.move("task_ws/Directory_C/{0}".format(file),"task_ws/scr/{0}".format(file))
	elif file.endswith(".sdf"):
		shutil.move("task_ws/Directory_C/{0}".format(file),"task_ws/sdf/{0}".format(file))
	else:
		shutil.move("task_ws/Directory_C/{0}".format(file),"task_ws/other/{0}".format(file))

os.rmdir(path)