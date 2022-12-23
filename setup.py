
print("1. Set-up")
print("2. Exit")
setup = int(input("Enter: "))
if setup == 1:
    print("Unzipping Files")
    import unzip
    exec(open('unzip.py').read())
    print("Downloading Requirements...")
    import os
    os.system('cmd /k "pip3 install -r requirements.txt"')
    print("Downloading Requirements...")
if setup == 2:
    exit()
  
 

