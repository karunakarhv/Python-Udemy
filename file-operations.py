#yfile = open("filetest.txt")
#print(myfile.read())
#Problem with this file pointer would have moved to the end of file, 
#hence causing the next line to print blank.
#print(myfile.read())

#For the above problem we can use the below method
#To Print the contents of file as many times as we wish
""" content = myfile.read()
print(content)
print(content)
print(content) """

#print(myfile.read(10))

#After performing the file operations, its always a good practice
#To close a file, becuase the file handle will remain in RAM, instead of getting
#deleted.
#myfile.close()
#Any operations after the file handle will cause an I/O error.
#myfile.read()

#Another good practice is to use "WITH Content Manager" 
# in order for proper close of file automatically

with open("file-operations/filetest.txt") as myfile:
    content = myfile.read()

with open("file-operations/another-filetest.txt", "w") as write_handle:
    write_handle.write(content)

print(content)