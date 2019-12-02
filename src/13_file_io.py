"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
import os

with open(f"{os.getcwd()}/src/foo.txt") as f:
    read_data = f.read()
    print(read_data)

f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open(f"{os.getcwd()}/src/bar.txt", "w+") as f:
    f.write("This is line 1\n")
    f.write("This is line 2\n")
    f.write("This is line 3\n")
f.close()

with open(f"{os.getcwd()}/src/bar.txt") as f:
    read_data = f.read()
    print(read_data)

f.close()