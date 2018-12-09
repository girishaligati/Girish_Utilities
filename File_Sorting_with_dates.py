#Program for sorting the files based on the files names that has dates in it of type : "IMG_20180522_115409,VID_20180706_172806"
    #Update 1 : Only Windows files, written for oneplus6 photo format
    #Update 2 : Adding code for exception handling when the file in dest already exists
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
            date_str_from_file=files[i].split('_')
            str_mkdir=dt.strptime(date_str_from_file[1],'%Y%m%d').strftime('%m-%B %Y')
            if(str_mkdir in os.listdir(dest_path)):
                print("Copying "+files[i]+" now into the folder " + str_mkdir )
                try:
                    sh.move(files[i],dest_path+'\\'+str_mkdir)
                except Exception as e:
                    print(e)
            else:
                print("Directory doesn't exist, creating now")
                os.mkdir(dest_path+'\\'+str_mkdir) 