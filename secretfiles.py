"""

	- get all file names
	- for each file
		- rename

used os.listdir()
"""
import os
import string

def rename_files():
	# step-1: get filenames from the folder
	file_list = os.listdir(r"F:\fullPy\prank")
	print(file_list)
	saved_path = os.getcwd()
	os.chdir(r"F:\fullPy\prank")

	#for each file, rename file
	for file_name in file_list:
		print("Old Name - "+file_name)
		print("New Name - "+file_name.translate(None, '0123456789'))
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)
	print file_list
rename_files()