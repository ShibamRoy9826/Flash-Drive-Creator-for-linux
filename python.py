#!/usr/bin/python
import os

print("Type 'help' for help and 'exit'")
firstin = input("Type 'help' for help. Press enter to see the available drives and continue with the installation.")

if firstin == "help":
    print("this is help")
else:
    os.system(command= "lsblk")

#collecting data
drive = input("Please type in the name of the Drive you want to flash: ")
iso = input("Please enter the path to your iso file: ")
verif = input("All data on your drive will be lost. Do you want to continue?[Y/n]: ")

if verif == "Y":

    # Step 1:
    # Unmount drive
    os.system(command="sudo umount "+ drive)

    # Step 2:
    # Create the Bootable USB

    #print("sudo dd if=" + iso + " of="+ drive +" bs=4M status=progress")

    os.system(command="sudo dd if=" + iso + " of=/dev/sdX bs=4M status=progress")

    # Step 4:
    # Sync and eject
    os.system(command="sudo sync")

else:
    print("...................TASK ABORTED.....................")