
import gseapy


### global conditions

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/genes_PvsCsubstracted_GSEA.txt",description='PvsC',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1_3_5.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/genes_PDONvsPsubstracted_GSEA.txt",description='DONvsPDON',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1_3_5.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/genes_CDONvsCsubstracted_GSEA.txt",description='CDONvsC',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1_3_5.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/genes_PDONvsPsubstracted_GSEA.txt",description='PDONvsP',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1_3_5.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)


gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/genes_PvsCsubstracted_GSEA.txt",description='PvsC',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/genes_PDONvsPsubstracted_GSEA.txt",description='DONvsPDON',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/genes_CDONvsCsubstracted_GSEA.txt",description='CDONvsC',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/genes_PDONvsPsubstracted_GSEA.txt",description='PDONvsP',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)


## unique to a comparison

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/C_P_only.txt",description='PvsC_2',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1_3_5.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/CDON_PDON_only.txt",description='DONvsPDON_2',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1_3_5.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/CDON_C_only.txt",description='CDONvsC_2',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1_3_5.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/PDON_P_only.txt",description='PDONvsP_2',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1_3_5.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)



## unique to a comparison (all kegg)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/C_P_only.txt",description='PvsC',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/CDON_PDON_only.txt",description='DONvsPDON',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/CDON_C_only.txt",description='CDONvsC',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/PDON_P_only.txt",description='PDONvsP',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

## overlap C vs CDON

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA/U1_c_cdon.txt",description='U1_C_CDON',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA/U1_c_cdon_only.txt",description='U1_C_CDON_only',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA/U1_c_cdon_substracted.txt",description='U1_C_CDON_substracted',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)


## cdon / pdon / p - background

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA/pdon_substracted.txt",description='PDON_substracted',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)


gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA/cdon_substracted.txt",description='CDON_substracted',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)


gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA/p_substracted.txt",description='P_substracted',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)


## models 1, 2, 4
gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA/Model_4_U1CDON-C_substracted.txt",description='model_4',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA/Model_2_U1CDON-C.txt",description='model_2',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA/Model_1_U1CDON-C.txt",description='model_1',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA',cutoff=0.5, verbose=True, background = 7951)




/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/m1_PDON-Pros.txt

/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/m3_U1_CDON-Ctrl.txt
/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/m3_U1_PDON-CDON.txt
/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/m3_U1_PDON-Pros.txt
/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/m3_U1_Pros-Ctrl.txt

## model 1 U397

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/m1_CDON-Ctrl.txt",description='model_1_CDON_C',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/m1_PDON-CDON.txt",description='model_1_PDON-CDON',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/m1_PDON-Pros.txt",description='model_1_PDON-P',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/m1_Pros-Ctrl.txt",description='model_1_Pros-Ctrl',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models',cutoff=0.5, verbose=True, background = 7951)



## model 3 U1

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/m3_U1_CDON-Ctrl.txt",description='model_3_CDON_C',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/m3_U1_PDON-CDON.txt",description='model_3_PDON-CDON',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/m3_U1_PDON-Pros.txt",description='model_3_PDON-P',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/m3_U1_Pros-Ctrl.txt",description='model_3_Pros-Ctrl',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models',cutoff=0.5, verbose=True, background = 7951)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/U1_U9_model_3.txt",description='model_3_U1_U9',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models',cutoff=0.5, verbose=True, background = 6322)


gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models/U1_U9_model_3.txt",description='model_3_U1_U9_whole_KEGG',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models',cutoff=0.5, verbose=True, background = 6322)



## model 4 Ctrl (U1 vs U937)

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/DGE/Model_4_U1_U937.txt",description='model_4',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models',cutoff=0.5, verbose=True, background = 7951)


## jlat vs Jurkat

gseapy.enrichr(gene_list="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/GSEA_LT.txt",description='LT',gene_sets="/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/processing/KEGG_1.gmt",outdir='/home/flomik/Desktop/Code-PHD/Proteomics_Cameroon_India/results/GSEA_models',cutoff=0.5, verbose=True, background = 7951)


