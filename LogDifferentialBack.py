class LogDifferential:
    def __init__(self):
        pass
    
    def LogDif(df,col):
        import pandas as pd
        import numpy as np
        
        dfLog=df.iloc[:,col:].replace(0,1e-10).apply(np.log)
        dfLogDif=dfLog.diff().dropna()
        return dfLog, dfLogDif

    def DFbackLogDif(dfLog, dfLogDif):
        import pandas as pd
        import numpy as np
        
        dfBack=pd.concat([pd.DataFrame(dfLog.iloc[0,:]).T,pd.DataFrame(dfLogDif)], axis=0).cumsum().apply(np.exp)
        return dfBack

    def SRbackLogDif(srLog, srLogDif):
        # srLog   = initial value before LOG. Pass a series and the first one to be defined.
        # sfLogDif= predicted value in Log-Differential
        import pandas as pd
        import numpy as np
        
        dfBack=pd.DataFrame(np.append(srLog[0],srLogDif),columns=['yhat']).cumsum().apply(np.exp)
        return dfBack