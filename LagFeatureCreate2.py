class dfTransform():
    def __init__(self):
        lags=12
        step=1
    
    def create_lag_features(y, step, lags):
        import numpy as np
        import pandas as pd
        from sklearn.preprocessing import StandardScaler
        from statsmodels.tsa.stattools import pacf
           
        scaler = StandardScaler()
        features = pd.DataFrame()
        
        partial = pd.Series(data=pacf(y, method='ywmle', nlags=lags))
        lstLags=list(zip(list(partial[np.abs(partial) >= 0.2].index), list(np.abs(partial[np.abs(partial) >= 0.2]))))
        dfList= pd.DataFrame(lstLags, columns=['idx','val'])
        dfList= dfList[dfList.idx>0].sort_values('val', ascending=False)
        lags  = list(dfList.idx.values)
        print(lags)
        
        lstLagIdx=list()

        for v in lags:
            if v-step>=0:
                lstLagIdx.append(v-step)
        
        if len(lstLagIdx)==0:
            lstLagIdx=[0]
        
        print(lstLagIdx)
        
        # lags = list(partial[np.abs(partial) >= 0.2].index)
        # avoid to insert the time series itself
        # lags.remove(0)
        
        df = pd.DataFrame()
            
        for l in lstLagIdx:
            df[f"lag_{l}"] = y.shift(l)
        
        features = pd.DataFrame(df[df.columns],
                                columns=df.columns)  # scaler.fit_transform(df[df.columns])
        features.index = y.index
        
        return features
    