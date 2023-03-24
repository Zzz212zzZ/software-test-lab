#!/bin/python3
#generate dif statistic (perLine)
#format:  epoch_1,epoch_2 ... epoch_18 
# case_1:    1   ,   2  , ...    1      

import os
with open("dif_percentages_per.csv","w") as f:
    row=["epoch_"+str(bugCnt) for bugCnt in range(1,19)]
    rowStr=",".join(row)
    f.write(rowStr+"\n")

with open("dif_percentages_per.csv","a") as f_csv:
    for caseCnt in range(1,200):
        isFail=[]
        for bugCnt in range(1,19):
            filename=f"./result/{bugCnt}/r{caseCnt}"
            if(os.path.getsize(filename)==0):
                isFail.append("0")
            else:
                isFail.append("1")
        isFailStr=",".join(isFail)  
        f_csv.write(f"{bugCnt},{isFailStr}\n")
        