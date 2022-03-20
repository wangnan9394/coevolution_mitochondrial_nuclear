import os
import argparse

parser = argparse.ArgumentParser(description = 'used for test chimera ORFs related to conserved genes in the intergenic region', add_help = False, \
    usage = '\npython 1.blastn.py -i [input.vcf]  <optinal:  >')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-orf', '--orf_fa', metavar = 'orf.fa file', help = 'orf.fa file', required = True)
required.add_argument('-bp30', '--bp30', metavar = '30bp-short segemnets', help = '30bp-short segemnets', required = True)
required.add_argument('-genome', '--genome', metavar = 'genome fa', help = 'genome fa', required = True)
required.add_argument('-conserved', '--conserved', metavar = 'conserved.fa', help = 'conserved.fa', required = True)
required.add_argument('-sample', '--sample_name', metavar = 'sample name', help = 'sample name', required = True)
#required.add_argument('-o', '--output', metavar = '[output.txt]', help = '输出转化完成的txt文件', required = True)
#required.add_argument('-r', '--region', metavar = '[region]', help = '范围值 Mb', default='2',type=int)

args = parser.parse_args()

orf_FA=args.orf_fa#'Ma.G1.scaffolds.line.orf.fa'
bp30_FA=args.bp30#'split-to-includingfragemnet-30bp.fa'
genome_FA=args.genome#'Ma.G1.circular.line.fa'
conserved_FA=args.conserved#'G1genefragment.fa'
sample_n=args.sample_name#'G1'

CMD_pre1='makeblastdb -in {} -dbtype nucl -title {}'.format(orf_FA,orf_FA)
CMD_pre2='makeblastdb -in {} -dbtype nucl -title {}'.format(genome_FA,genome_FA)
CMD_pre3='blastn -db {} -query {} -out SMQ-jieguo.txt -evalue 0.00001 -max_target_seqs 5 -outfmt 6'.format(orf_FA,bp30_FA)
os.system(CMD_pre1)
os.system(CMD_pre2)
os.system(CMD_pre3)

rongyu=[]
with open("SMQ-jieguo.txt",'r') as f:
    for line in f:
        line=line.split('\t')
        a=line[0]
        a=a.split('-')[0]
        b=line[1]
        input=a+'-'+b
        rongyu.append(input)
list2=list(set(rongyu))
#print(len(list2))

FA=orf_FA
seq_A={}
with open(FA,'r') as fd:
    for line in fd:
        if line.startswith('>'):
            name=line.replace(">",'').split()[0]
            #print(name)
            seq_A[name]=''
        else:
            seq_A[name]+=line.replace("\n",'').strip()
#print(seq_A[one])
FB=conserved_FA
seq_B={}
with open(FB,'r') as fd:
    for line in fd:
        if line.startswith('>'):
            name=line.replace(">",'').split()[0]
            #print(name)
            seq_B[name]=''
        else:
            seq_B[name]+=line.replace("\n",'').strip()
#print(seq_B[two])

FC=orf_FA
seq_C={}
list_pos=[]
with open(FC,'r') as fd:
    for line in fd:
        if line.startswith('>'):
            name_pos=line.replace("\n",'').replace(">",'')
            list_pos.append(name_pos)
#print(list_pos)

new_file=sample_n+'.results'
CMD_tmp0='rm {}'.format(new_file)
os.system(CMD_tmp0)
for i in list2:
    print(len(list2))
    out_A=open('A.fa','w')
    out_B=open('B.fa','w')
    one=i.split('-')[1]
    two=i.split('-')[0]
    #print(one,two)
    target=''
    for each in list_pos:
        if one == each.split()[0]:
            target=each
    name_sample='***************************TEST:'+one+'-'+two+'*****************'+target
    print(name_sample)
    header_A='>'+one+'\n'
    out_A.write(header_A)
    out_A.write(seq_A[one])
    len_A=len(seq_A[one])
    out_A.close()
    
    header_B='>'+two+'\n'
    out_B.write(header_B)
    out_B.write(seq_B[two])
    len_B=len(seq_B[two])
    out_B.close()
    name_sample=name_sample+'ORF_len:'+str(len_A)+','+'GENE_len:'+str(len_B)
    CMD1='blastn -db {} -task blastn-short -word_size 7 -query A.fa -out A.txt -evalue 0.00001 -max_target_seqs 5 -outfmt 6'.format(genome_FA)
    CMD2='blastn -db {} -task blastn-short -word_size 7 -query B.fa -out B.txt -evalue 0.00001 -max_target_seqs 5 -outfmt 6'.format(genome_FA)
    os.system(CMD1)
    os.system(CMD2)
    CMD_tmp='echo {} >>{}'.format(name_sample,new_file)
    os.system(CMD_tmp)
    CMD3='cat A.txt >>{}'.format(new_file)
    CMD4='cat B.txt >>{}'.format(new_file)
    os.system(CMD3)
    #print(CMD1,CMD2,CMD3,CMD4)
    os.system(CMD4)
    #break

