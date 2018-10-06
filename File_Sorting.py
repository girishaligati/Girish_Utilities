#Program for sorting the files based on the File Modified Time 
    #Update 1 : Only Windows files 
import os
from datetime import datetime as dt
import shutil as sh

print("Current working directory is " + os.getcwd())
print("Paste the folder path that has to be sorted")
abs_path=input()
print("Enter the destination path where the sorted files have to moved")
dest_path=input()
for dir,dirs,files in os.walk(abs_path):
    os.chdir(dir)
    if (dir.__contains__('git') or dir.__contains__('.')):
        pass
    else:
        for i in range(len(files)):
            mod_time = os.stat(files[i]).st_mtime
            str_mkdir = dt.fromtimestamp(mod_time).strftime('%B %Y')
            if(str_mkdir in os.listdir(dest_path)):
                print("Copying "+files[i]+" now into the folder " + str_mkdir )
                sh.copy(files[i],dest_path+'\\'+str_mkdir)
            else:
                print("Directory doesn't exist, creating now")
                os.mkdir(dest_path+'\\'+str_mkdir) 
                sh.copy(files[i],dest_path+'\\'+str_mkdir)