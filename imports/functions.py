#!/bin/usr/python3
import os
import sys

import imports.colors as color

def get_files():
	try: user_input  = input("Drag and drop here your project folder (or entry full path): ")
	except: sys.exit()
	folder_path = ""

	# Clear path
	for i in range(len(user_input)):
		if user_input[i] is "'" or user_input[i] is " ":
			pass
		else:
			folder_path += user_input[i]

	# Get list of files
	try:
		result = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,f))]
		result.append(folder_path)
		return result
	except Exception as e:
		print(color.FAIL + "" + e + color.ENDC)
		sys.exit()




def show_menu(files):
	print(color.WARNING + "\nChose file to watching for compailing" + color.ENDC)
	for i,j in enumerate(files):
		if i != len(files)-1:
			print("{}. {}".format(i+1, j))
	print("\n0. Exit\n\n")




def status(file, counter):
	os.system("reset")
	print(color.HEADER + "Im watching...\n" + color.ENDC)

	print("Watching file: {}{}{}".format(color.BOLD, file, color.ENDC))
	print("How many saves: {}{}{}".format(color.BOLD, counter, color.ENDC))



def execute(file, path):
	columns = int(os.popen('tput cols').read())
	center  = int(columns/2) - 4
	print("\n\n" + color.WARNING)
	print("#" * columns)
	print(' '*center + color.BOLD+"COMPILED"+color.ENDC+color.WARNING)
	print("#" * columns)
	print('\n\n' + color.ENDC)


	# Get extension
	for i,j in enumerate(file):
		if j == '.':
			extension = file[i+1:]

	if extension == 'c' or extension == 'cc' or extension == 'cpp':
		os.system('g++ {} -o output.o && ./output.o'.format(path))


def clear():
	print("CLEAREING")