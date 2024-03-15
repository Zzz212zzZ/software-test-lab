#!/usr/bin/env python3
#This code adds the interpreter path to the file. 
#So we don't have to mannualy use /bin/python3 to execute the file#

content="\
    echo 'Lines executed,Branches executed,Taken at least once,Calls executed,' > cov_percentages.csv;\
    mkdir outputs;\
    for((i=1;i<=18;i++));do mkdir ./outputs/$i ;done;\
    sed '' FaultSeeds.h > FaultSeeds;\
    for((i=1;i<=18;i++));\
        do sed $i's#*##g' FaultSeeds > tmp;sed $i's#/##g' \
        tmp > FaultSeeds.h;gcc -fprofile-arcs -ftest-coverage -I. -o grep.exe grep.c;"

allLines=[]
with open('./grep_1.2/grep/testplans.alt/v1/v0.cov.universe', 'r') as f:
    row=0

    for line in f.readlines():
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
        line=line+" > ./outputs/$i/t"+str(row)+";"   # add output path
        content+=line
        # print(line)
        
    print(row)

with open("handle.sh","w") as f:
    f.write(content+\
        "gcov -b grep.c | grep -oE '[0-9]+\.[0-9]+%' | grep -v '0.00' | tr '\\n' ',' >> cov_percentages.csv; echo '' >> cov_percentages.csv;"\
        +"done;"+"sed '' FaultSeeds > FaultSeeds.h;")
    
    