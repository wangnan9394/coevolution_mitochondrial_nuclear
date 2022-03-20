out_filter=open("genes.filter.txt",'w')#10kb region for target genes
with open("Mini_citrus.gene.model.gff3","r") as f:
    for line1 in f:
        line=line1.replace("\n","").split('\t')
        chr=int(line[0][-1])
        gene=line[2]
        start=int(line[3])
        end=int(line[4])
        with open("location.txt","r") as fd:
            for each in fd:
                each=each.replace("\n","").split('\t')
                pos=int(each[2])
                chrom=int(each[0])
                if chrom==chr and pos+10000 >start and pos-10000<end and gene=='gene':
                    #rint(line1)
                    out_filter.write(line1)
out_filter.close()

oooo=open("functions.txt",'w')
with open("genes.filter.txt","r") as f:
    for line1 in f:
        line=line1.replace("\n","").split('\t')
        genes=(line[-1])[3:-1]
        with open("Mini_citrus_Function.annotation.xls",'r') as fd:
            for one1 in fd:
                one=one1.replace("\n",'').split('\t')
                id=one[0]
                if id==genes+'.1':
                    #print(one)
                    oooo.write(one1)
