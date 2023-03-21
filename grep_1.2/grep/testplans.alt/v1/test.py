#!/usr/bin/env python3
#This code adds the interpreter path to the file. 
#So we don't have to mannualy use /bin/python3 to execute the file#

content="mkdir outputs;"
allLines=[]
with open('/home/towel/桌面/grep_1.2/grep/testplans.alt/v1/v0.cov.universe', 'r') as f:
    row=0
    # for line in f:
    #     last_line=line
    #     print(line)
    #     i+=1
    for line in f.readlines():
        # print(repr(line))
        # print(repr(line.strip()))
        # print(line)
        allLines.append(line)
        row+=1
        line=line.replace("../inputs","../../../inputs")
        line=line.replace("-P "," ")  # remove "-P "
        line=line.replace("]\n"," ")
        line=line.replace(" ["," ")
        line=line.replace("] "," ")
        
        line=line.replace("\\","\\\\")   #shell: \\ => \
        # line=line.replace("\n","")   #remove enter
        # line=line[1:-1]  #remove [ ]
        line="./grep.exe "+line  #add instruction ./grep.exe
        line=line+" > ./outputs/t"+str(row)+";"   # add output path
        content+=line
        print(line)
        
    print(row)

with open("handleOnce.sh","w") as f:
    f.write(content+"gcov -b grep.c;")
    
    