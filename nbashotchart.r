install.packages("BasketballAnalyzeR")

library(BasketballAnalyzeR)
PbP <- PbPmanipulation(PbP.BDB)
subdata <- subset(PbP, player=="Kevin Durant")
subdata$xx <- subdata$original_x/10
subdata$yy <- subdata$original_y/10-41.75

shotchart(data=subdata, x="xx", y="yy", scatter = T,
          pt.col = 'green',
          bg.col = 'white')

shotchart(data=subdata, x="xx", y="yy", scatter = T,
          z = 'result',
          bg.col = 'black',
          courtline.col = 'white',
          palette = 'hot')

shotchart(data=subdata, x="xx", y="yy", scatter = T,
          num.sect = 5,
          type = 'sectors',
          z = 'playlength')

shotchart(data=subdata, x="xx", y="yy", scatter = F,
          num.sect = 5,
          type = 'sectors',
          z = 'playlength',
          result = 'result')
