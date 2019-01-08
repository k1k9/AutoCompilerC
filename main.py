#!/usr/bin/python3
import os
import sys

import imports.functions as funcs
import imports.colors		 as color



### START ###
os.system('reset')
print(color.HEADER + "Welcome in Easy Linux Auto-Comiler" + color.ENDC)
files = funcs.get_files()

if type(files) == type(None):
	print(color.FAIL + "\nThis folder is empty\n" + color.ENDC)
	sys.exit()



### MENU ###
funcs.show_menu(files)

# Get file
while True:
	chose = input("File (number): ")

	try:
		chose = int(chose)-1

		if chose < len(files)-1:
			watching_file = files[chose]
			break
		else: print(color.FAIL + "Chose option from menu\n\n" + color.ENDC)
	except: print(color.FAIL + "Chose option from menu\n\n" + color.ENDC)



### WATCHING FILE ###
path_to_file = files[len(files)-1]+"/"+watching_file
last_update  = os.path.getmtime(path_to_file)
save_counter = 0

funcs.status(watching_file, save_counter)

while True:
	try:
		check_last_update = os.path.getmtime(path_to_file)
		if check_last_update > last_update:
			last_update = check_last_update
			save_counter += 1
			funcs.status(watching_file, save_counter)
			funcs.execute(watching_file, path_to_file)
	except:
		pass