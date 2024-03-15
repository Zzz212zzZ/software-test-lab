#!/usr/bin/env python3
with open('diffAll.sh','w') as f:
    #cover the history
    f.write('mkdir result;\n\
for((i=1;i<=18;i++));do mkdir ./result/$i ;done;\n')

with open('diffAll.sh', 'a') as f:
    for bugCnt in range(1,19):
        f.write(f"echo '---------------------diff bug{bugCnt}--------------------'\n")
        for caseCnt in range(1,200):
            f.write(f"echo 'diff case {caseCnt} in {bugCnt}' \n")
            f.write(f"diff ./outputs/t{caseCnt} ../../versions.seeded/v1/outputs/{bugCnt}/t{caseCnt} \
                >./result/{bugCnt}/r{caseCnt} \n")
    
    
content="mkdir result; \n\
    for((i=1;i<=18;i++));do mkdir ./result/$i ;done; \n"

