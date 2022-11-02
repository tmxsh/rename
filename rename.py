import os

def rename(path):
    #print(path)
    dir = os.listdir(path)
    whack = ""
    for filename in dir:
        if os.name == "nt":
            test = path + "\\" + filename
            whack = "\\"
        else:
            test = path + "/" + filename
            whack = "/"
            
        if os.path.isdir(test):
            rename(test)
        else:
            if filename.find(" ") != -1:
                index = filename.find(" ")
                newName = filename[:index] + "_" + filename[index+1:]
                while(newName.find(" ") != -1):
                    index = newName.find(" ")
                    newName = newName[:index] + "_" + newName[index+1:]
                
                os.rename(test, path + whack + newName)

        
rename(os.getcwd())