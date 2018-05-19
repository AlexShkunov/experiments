
print('** Test script start **')

print('Simple arithmetics...')
2+5

print('arguments...')
args = commandArgs(trailingOnly=TRUE)

for (one in args){
  print(paste("Arg = ", one))
}

if (length(args)==0) {
  stop("Error, supply Datafile argument", call.=FALSE)
}

dat = read.csv(args[1], header = TRUE)
head(dat)
