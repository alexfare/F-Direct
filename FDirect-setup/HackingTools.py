from colorama import init
init() #For adding color, text stlying, etc. Do deinit() to stop.


from colorama import Fore, Style #add color. Use Fore(test), Back(background) and/or Style.
print("\n")
print(Fore.RED + "F-Direct - Hacking Tools") #title

#list of options
print(Fore.GREEN + "\n1. Password Tools")
print("\n2. Scanning Tools - COMING SOON")
print("\n3. Extractor Tools - COMING SOON")
print("\n4. Encryption Tools - COMING SOON")
print("\n5. Misc Tools - COMING SOON")
print("\n6. MAIN MENU")
print(Style.RESET_ALL)
    
selection = int(input("Enter: "))

if selection == 1:
    import Password_Cracking_Tools
    exec(open('Password_Cracking_Tools.py').read())
            
elif selection == 2:
    import Scanning_Tools
    exec(open('Scanning_Tools.py').read())
        
elif selection == 3:
    import Scanning_Tools
    exec(open('Scanning_Tools.py').read())
        
elif selection == 4:
    import Scanning_Tools
    exec(open('Scanning_Tools.py').read())
        
elif selection == 5:
    import Scanning_Tools
    exec(open('Scanning_Tools.py').read())
        
elif selection == 6:
    import FDirect
    exec(open('FDirect.py').read())
    
        
else:
    print("Error!")
    import HackingTools
    exec(open('HackingTools.py').read())
