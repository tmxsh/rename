import os

s = os.listdir(os.getcwd())

def rename(path):
    dir = os.listdir(path)
    for filename in dir:
        if os.path.isdir(path + "\\" + filename):
            rename(path + "\\" + filename)
        else:
            if filename.find(" ") != -1:
                index = filename.find(" ")
                newName = filename[:index] + "_" + filename[index+1:]
                while(newName.find(" ") != -1):
                    index = newName.find(" ")
                    newName = newName[:index] + "_" + newName[index+1:]
                
                os.rename(path + "\\" + filename, path + "\\" + newName)

        
rename(os.getcwd())