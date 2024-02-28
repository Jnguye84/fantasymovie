library(tidyverse)
library(dplyr)
library(igraph) 
library(reticulate)
setwd("C:/Users/Owner/Documents/GitHub/fantasymovie/Predict-Movie-Box-Office-Success")
df <- read_csv('pca_df_new.csv') #upload csv
df_actors <- df[1:990,1:990] #33 rows, 33 columns starting at the first actor
set.seed(1)

#graph
graph <- graph_from_adjacency_matrix(as.matrix(df_actors), mode = "undirected", weighted = NULL)

# Set actor names as vertex names
V(graph)$name <- names(df_actors)

# Calculate betweenness centrality
betweenness_values <- betweenness(graph)

betweenness_values <- betweenness_values[order(-betweenness_values)]

betweenness_dict <- setNames(as.list(betweenness_values), names(betweenness_values))#make dictionary
