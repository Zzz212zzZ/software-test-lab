#!/bin/python3
#generate dif statistic
#format:  Bug epoch,Fail case num
import os
with open("dif_percentages.csv","w") as f:
    f.write("Bug epoch,Fail case num\n")




with open("dif_percentages.csv","a") as f_csv:
    for bugCnt in range(1,19):
        failNum=0
        for caseCnt in range(1,200):
            filename=f"./result/{bugCnt}/r{caseCnt}"
            if(os.path.getsize(filename)!=0):
                failNum+=1
                
        f_csv.write(f"{bugCnt},{failNum}\n")

        
        