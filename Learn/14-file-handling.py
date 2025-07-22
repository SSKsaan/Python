# terminal must be in the same directory as the file being opened in order to work

file = open("testFile.txt", "r") # "r" is for read mode
content = file.read() # read() returns the whole file
print(content if content else "File is Empty Before Writing")
file.close() # close the file to change file mode

file = open("testFile.txt", "w")  # "w" is for write mode
file.write("Wrote this file:") # write() overwrites the whole content of the file in "w" mode
file.close()

file = open("testFile.txt", "a") # "a" is for append mode
file.write("\nThis is an added line") # write() adds content to the file in "a" mode
file.close()

with open("testFile.txt", "rb") as file: # "rb" is for read in binary mode
    print(file.read()) # other modes also have "_b" versions
# with statement automatically handles file closing, even if error occurs

try: # exception/error handling
    with open("testFile.txt", "x") as file: # "x" is for exclusive creation
        print(file.read()) 
except FileExistsError: # throws error if file already exists in "x" modes
    print("\nFile already exists:\n--------------------")
finally: # will run whether there's an error or not
    with open("testFile.txt", "a+") as file: # "_+" modes are _ mode with read and write
        # w+ and a+ modes will create a new file if file doesn't exist, but r+ modes will throw an error
        file.write("\nThis is another added line")
        file.seek(0) # Move file pointer to beginning to read, needed to read in "w+"/"a+" modes
        print(file.read())
        file.truncate(0) # removes data from the current pointer (0 means beginning) to the end of the file