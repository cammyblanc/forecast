class dfStockprice():
    def __init__(self):
        pass
    def execute(self,file):
        import os
        import pandas as pd
        import pandas_datareader.data as getStock

        dfStock=pd.read_csv(file)
        dfStock['str']='.JP'
        dfStock.id=dfStock.id.astype(str)
        dfStock['stock']=dfStock.id.str.cat(dfStock.str)

        lst  = ['AMZN.US'] 
        lst1=list(dfStock.stock)
        for i in lst1:
            lst.append(i)

        name = ['dt','amazon']
        name1=list(dfStock.name)
        for i in name1:
            name.append(i)
   
        dfStockprice = getStock.DataReader([str(c) for c in lst], 'stooq')        
        dfStockTable=pd.DataFrame()
        for i in lst:
            dfStockTable = pd.concat([dfStockTable, dfStockprice.Close[i]], axis=1).dropna()
        
        dfStockTable = dfStockTable.reset_index()
        dfStockTable.columns=name
        return dfStockTable
