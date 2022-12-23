print("F-Direct")

start_input = True

def start_menu():
    print("1. Port Scanner")
    print("2. SubDomain Scanner")
    print("3. XSS Vulnerability Scanner")
    print("4. MAIN MENU")

    
    selection = int(input("Enter: "))

    if selection == 1:
        import sys_info
        exec(open('sys_info.py').read())
            
    elif selection == 2:
        print("Coming Soon!")
        
    elif selection == 3:
        print("Exiting!")
        import exit_script
        exec(open('exit_script.py').read())
        start_input = False
        
    else:
        print("Error!")
     
while start_input == True:
    start_menu()