# Reading and Writing Plaintext Files

# shelfFiles are very similar to dictionaries
# open() will return a file object which has reading and writing related methods
# Pass 'r' (or nothing) to open() to open the file in read mode. 'w' write mode, 'a' append mode
# opening a nonexistent filename in write or append mode will create the file
# call read() or write() to read the contents of a file or write a string to a file.
# call readlines() to return a list of strings of the file's content
# call close() when you are done with the file
# the shelve mod can store python values in a binary file
# shelve.open() returns a dictionary-like shelf value

