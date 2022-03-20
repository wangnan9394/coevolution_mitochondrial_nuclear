import vcf

import argparse

parser = argparse.ArgumentParser(description = 'For citrus', add_help = False, usage = '\npython3 -i [input vcf] -l [seed seqs]')
required = parser.add_argument_group()
optional = parser.add_argument_group()
required.add_argument('-i', '--input', metavar = '[input.beagle.vcf]', help = 'input.vcf', required = True)
required.add_argument('-s', '--seed', metavar = '[seed seqs]', help = 'seed seqs ATTGCT', required = True)
optional.add_argument('-h', '--help', action = 'help', help = 'help')

args = parser.parse_args()


count=[]
seq=''
seed=args.seed
vcf_reader = vcf.Reader(open(args.input,'r'))
for record in vcf_reader:
    a=len(record.REF)
    b=len(record.ALT[0])
    if a==1 and b==1:
        seq+=record.REF
        count.append(record.POS)
len_ref=len(seq)
dict=[]
for i in range(len_ref-len(seed)):
    pos_s=count[i]
    pos_e=count[i+len(seed)]
    target=str(pos_s)+'_'+str(pos_e)
    dict.append(seq[i:i+len(seed)])
    dict.append(target)
#print(dict)
for num,i in enumerate(dict):
    if i==seed:
        print(i,dict[num+1])