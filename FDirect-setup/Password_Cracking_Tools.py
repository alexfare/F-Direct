from colorama import init
init() #For adding color, text stlying, etc. Do deinit() to stop.


from colorama import Fore, Style #add color. Use Fore(test), Back(background) and/or Style.
print(Fore.RED + "F-Direct - Password Cracking Tools")

print(Fore.GREEN + "\n1. Brute Force - SSH")
print("\n2. FTP Cracker")
print("\n3. WIFI Cracker ")
print("\n4. Key Logger ")
print("\n5. Reverse Shell")
print("\n6. PDF Cracker")
print("\n7. Zip File Cracker")
print("\n8. MAIN MENU")
print(Style.RESET_ALL)
    
selection = int(input("Enter: "))

if selection == 1:
    import bruteforce_start
    exec(open('bruteforce_start.py').read())
            
elif selection == 2:
    import ftp_cracker_start
    exec(open('ftp_cracker_start.py').read())
        
elif selection == 3:
    print("Exiting!")
    import exit_script
    exec(open('exit_script.py').read())
    start_input = False
        
else:
    print("Error!")
    import Password_Cracking_Tools
    exec(open('Password_Cracking_Tools.py').read())
