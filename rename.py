import os
def rename_files():

    #get file name from folder
    file_list = os.listdir("/Users/user/Downloads/prank")
    #print(file_list)

    saved_path = os.getcwd()
    print ("Current working Directory is " +saved_path)
    os.chdir("/Users/user/Downloads/prank")
    
    #for each file, rename files
    for file_name in file_list:
       os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    
rename_files()
