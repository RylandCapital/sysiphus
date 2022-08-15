import pandas as pd

from configs.rbos import PLACEMENTS

def rbos_next_day(dataset):

    df = dataset[['oc%']]
    df.columns = PLACEMENTS.keys()

    df['target'] = [df.loc[i,:].sort_values().index[-1] for i in df.index]
    df['target_label'] = df['target'].apply(lambda x: PLACEMENTS[x])
    df['target'] = df['target'].shift(-1)
    df['target_label'] = df['target_label'].shift(-1)

    return df[['target', 'target_label']]

    
    
    
