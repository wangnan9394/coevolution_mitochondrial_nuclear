from lib2to3.pgen2.pgen import generate_grammar


out=open('pan.mt.anno.100.SAF','w')
header='GeneID'+'\t'+'Chr'+'\t'+'Start'+'\t'+'End'+'\t'+'Strand'+'\n'
out.write(header)
with open("G1.fai.txt",'r') as fd:
    for line in fd:
        line=line.replace("\n",'').split('\t')
        chr=line[0]
        len=line[1]
        for i in range(52000):
            gene='gene'+'-'+chr+'-'+str(i)
            chr=chr
            start=100*i
            end=100*(i+1)
            if end >int(len):
                end=int(len)
                break
            ll=gene+'\t'+chr+'\t'+str(start)+'\t'+str(end)+'\t'+'+'+'\n'
            out.write(ll)