#!/usr/bin/python3


import os
import shutil
import sys
import re

status =0

if sys.argv[1] == "c1":
	try :
		path1=sys.argv[2]
	except :
		print("PLZ enter a path ")
		exit(0)
	here = os.path.exists(path1) 
	here_A = os.path.exists("{0}/directory_A".format(path1)) 
	here_B = os.path.exists("{0}/directory_B".format(path1)) 
	if here :
		if here_A and here_B:
			status = 1
		else:
			print ("Directory_A or Directory_B is not exist")
	else:
		print ("Directory is not exist")
	exit(status)
elif sys.argv[1] == "c1-1":
	path1=sys.argv[2]
	here_c = os.path.exists("{0}/directory_C".format(path1))
	if here_c:
		status =1
	else:
		print ("Directory_C is not exist")
	exit(status)
elif sys.argv[1] == "c2":
	try:
		prefix=sys.argv[2]
	except:
		print ("PLZ enter a prefix to add (Must be ITI_ or DIC_)")
		exit(0)
	if prefix == "ITI_" or prefix == "DIC_" :
		prefix=prefix
	else :
		print("PLZ enter ITI_ or DIC_")
		exit(0)
	remove =0
	try:
		remove=sys.argv[3]
	except:
		print ("PLZ enter remove_comment if you need")
		exit (1)
	if remove == "remove_comment":
		exit (1)
	else :
		print("Write (remove_comment)")

elif sys.argv[1] == "c2-1":
	path1=("{0}/directory_C".format(sys.argv[2]))
	list_c=os.listdir(path1)
	for file in list_c:
		f1=open("{1}/{0}".format(file,path1),"r")
		x=f1.read()
		if file.endswith(".v"):
			if not re.search(r"(^)[^//]module\s+{0}(\w+)".format(sys.argv[4]),x,re.MULTILINE) :
				print ("You have a problem in your .v files")
				exit(0)
			
			try :
				if sys.argv[5] == "remove_comment":
					if re.search(r"\/\/[^directory].*",x):
						print ("You still have comment in your files")
						exit(0)
			except:
				path1=path1
		if file.endswith(".sdf"):
			if not re.search(r"{0}{1}".format(sys.argv[4],sys.argv[3]),x):
				print ("You have a problem in your sdf files")
				exit(0)
	exit(1)			

elif sys.argv[1] == "c3":
	path1=sys.argv[2]
	rtl=os.listdir("{0}/rtl".format(path1))
	other=os.listdir("{0}/other".format(path1))
	scr=os.listdir("{0}/scr".format(path1))
	sdf=os.listdir("{0}/sdf".format(path1))

	for x in rtl:
		if not x.endswith(".v"):
			print ("Error :{0}is not under rtl".format(x))
			exit(0)
	for x in scr:
		if not (x.endswith(".sh") or x.endswith(".py")):
			print ("Error :{0}is not under scr".format(x))
			exit(0)
	for x in sdf:
		if not x.endswith(".sdf"):
			print ("Error :{0}is not under sdf".format(x))
			exit(0)
	for x in other:
		if x.endswith(".v") or x.endswith(".sh") or x.endswith(".py")or x.endswith(".sdf"):
			print ("Error :{0}is not under rtl".format(x))
			exit(0)
	exit(1)		
