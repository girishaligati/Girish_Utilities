import datetime
import os
import re


class Modify_TS():
    def __init__(self, curr_ts_li):
        self.curr_ts_li = curr_ts_li

    def hasten(self,hasten_by):
        new_ts=[]
        for ts in self.curr_ts_li :
            ts_obj = datetime.datetime.strptime(ts,'%H:%M:%S,%f')
            new_ts.append(datetime.datetime.strftime(ts_obj + datetime.timedelta(seconds = hasten_by),'%H:%M:%S,%f'))
        return new_ts

    def delay(self,delay_by):
        new_ts=[]
        for ts in self.curr_ts_li :
            ts_obj = datetime.datetime.strptime(ts,'%H:%M:%S,%f')
            new_ts.append(datetime.datetime.strftime(ts_obj - datetime.timedelta(seconds = delay_by),'%H:%M:%S,%f'))
        return new_ts

    def printing(self):     #Test Method
        for li in self.curr_ts_li:
            print(li)
 
def writelist_to_file(read_list,write_list,file_str):
    print(type(read_list[0]))
    print(type(write_list[0]))
    for i in range(len(read_list)):
        file_str.replace(read_list[i],write_list[i])
        with open(abs_path_1,'w+') as fd_1:
            fd_1.write(file_str)
        #re.sub(read_list[i],write_list[i],file_str)
        # print(read_list[i], write_list[i])
    return file_str
    

if __name__ == "__main__":
    # abs_path=input("Provide the file with the absolute location ")
    abs_path=r"C:\8780076\Vagrant\sharedfolder\Projects\Girish_Utilities\Subtitle_Editor\Ghost_Ship_(2002).srt"
    time_list=[]
    with open(abs_path,'r+') as fd:
        file_str = fd.read()
        time_list = re.findall(r"\d{2}:\d{2}:\d{2},\d{3}",file_str)
        
    obj = Modify_TS(time_list)
    obj.printing() # Test print
    time_var = float(input("Hasten / Delay by (Ex - 1.5, 2.6,....):"))

    if(input("Enter any value to Hasten else they will be Delayed")):
        new_ts_obj = obj.hasten(time_var)
        print(new_ts_obj)
    else:
        new_ts_obj = obj.delay(time_var)

    abs_path_1 = r"C:\8780076\Vagrant\sharedfolder\Projects\Girish_Utilities\Subtitle_Editor\Ghost_Ship_(2002)_1.srt"

