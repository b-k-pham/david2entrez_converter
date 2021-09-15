import pandas as pd
import numpy as np
import os

def Gene2Entrez_Dict():
    fpath = os.path.dirname(os.path.abspath(__file__)) + '/ENTREZ_GENE_ID2DAVID_GENE_NAME.txt'
    DAVID_Entrez = pd.read_csv(fpath,sep = '\t',header = None)
    DAVID_Entrez = DAVID_Entrez.rename(columns = {0: 'ENTREZ', 1: 'Map'})
    Map = DAVID_Entrez['Map'].values.tolist()
    OFC = []
    for val in Map:
        start = val.rfind('(')
        end = val.rfind(')')
        val = val[start:end+1]
        OFC.append(val.replace(')','').replace('(',''))
    
    DAVID_Entrez['OFFICIAL_GENE_SYMBOL'] = OFC

    OFC2ENTREZ_df = DAVID_Entrez[['ENTREZ','OFFICIAL_GENE_SYMBOL']]

    ENTREZ = OFC2ENTREZ_df['ENTREZ'].values.tolist()
    OFC = OFC2ENTREZ_df['OFFICIAL_GENE_SYMBOL'].values.tolist()

    OFC2ENTREZ = {}
    for z in range(len(ENTREZ)):
        OFC2ENTREZ[OFC[z]] = ENTREZ[z]
        
    return OFC2ENTREZ
    

