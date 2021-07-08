# Walking a Directory Tree

# import os
import os

for folderName, subfolders, filenames in os.walk('/Users/weijunxia/Documents/python2'):
	print('The folder is ' + folderName + ' are: ' + str(subfolders))
	print('The subfolders in ' + folderName + ' are: ' + str(filenames))

	for subfolder in subfolders:
            if 'fish' in subfolder:
                os.rmdir(subfolder)
                
        for file in filenames:
            if file.endswith('.py'):
                shutil.copy(os.join(folderName, file), (os.join(folderName, file + 'backup'),
