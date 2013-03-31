boston=read.fwf('data/boston', widths=c(7,-1,8,-1,5,-1,7,-1,7),
  skip=7, col.names=c('id', 'd', 'h', 'pred', 'z'), sep='/')
t = as.numeric(as.POSIXct(strptime(paste(boston[,2], boston[,3]), '%Y%m%d %H:%M')))
# make it hourly.
boston$t = t / 3600

