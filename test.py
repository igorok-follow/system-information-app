import psutil
from colorama import Fore
import os

def show_desktop_stats():
	# print("Platform: " + platform.platform())
	# print("Platform version: " + platform.version())
	# print("Processor information: " + platform.processor())

	while True:
		change = input(Fore.WHITE + "$ ")
		change.lower().strip().replace(" ", "")
			
		if change == "help":
			print(Fore.RED + "Commands: " + Fore.WHITE)
			print(Fore.GREEN + "	1. help")
			print(Fore.GREEN + "	2. cpu_usage")
			print(Fore.GREEN + "	3. ram_usage")
			print(Fore.GREEN + "	4. clear_console")
			# print(Fore.GRAY + "	5. disk_usage")
			print(Fore.GREEN + "	5. info")
		elif change == "cpu_usage":
			print(Fore.WHITE + "Cpu usage level: " + str(psutil.cpu_percent(interval = 1)))
		elif change == "ram_usage":
			print("Ram usage level: " + str(psutil.virtual_memory()[2]))
		# elif change == "disk_usage":
		# 	print("Disk usage level: " + str(psutil.disk_usage()[0]))
		elif change == "info":
			print(Fore.BLUE)
			print("   .__                                  __               _____       .__   .__                   ")
			print("   |__|  ____    ____  _______   ____  |  | __         _/ ____\____  |  |  |  |    ____  __  _  __")
			print("   |  | / ___\  /  _ \ \_  __ \ /  _ \ |  |/ /  ______ \   __\/  _ \ |  |  |  |   /  _ \ \ \/ \/ /")
			print("   |  |/ /_/  >(  <_> )|  |  \/(  <_> )|    <  /_____/  |  | (  <_> )|  |__|  |__(  <_> ) \     / ")
			print("   |__|\___  /  \____/ |__|     \____/ |__|_ \          |__|  \____/ |____/|____/ \____/   \/\_/  ")
			print("      /_____/                              \/                                                   ")
			print("")
			print(Fore.WHITE + "Creator's github :" + Fore.RED + " https://github.com/igorok-follow")
			print(Fore.WHITE)
		elif change == "clear_console":
			os.system('cls')
		elif change == "":  #should will fix bugs
			pass
		else:
			print(Fore.WHITE + "Invalid syntax")


if __name__ == '__main__':
	show_desktop_stats()