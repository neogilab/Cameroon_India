#' Save figure as PDF in results
#'
#' @param figure variable containing figure
#' @param name name of the figure
#' @param height height of the figure
#' @param width width of the figure
save_figure <- function(figure, name, height, width){
  path_fig <- paste0("results/figures/", name_ana, "_", name,".pdf")
  dev.copy(pdf, path_fig, width = width, height = width)
}

#' Save figure as PDF in results
#'
#' @param ggplot variable containing figure
#' @param name name of the figure
#' @param height height of the figure
#' @param width width of the figure
save_ggplot <- function(name, height, width){
  path_fig <- paste0("results/figures/", name_ana, "_", name,".pdf")
  ggsave(path_fig, width = width, height = width)
  dev.off()
}

#' Save file as csv
#'
#' @param file variable containing file
#' @param name name of the file
#' @param destination destination folder for file
save_file_csv <- function(file, name, destination){
  path_file <- paste0(destination, name_ana, "_", name,".csv")
  print(path_file)
  write.csv(file, file = path_file)
}


#' Save file as txt
#'
#' @param file variable containing file
#' @param name name of the file
#' @param destination destination folder for file
save_file <- function(file, name, destination){
  path_file <- paste0(destination, name_ana, "_", name,".txt")
  print(path_file)
  write.table(file, file =path_file, sep = "\t", row.names = TRUE, 
              col.names = NA)
}

#' Save file as txt
#'
#' @param file variable containing file
#' @param name name of the file
#' @param destination destination folder for file
save_file_excel <- function(file, name, destination){
  path_file <- paste0(destination, name_ana, "_", name,".xlsx")
  print(path_file)
  write.xlsx(file, file =path_file)
}

#' Run Man withney test between 2 conditions
#'
#' @param file 
#' @param n_c1 number of samples in condition 1
#' @param n_c2 number of samples in condition 2
#' @param c1 name condition 1
#' @param c2 name condition 2
my_man_whithney <- function(data, n_c1, n_c2, c1, c2){
  test_table <- data.frame(Accession = NA, Log2FC = NA, pvalue = NA, FDR = NA, Significance = NA)
  metabolites <- rownames(data)
  n_c2_start <- n_c1 +1
  n_c2_stop <- n_c1 + n_c2
  print(n_c2_start)
  print(n_c2_stop)
  print(names(data)[1:n_c1])
  print(names(data)[n_c2_start:n_c2_stop])
  for (i in 1:nrow(data)){
    a <- as.matrix(data[i, 1:n_c1])
    b <- as.matrix(data[i, n_c2_start:n_c2_stop])
    ts <- wilcox.test(a, b)
    test_table[i, 3] <- ts$p.value
    test_table[i, 2] <- log2((sum(b)/n_c2)/(sum(a)/n_c1))
    test_table[i, 1] <- rownames(data)[i]
  }
  #
  rownames(test_table) <- metabolites
  test_table$FDR <- p.adjust(test_table$pvalue, method = "fdr")
  test_table$Significance <- ifelse(test_table$pvalue < 0.05, "SIGN", "NS")
  name <- paste0(c1, "_vs_", c2, "_Man_whitney_test_results")
  print(name)
  test_table <- test_table[complete.cases(test_table), ]
  save_file_excel(test_table, name, "results/India/Man_whithney/")
  save_file_csv(test_table, name, "results/India/Man_whithney/")
  test_table_2 <- test_table[test_table$FDR < 0.1, ]
  print(nrow(test_table_2))
  test_table_2$Significance <- ifelse(test_table_2$Log2FC < 0, paste0("downregulated in ", c2), paste0("upregulated in ", c2))
  name <- paste0(c1, "_vs_", c2, "_Man_whitney_test_results_filtered")
  save_file_csv(test_table_2, name, "results/India/Man_whithney/")
  save_file_excel(test_table_2, name, "results/India/Man_whithney/")
  return(test_table)
}

#' Print heatmap of genes differentially expressed
#'
#' @param r_norm dataframe containing proteim abundances of conditions to compare
#' @param DF_top_table_2 Filt DGE results table containing uniprot ID
#' @param name_ana name of analysis
#' @param comp comparison done
#' @param annotationInfo table containing uniprot accession and gene name
#' @param label_cutoff name FDR cutoff value
clustering_DGE <- function(subset, dge_table, name_ana, size, a, b, c1, c2){
  subset <- subset[rownames(subset) %in% dge_table$Accession, ]
  my_palette <- colorRampPalette(c("#336699","#6699cc","#b3cce6","white","#ff9999","#ff3333","#cc0000"))(n=25)
  path_fig <- paste0("results/figures/", name_ana, "_clustering.pdf")
  pdf(path_fig, width=9, height=size)
  heatmap.2(as.matrix(subset),
            scale="row",
            Rowv = TRUE, #dont order
            Colv = TRUE,
            trace="none",
            col = my_palette,
            keysize = 2,
            dendrogram = 'both',
            ColSideColors = c(rep(c1, a),rep(c2, b)), srtCol=45)
  dev.off()
}

#' Run T test between 2 conditions
#'
#' @param file 
#' @param n_c1 number of samples in condition 1
#' @param n_c2 number of samples in condition 2
#' @param c1 name condition 1
#' @param c2 name condition 2
my_t_test <- function(data, n_c1, n_c2, c1, c2, annotationInfo){
  test_table <- data.frame(Accession = NA, Log2FC = NA, pvalue = NA, FDR = NA, Significance = NA)
  n_c2_start <- n_c1 +1
  n_c2_stop <- n_c1 + n_c2
  print(n_c2_start)
  print(n_c2_stop)
  print(names(data)[1:n_c1])
  print(names(data)[n_c2_start:n_c2_stop])
  for (i in 1:nrow(data)){
    a <- as.matrix(data[i, 1:n_c1])
    b <- as.matrix(data[i, n_c2_start:n_c2_stop])
    ts <- t.test(a, b)
    test_table[i, 3] <- ts$p.value
    test_table[i, 2] <- log2((sum(b)/n_c2)/(sum(a)/n_c1))
    test_table[i, 1] <- rownames(data)[i]
  }
  test_table$FDR <- p.adjust(test_table$pvalue, method = "fdr")
  test_table$Significance <- ifelse(test_table$FDR < 0.1, "SIGN", "NS")
  name <- paste0(c1, "_vs_", c2, "_T_test_results")
  save_file_excel(test_table, name, "results/T-Test/")
  save_file_csv(test_table, name, "results/T-Test/")
  test_table <- test_table[test_table$FDR < 0.1, ]
  print(nrow(test_table))
  test_table$Significance <- ifelse(test_table$Log2FC < 0, paste0("downregulated in ", c2), paste0("upregulated in ", c2))
  name <- paste0(c1, "_vs_", c2, "_T_test_results_filtered")
  save_file_csv(test_table, name, "results/T-Test/")
  save_file_excel(test_table, name, "results/T-Test/")
  return(test_table)
}



