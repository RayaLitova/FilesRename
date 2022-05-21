import os

name = "Raya_Litova_"
files = os.listdir()
for i in files:
	if(i!="rename.py"):
		#os.rename(i, i[len(name):]) #revert
		os.rename(i, name+i) #rename