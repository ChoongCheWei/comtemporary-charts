library(plotrix)

revenue <- c(2.65, 1.42, 1.17, 0.45, 0.59, 0.84, 0.02, 0.36)
category <- c("Travel", "Fashion", "Electronic", "Food", "Appliances", "Toys & DIY", "Music
", "Games")

fan.plot(revenue, labels = category, radius = 0.8, label.radius = 1.2, max.span=2.9, main="Top Category chosen By Malaysian")


