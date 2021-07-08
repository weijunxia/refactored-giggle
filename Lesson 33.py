# Deleting Files

# os.rmdir() deletes folders MUST BE EMPTY
# shutil.rmtree() removes entire folder and contents
# Dry Run: comment out unlink() function

# import os
# for filename in os.listdir():
#   if filename.endswith('.txt'):
#       os.unlink(filename)
#       print(filename)

# rmtree and unlink is risky
# import send2trash
# send2trash.send2trash() sends to recycling bin and not permanently deletes

# os.unlink() will delete a file
# os.rmdir() will delete a folder if it's empty
# shutil.rmtree() will delete a folder and all its contents
# deleting can be dangerous so dry run first
# send2trash.send2trash() will send a file or folder to the recycling bin

        
