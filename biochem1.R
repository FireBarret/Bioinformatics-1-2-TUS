# Data input 
   Data.df <- read.csv("/cloud/project/file3.csv")          
   colnames(Data.df) <- c("conc","rate")

# Selection of equation 
# 1: Michaelis Menten  2: Hill  3: substrate inhibition
SeleEqu0 <- 1     # Please write a number shown above the line   
   
# Initial parameters (初期値の設定)
   Kminit   <- 5         # 5     
   Vmaxinit <- 10        # 10
   nHinit   <- 2         # 2
   Kiinit   <- 1         # 1    

# Draw plots
   plot(Data.df$conc,Data.df$rate, 
        xlim = c(0,max(Data.df$conc)),  # range of x-axis
        ylim = c(0,max(Data.df$rate)),  # range of y-axis
        xlab = "Substrate (mM)",            # title of x-axis
        ylab = "Specific activity (U/mg)",  # title of y-axis
        main = "Kinetics plot",             # title of graph
        las      = 1,     # direction of scales 目盛の向き
        pch      = 16,    # a color of plots
        cex.axis = 1.3,   # 軸目盛りの文字の大きさ
        cex.lab  = 1.3    # 軸タイトルの文字の大きさ
        )

# Draw fitting curve

if(SeleEqu0 == 1){
  MM.nls <- nls(rate ~ (Vmax * conc / (Km + conc)), 
                data  = Data.df, 
                start = list(Km   = Kminit, 
                             Vmax = Vmaxinit
                             )
                )

  Km   <- unname(coef(MM.nls)["Km"])
  Vmax <- unname(coef(MM.nls)["Vmax"])

  curve(Vmax*x/(Km+x), 0, max(Data.df$conc),
        add = TRUE,
        lty = 1,     # 線分の種類
        lwd = 1.5    # 線分の太さ
        )
  Summary <- summary(MM.nls)

  Result0 <- c(paste("Vmax = ",signif(Vmax,digits=3)," +- ",signif(summary(MM.nls)$parameters[2,2],digits=3)," (U/mg)", sep = ""),
               paste("Km   = ",signif(Km,digits=3)," +- ",signif(summary(MM.nls)$parameters[1,2],digits=3)," (mM)", sep = "")
               )
  dim(Result0) <- c(2,1)
}

if(SeleEqu0 == 2){
  Hill.nls <- nls(rate ~ (Vmax * (conc ^ nH) / ((conc ^ nH) + (Km ^ nH))), 
                  data  = Data.df, 
                  start = list(Km   = Kminit, 
                               Vmax = Vmaxinit,
                               nH   = nHinit
                               )
                  )
  Km <- unname(coef(Hill.nls)["Km"])
  Vmax <- unname(coef(Hill.nls)["Vmax"])
  nH <- unname(coef(Hill.nls)["nH"])
  curve(Vmax*(x ^ nH)/((x ^ nH)+(Km ^ nH)), 0, max(Data.df$conc),
        add = TRUE,
        lty = 1, 
        lwd = 1.5
        )
  Summary <- summary(Hill.nls)
  Result0 <- c(paste("Vmax = ",signif(Vmax,digits=3)," +- ",signif(summary(Hill.nls)$parameters[2,2],digits=3), " (U/mg)", sep =""),
               paste("Km   = ",signif(Km,digits=3)," +- ",signif(summary(Hill.nls)$parameters[1,2],digits=3), " (mM)", sep =""),
               paste("nH   = ",signif(nH,digits=3)," +- ",signif(summary(Hill.nls)$parameters[3,2],digits=3), sep ="")
               )
  dim(Result0) <- c(3,1)
}

if(SeleEqu0 == 3){
  Subinh.nls <- nls(rate ~ (Vmax * conc / (Km + (1+conc/Ki)*conc)), 
                    data  = Data.df,
                    start = list(Km   = Kminit, 
                                 Vmax = Vmaxinit, 
                                 Ki   = Kiinit
                                 )
                    )
  Km   <- unname(coef(Subinh.nls)["Km"])
  Vmax <- unname(coef(Subinh.nls)["Vmax"])
  Ki   <- unname(coef(Subinh.nls)["Ki"])
  curve(Vmax*x/(Km+(1+x/Ki)*x),0,max(Data.df$conc),
        add = TRUE,
        lty = 1, 
        lwd = 1.5
        )
  Summary <- summary(Subinh.nls)
  Result0 <- c(paste("Vmax = ",signif(Vmax,digits=3)," +- ",signif(summary(Subinh.nls)$parameters[2,2],digits=3)," (U/mg)", sep = ""),
               paste("Km   = ",signif(Km,digits=3)," +- ",signif(summary(Subinh.nls)$parameters[1,2],digits=3)," (mM)", sep = ""),
               paste("Ki   = ",signif(Ki,digits=3)," +- ",signif(summary(Subinh.nls)$parameters[3,2],digits=3)," (mM)", sep = "")
               )
  dim(Result0) <- c(3,1)
}


print(Result0)
print(Summary)



