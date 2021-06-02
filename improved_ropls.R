## improved ropls 


#' Produce publication-quality ggplot images of ropls objects.
#'
#' `ropls.plot`` produces publication-quality ggplot images of ropls objects.
#' The functions automatically determines the model type ("PCA", "PLS", "OPLS","PLS-DA","OPLS-DA") from the ropls object.
#' The components shown in the plot are flexible and determined by the xvar and yvar parameters.
#'
#' @param d ropls object created by [opls()].
#' @param plottype Which type of plot to produce. Options include scores (default), loadings and metrics.
#' @param xvar which component to plot on the x-axis. Must refer to a single component ("p1") or orthogonal ("o1") component present in the supplied ropls object.
#' @param yvar which component to plot on the y-axis. Must refer to a single component ("p1") or orthogonal ("o1") component present in the supplied ropls object.
#' @param hotelling If set to TRUE, will add Hotelling's T2 ellipse to the plot.
#' @param ellipse If set to TRUE, will add an ellipse around the groups supplied in the model. Does not work for PCA, PLS and OPLS models.
#' @param col.var Vector of categorical or numerical values used to colour the variables of the loading plot.
#'
#' @return A ggplot object of the specified type.
#'   }
#'
#' @import dplyr
#' @import ggplot2
#'
#' @export
ropls.plot <- function(d, plottype = "score", xvar, yvar, hotelling = FALSE, ellipse = FALSE, col.var = NULL, col.pca = NULL){
  N <- nrow(d@scoreMN)
  sm <- d@modelDF
  y <- d@suppLs$yMCN
  print(y)
  hotFisN <- (N - 1) * 2 * (N^2 - 1) / (N^2 * (N - 2)) * qf(0.95, 2, N - 2)
  
  #Define scores
  if(length(d@orthoScoreMN) == length(d@scoreMN)){
    score = data.frame(d@scoreMN, d@orthoScoreMN)}
  else{score = data.frame(d@scoreMN)}
  #Define loadings
  if(length(d@orthoLoadingMN) == length(d@loadingMN)){
    loading = data.frame(d@loadingMN, d@orthoLoadingMN)}
  else{loading = data.frame(d@loadingMN)}
  
  #plotting scores
  if(plottype == "score"){
    if(d@typeC == "PCA"){p <- ggplot(score, aes_string(x = xvar, y = yvar, col = col.pca)) + geom_point(size = 2)}
    
    else{p <- ggplot(score, aes_string(x = xvar, y = yvar, col = "y")) + geom_point(size = 8, alpha = 0.9, shape = 21, color = "black", aes(fill = factor(y))) + 
      scale_color_manual(name = "Condition", values = c(c_border_CM_ART,c_border_CM_HC,c_border_CM_VP, c_IN_ART, c_IN_HC, c_IN_VP)) + 
      scale_fill_manual(name = "Condition", values=c(c_CM_ART,c_CM_HC,c_CM_VP, c_IN_ART, c_IN_HC, c_IN_VP))}
    
    p <- p + xlab(paste(xvar,":", sm[xvar, "R2X"] * 100, "%")) + ylab(paste(yvar,":", sm[yvar, "R2X"] * 100, "%"))
    p <- p + theme(
      legend.position = "none",
      legend.justification = c("right", "bottom"),
      legend.box.just = "right",
      legend.margin = margin(6, 6, 6, 6)
    )
    
    if(hotelling){
      p <- p + gg_circle(
        rx = sqrt(as.numeric(var(score %>% select(xvar))) * hotFisN),
        ry = sqrt(as.numeric(var(score %>% select(yvar))) * hotFisN),
        xc = 0, yc = 0)}
    
    if (ellipse) {
      p <- p + stat_ellipse(linetype = 2, type = "norm")}
  }
  #plotting loadings
  if(plottype == "loading"){
    p <- ggplot(loading, aes_string(x = xvar, y = yvar, col = col.var)) + geom_point(size = 2)
    p <- p + xlab(paste(xvar,":", sm[xvar, "R2X"] * 100, "%")) + ylab(paste(yvar,":", sm[yvar, "R2X"] * 100, "%"))
    p <- p + geom_hline(yintercept = 0, color = "gray") + geom_vline(xintercept = 0, color = "gray")
  }
  
  return(p)
}



# Function to plot a circle in ggplot
# Adapted from https://github.com/tyrannomark/bldR/blob/master/R/L2017.R
# GPL-3 license
#' Function to add circles and ellipses to ggplot images.
#'
#' `gg_circle`` produces circles and ellipses that can be added to ggplot images.
#'
#' @param rx parameter.
#' @param ry parameter.
#' @param xc parameter.
#' @param yc parameter.
#' @param color parameter.
#' @param fill parameter.
#'
#' @return a circle.
#'   }
gg_circle <- function(rx, ry, xc, yc, color="black", fill=NA, ...) {
  x <- xc + rx*cos(seq(0, pi, length.out=100))
  ymax <- yc + ry*sin(seq(0, pi, length.out=100))
  ymin <- yc + ry*sin(seq(0, -pi, length.out=100))
  annotate("ribbon", x=x, ymin=ymin, ymax=ymax, color=color, fill=fill, ...)
}