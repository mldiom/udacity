import os
def rename_thatfile():
    
    current_d = os.getcwd()
    print("currently in " + current_d)
    os.chdir("Users/user/Downloads/prank")
    print("now in" + current_d)

    for file_name in file_list:
        os.rename(file_name("rochester.jpg"),"worcerter.jpg")

#rename_thatfile()
