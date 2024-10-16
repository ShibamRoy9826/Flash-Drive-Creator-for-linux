import os

print("Type 'help' for help and 'exit'")
input("Please insert pendrive and press enter.")

x = input(">>")

if x == "help":
    print("")
else:
    os.system(command= x)