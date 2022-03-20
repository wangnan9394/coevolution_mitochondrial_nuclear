#group=["Ma21CI0","Ma21CI1","Ma21CI2","N18BUD","N18COR","N18HUM","N18VEU","citron_JY28","citron_JY4","citron_JY5","citron_XZ","citron_XZ1","N18LIM","N18LMA","N18RRL","lemon_05L-06","lemon_BJ","lemon_JY22","lemon_LS","lemon_ML","JinLanYou","pummelo_10Z","pummelo_28H","pummelo_AJH","pummelo_CQ-016","pummelo_GXY","pummelo_GY-1","pummelo_HB","pummelo_HHSWY","pummelo_NJYPS","pummelo_Q-04","pummelo_RL-06","pummelo_SMST","pummelo_SR3-2","pummelo_STY","pummelo_WSY","pummelo_YNMD","pummelo_YNSJ","JSYA"]
import pandas as pd
import numpy as np
group=["Ma21CI0","Ma21CI1","N18VEU","citron_JY28","citron_JY4","citron_JY5","citron_XZ","citron_XZ1","N18LIM","lemon_05L-06","lemon_BJ","lemon_JY22","lemon_LS","lemon_ML","JinLanYou","pummelo_10Z","pummelo_28H","pummelo_AJH","pummelo_CQ-016","pummelo_GXY","pummelo_GY-1"]

#def samplot(group,start,end):
start=95000
end=95003
list=[]

row=[]
for i in range(start+1,end):
    row.append(i)
list.append(row)

for num,i in enumerate(group):
    outfile=open("bamplot"+str(num+1)+".txt",'w')
    with open(str(i)+".depth",'r') as f:
        sample=[]
        for i in f:
            i=i.replace("\n","").replace(" ","").split("\t")
            pos=int(i[1])
            coverage=int(i[2])
            if pos>start and pos<end:
                sample.append(coverage)
                ll=str(pos)+'\t'+str(coverage)+'\n'
                outfile.write(ll)

#def merge_stat():
    #out_file=open("locus1.txt",'w')
    #for site in range(start,end):
    #    s=str(site)+'\t'
    #    for num,i in enumerate(group):
    #        with open(str(i)+".depth",'r') as f:
    #            for i in f:
    #                i=i.replace("\n","").replace(" ","").split("\t")
     #               pos=int(i[1])
     #               coverage=int(i[2])
     #               if pos==site:
      #                  s+=str(coverage)+'\t'
      #                  break
     #   s=s[:-1]+'\n'
     #   out_file.write(s)
    #print(s)
