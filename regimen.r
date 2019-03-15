library(ggplot2)
library(plotly)
library(ggridges)

load("regimen.RData")
cycles=NULL
for(i in 1:length(result)){
    cycles=c(cycles,length(grep("number",names(result[[i]]))))
    
}
