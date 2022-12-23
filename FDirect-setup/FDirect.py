from colorama import init
init() #For adding color, text stlying, etc. Do deinit() to stop.


from colorama import Fore, Style #add color. Use Fore(test), Back(background) and/or Style.
print("\n")
print(Fore.RED + "F-Direct - MAIN MENU") # Fore.RED adds color - Do print(Style.RESET_ALL) to stop after this

print(Fore.GREEN + "\n1. System Information - (CPU Temps)")
print("\n2. Hacking Tools")
print("\n3. Coming Soon!")
print("\n4. Exit")
print(Style.RESET_ALL)
    
selection = int(input("Enter: "))

if selection == 1:
    import sys_info
    exec(open('sys_info.py').read())
    import FDirect
    exec(open('FDirect.py').read())
            
elif selection == 2:
    import HackingTools
    exec(open('HackingTools.py').read())
        
elif selection == 3:
    print("Exiting!")
    import exit_script
    exec(open('exit_script.py').read())
    start_input = False
        
else:
    print("Error!")
    import FDirect
    exec(open('FDirect.py').read())
     