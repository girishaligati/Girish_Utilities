import datetime
import os
import re

# Class implementation for Modifiying the subtitles file
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
    

#Begin of main program
if __name__ == "__main__":
    abs_path=input("Provide the srt file with the absolute location ")
    # abs_path=r"C:\8780076\Vagrant\sharedfolder\Projects\Girish_Utilities\Subtitle_Editor\Ghost_Ship_(2002).srt"
    outputfile = os.path.splitext(abs_path)[0] + '_output'+os.path.splitext(abs_path)[1]
    # abs_path_1 = r"C:\8780076\Vagrant\sharedfolder\Projects\Girish_Utilities\Subtitle_Editor\Ghost_Ship_(2002)_1.srt"
    time_list=[]
    new_ts_obj = []
    temp_val = int(input("1: Hasten 2: Delay : "))
    time_var = float(input("Hasten / Delay by (Ex - 1.5, 2.6,....): "))

    with open(abs_path,'r+') as fd:
        with open(outputfile+'','w+') as wfd:
            for line in fd:
                if (re.findall(r"\d{2}:\d{2}:\d{2},\d{3}",line)):
                    time_list = re.findall(r"\d{2}:\d{2}:\d{2},\d{3}",line)
                    obj = Modify_TS(time_list)
                    if(temp_val == 1):
                        new_ts_obj = obj.hasten(time_var)
                    elif(temp_val == 2):
                        new_ts_obj = obj.delay(time_var)
                    wfd.write(new_ts_obj[0]+' --> '+ new_ts_obj[1] + '\n')
                else:
                    wfd.write(line)
        print("File has been Hastened/Delayed successfully ")
