# Filenames and Absolute/Relative File Paths

# files have a name and a path
# root folder is lowest. windows is C:\ mac & linux is /
# in a file path the folders and filename are separated by backslashes on windows and forward slashes on mac
# use os.path.join() function to combine folders with correct slash
# cwd is folder that any relative paths are relative to
# os.getcwd() will return current working dir
# os.chdir() will change cwd()
# abs paths begin with root folder relative do not
# the .folder represents this folder. the ..folder represents "the parent folder"
# os.path.abspath() returns an abs path form of the path passed to it
# os.path.isabs() returns True if the path passed to it is absolute
# os.path.relpath() returns the relative path beweteen two paths passed to it
# os.makedirs() can make folders
# os.path.getsize() returns a files size
# os.lisdir() returns a list of strings of filenames
# os.path.exists() returns True if filename passed to it exists
# os.path.isfile() and os.path.isdir() return True if they were passed a filename or file path.
