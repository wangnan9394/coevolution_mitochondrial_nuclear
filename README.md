# co-evolution_mitochondrial_nuclear-

coverage_depth_stats.py--python script for catch the coverages in target regions.
align_the_circle_genome_by_identical_seeds.py--mitogenome as a circle genome if necessary to align with a same start seqs(position).

Circos_plot:
conf file, a input file for circos software;
pi.txt, a genetic diversity cacultaed based on 184 samples;
SNP.distribution, a density of SNP in mitogenome based on 184 samples.

MT_haplotype_NU_LD_blocks:
GWAS_GEMMA.worksteps, the workflow to perform GWAS base on nuclear LD blocks and mitogenome haplotypes
GO_10kb_region_for_selected_genes_and_anno.py--python script for grep candidate genes surround the siginificant SNPs(10kb region);
GO-analysis-out.xlsx, the result of GO analysis.

RNA_seqs_analysis_in_replacement_samples:
All_mitgenome_G1_G1+HB_HB_TPMvalues.txt, the result of TPM values in mitogenome(based on RNA anno(100 bp steped windows));
Conserved_genes_G1_G1+HB_HB_TPMvalues.txt, the 100 bp steped windows related to conserved genes or fragements;
G1.anno.100.SAF, the predicted gene structure(100 bp steped windows); 
make-SAF.py--python script to make a SAF file for featureCount.

chimera-orfs-detected:
test_chimeraORFs_in_intergenic_region.py--python script detect the chimera ORFs related to conserved genes or fragments in intergenic regions of mitogenome;
split_conservaedgenes_to_30bp.py--python script to split conserved genes or fragments into 30 bp short seqs;
Folders:the 14 assembles and chimera resutls.

genetic_load_results:
genetic_load_based_on_pops.txt, the genetic load estimated in 184 samples,'At'(atalantia) as a outgroup (ancestry sequences).

paternla_leaksge_heteroplasmy:
lemon_paternal_leakage.xlsx, the result of heteroplasmy mediated by paternal leakage in sour_orange and grapefruit populations;
sour_orange(subgroup1 and subgroup2)_paternal_leakage.xlsx, the result of heteroplasmy mediated by paternal leakage in sour_orange and grapefruit populations.

The other population genomic tools, workflows and scripts could be find in wangnan9394/apomixis_parallel_evolution and wangnan9394/conservation_genomics
