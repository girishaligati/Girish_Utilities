#Program for sorting the files based on the files names that has dates in it of type : "IMG_20180522_115409,VID_20180706_172806"
    #Update 1 : Only Windows files, written for oneplus6 photo format
    #Update 2 : Adding code for exception handling when the file in dest already exists
    #Update 3 : Adding code for the Building GUI with TKinter - 
    #           Modifed -   Files will not be moved anymore they will be copied in destination directory
    #           Issue   -   Text box is not being updated in Real time --> Need to find the Solution???

import os
from datetime import datetime as dt
import shutil as sh
import tkinter as tk


########################### Functional code for Sorting the files #############################
def Sort_files():
    Output_log.insert('end',"Current working directory is " + os.getcwd() + '\n')
    abs_path=Wgt_Src_txt.get()
    Output_log.insert('end', abs_path + " is the folder path that will be sorted"+ '\n')
    dest_path=Wgt_Dest_txt.get()
    Output_log.insert('end',dest_path + " is the path where the sorted files will be copied"+ '\n')

    for dir,dirs,files in os.walk(abs_path):
        os.chdir(dir)
        if (dir.__contains__('git') or dir.__contains__('.')):
            pass
        else:
            for i in range(len(files)):
                date_str_from_file=files[i].split('_')
                str_mkdir=dt.strptime(date_str_from_file[1],'%Y%m%d').strftime('%m-%B %Y')
                if(str_mkdir in os.listdir(dest_path)):
                    Output_log.insert('end',"Copying "+files[i]+" now into the folder " + str_mkdir+ '\n')
                    try:
                        sh.copy2(files[i],os.path.join(dest_path,str_mkdir))
                    except Exception as e:
                        Output_log.insert('end',e + '\n')
                else:
                    Output_log.insert('end',str_mkdir + " Directory doesn't exist, creating now"+ '\n')
                    os.mkdir(os.path.join(dest_path,str_mkdir)) 
    Output_log.insert('end', '##### Sorted the files successfully #####')
###############################################################################################

########################### Below is the Code for creating the GUI  ###########################

sort_img_app=tk.Tk()
sort_img_app.title("Application for Sorting Images by Dates")

Top_Frame = tk.Frame(sort_img_app)
Bottom_Frame = tk.Frame(sort_img_app)

tk.Label(Top_Frame, text='Sort Images Application',font='Helvetica').grid(row=0,column=0)
tk.Label(Top_Frame, text=' - Designed by Girish',justify='right').grid(row=1,column=1)

tk.Label(Top_Frame, text='Source Path').grid(row=2,column = 0) 
Wgt_Src_txt = tk.Entry(Top_Frame,text='Source')

tk.Label(Top_Frame, text='Destination Path').grid(row=3,column = 0) 
Wgt_Dest_txt = tk.Entry(Top_Frame,text='Destination')

Wgt_Convert = tk.Button(Top_Frame,text='Convert',command=Sort_files)

tk.Label(Bottom_Frame,text="Log Display:",anchor='w',justify='left').grid(row=0,column=0)
# Output_log = tk.Text(master=Top_Frame)
Output_log=tk.Text(master=Bottom_Frame,height=20,width=100)
Output_log.grid(row=1,column=0)

Wgt_Src_txt.grid(row=2,column=1)
Wgt_Dest_txt.grid(row=3,column=1)
Wgt_Convert.grid(row=4,column=1)
# Output_log.grid()
 
Top_Frame.pack()
Bottom_Frame.pack()


tk.mainloop()
###############################################################################################