import pandas as pd

def feature_calculation(data_clean):     
    selected_features = ['satelites',
                         'alimentacion',
                         'bateria',
                         'retardo',
                         'rssi_celular',
                         'ignicion']                         
    first_decil = data_clean[selected_features]\
        .quantile(q=0.1, axis=0)\
        .add_prefix('first_decil_')
    last_decil = data_clean[selected_features]\
        .quantile(q=0.9, axis=0)\
        .add_prefix('last_decil_')
    tmp_mean = data_clean[selected_features]\
        .mean()\
        .add_prefix('mean_')
    tmp_std = data_clean[selected_features]\
        .std()\
        .add_prefix('std_')
    tmp_skew = data_clean[selected_features]\
        .skew()\
        .add_prefix('skew_')
    tmp_kurt = data_clean[selected_features]\
        .kurtosis()\
        .add_prefix('kurt_')

    feat_vec = pd.concat([first_decil,
                          last_decil,
                          tmp_mean,
                          tmp_std,
                          tmp_skew,
                          tmp_kurt],
                         axis=0)
    return feat_vec

def feature_calc_label(data_clean, label):
    feat_vec = feature_calculation(data_clean)
    feat_vec['label'] = label
    return feat_vec

def feature_calc_label_batch(clean_data, label):
    feat_vec = pd.DataFrame()
    for element in clean_data:
        feat_vec = feat_vec.append(feature_calc_label(element, label),ignore_index=True)
    return feat_vec

def feature_calc_batch(clean_data):
    feat_vec = pd.DataFrame()
    for element in clean_data:
        feat_vec = feat_vec.append(feature_calculation(element),ignore_index=True)
    return feat_vec
