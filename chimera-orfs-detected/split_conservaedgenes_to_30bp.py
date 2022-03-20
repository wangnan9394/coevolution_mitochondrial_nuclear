out=open('split-to-30bp.fa','w')
seq={}
with open("MT-conserved.fa",'r') as fd:
    for line in fd:
        if line.startswith('>'):
            name=line.replace(">",'').split()[0]
            seq[name]=''
        else:
            seq[name]+=line.replace("\n",'').strip()
for key in seq:
    
    lens=len(seq[key])
    for i in range(20000):
        seq_catch=seq[key]
        start=i*15
        end=i*15+30
        a=seq_catch[start:end]
        a=a+'\n'
        ll_name='>'+key+'-part'+str(i)+'\n'
        #print(ll_name,a)
        out.write(ll_name)
        out.write(a)
        if 30*(i+1)>lens:
            break