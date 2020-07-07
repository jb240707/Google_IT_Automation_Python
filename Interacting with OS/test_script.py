"""
The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared by the 'comments' variable, and returns the size of the new file. Fill in the gaps to create a script called "program.py".
"""


import datetime
import os


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)
        filesize = len(comments)
    return(filesize)


print(create_python_script("program.py"))


"""
The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms". 
"""


def new_directory(directory, filename):
    if not os.path.exists(directory):
        os.mkdir(directory)
    os.chdir(directory)
    with open(filename, 'w') as f:
        pass
    return(os.listdir())


print(new_directory("PythonPrograms", "script.py"))


"""
The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.
"""


def file_date(filename):
    # Create the file in the current directory
    with open(filename, "w") as file:
        pass
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    new_date = datetime.datetime.fromtimestamp(timestamp)
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return ("{}".format(new_date.date()))


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd


"""
The parent_directory function returns the name of the directory that's located just above the current working directory. Remember that '..' is a relative path alias that means "go up to the parent directory". Fill in the gaps to complete this function.
"""


def file_date(filename):
    # Create the file in the current directory
    with open(filename, 'w') as file:
        pass
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    curr_time = datetime.datetime.fromtimestamp(timestamp)
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return ("{}".format(curr_time.strftime("%Y-%m-%d")))


print(file_date("newfile.txt"))
# Shojuld be today's date in the format of yyyy-mm-ddcddd
