import os
import collections
from pprint import pprint
import sys
import time
import colorama

colorama.init(autoreset=True)

otherExtensions = []
errors = []
bannerColor = colorama.Fore.GREEN

def displayPercentage(arrayOfFiles):
	increaseRate = round(100 / len(arrayOfFiles))
	val = 0
	maxVal = 100
	while val <= maxVal:
		if(val + increaseRate > 100):
			print("100%")
			break
		print(f"{val}%")
		time.sleep(0.05)
		os.system('cls')
		val = val + increaseRate

def Manual_Extension(InputLocation):
	if not os.path.exists(InputLocation):
		print("Invalid Input Location!")
		input("> ")
		main()
	PATH = os.path.normpath(InputLocation)
	folderType = input("Extension Type: ").lower()
	# File Type To Folder
	file_mappings = collections.defaultdict()
	for filename in os.listdir(PATH):
		file_type = filename.split('.')[-1]
		if(file_type == folderType):
			file_mappings.setdefault(file_type, []).append(filename)
		else:
			if(file_type not in otherExtensions):
				otherExtensions.append(file_type)


	# Move All Files Seperate Folders
	for folder_name, folder_items in file_mappings.items():
		folder_path = os.path.join(PATH, folder_name)
		if not os.path.exists(folder_path):
			os.mkdir(folder_path)

		for folder_item in folder_items:
			source = os.path.join(PATH, folder_item)
			destination = os.path.join(folder_path, folder_item)
			# print(f'{folder_item} to {folder_name}/{folder_item}')
			try:
				os.rename(source, destination)
			except Exception as e:
				errors.append(e)
				continue
	displayPercentage(folder_items)
	print("Manual Execution Finish!")
	runAgain = input("Press 'X' to Exit, or Enter To Continue.")
	if(runAgain.lower() == "x"):
		sys.exit()
	else:
		main()

def Auto_Extension(InputLocation):

	if not os.path.exists(InputLocation):
		print("Invalid Input Location!")
		input("> ")
		main()
	PATH = os.path.normpath(InputLocation)

	# File Type To Folder
	file_mappings = collections.defaultdict()
	for filename in os.listdir(PATH):
		file_type = filename.split('.')[-1]
		file_mappings.setdefault(file_type, []).append(filename)

	# pprint(file_mappings)

	# Move All Files Seperate Folders
	for folder_name, folder_items in file_mappings.items():
		folder_path = os.path.join(PATH, folder_name)
		if not os.path.exists(folder_path):
			os.mkdir(folder_path)

		for folder_item in folder_items:
			source = os.path.join(PATH, folder_item)
			destination = os.path.join(folder_path, folder_item)
			# print(f'{folder_item} to {folder_name}/{folder_item}')
			try:
				os.rename(source, destination)
			except Exception as e:
				errors.append(e)
				continue
	displayPercentage(folder_path)
	print("Automatic Execution Finish!")
	print("")
	input("Press any key to exit!")

def main():
	print(bannerColor + r'   ___      ____                _        ')
	print(bannerColor + r'  / _ \___ / __ \_______ ____  (_)__ ___ ')
	print(bannerColor + r" / , _/ -_) /_/ / __/ _ `/ _ \/ /_ // -_)")
	print(bannerColor + r"/_/|_|\__/\____/_/  \_, /_//_/_//__/\__/ ")
	print(bannerColor + r'                   /___/                 ')

	print(bannerColor + '  _______________________________')
	print(bannerColor + ' |                               |')
	print(bannerColor + ' |   Manual Execute: 0           |')
	print(bannerColor + ' |   Auto Execute: 1             |')
	print(bannerColor + ' |   Exit: X                     |')
	print(bannerColor + ' |_______________________________|')
	print()
	print(bannerColor + ' Messed Up Folder To Clean Folders, By Automatically or Manually File Separation (only by the mentioned extension)!')
	print(bannerColor + ' -------------------------------------------------------------------------------')
	                                        
	typeOfExecute = input("> ")
	time.sleep(1)

	if (typeOfExecute == "0"):
		usrpath = input("Location: ")
		Manual_Extension(usrpath)
		print("")
		print(otherExtensions)
		# print("")
		# print(errors)
		print("")
		input(">")

	elif(typeOfExecute == "1"):
		usrpath = input("Location: ")
		Auto_Extension(usrpath)
		# print("")
		# print("")
		# print(errors)
		print("")
		input(">")
	elif(typeOfExecute.lower() == "x"):
		sys.exit()
	else:
		print("Invalid Input! Try Again. OR press 'X' key to Exit")
		commandInput = input("> ")
		if(commandInput.lower() == "x"):
			sys.exit()
		else:
			main()

main()

