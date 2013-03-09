raw <- read.csv('9850-01-JAN-1982_slev.csv', header=FALSE, skip=8, col.names=c('t', 'z', 'dummy'))
# arrange column 1 to be expressed in hours (since 1970-01-01T00:00:00)
hourly <- raw[,]
hourly[,1] <- as.numeric(as.POSIXct(hourly[,1]))/3600

