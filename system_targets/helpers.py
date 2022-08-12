import pandas as pd

from configs.rbos import PLACEMENTS

def rbos_next_day(dataset):

    df = dataset[['Close']]
    df.columns = PLACEMENTS.keys()

    df = df.pct_change()

    df['target'] = [df.loc[i,:].sort_values().index[-1] for i in df.index]
    df['target_label'] = df['target'].apply(lambda x: PLACEMENTS[x])

    return df[['target', 'target_label']]

    
    
    
