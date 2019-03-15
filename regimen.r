library(ggplot2)
library(plotly)
library(ggridges)

load("regimen.RData")


cycles=NULL
for(i in 1:length(result)){
    if(length(grep("number",names(result[[i]])))==0){
        print(result[[i]])
    }
    else{
        cycles=c(cycles,length(grep("number",names(result[[i]]))))
    }
}

table(cycles)

