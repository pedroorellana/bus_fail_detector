from packages.extract_data import extract_raw_data_batch
from packages.extract_data import clean_prepare_data_batch
from packages.feature_calc import feature_calc_batch
from packages.model import predict_all_models, save_predictions

def main():
    # raw_data_list is a list of pandas dataframes, each one containing a sample of data 
    # predict a fail. Is the main input.
    # The only constraint of this elements is that the column 
    # devicetime should be a datetime object. look at "extract_raw_data_from_csv"
    raw_data_list = extract_raw_data_batch("data\\Ignición\\IGN_Mala")
    prep_data_list = clean_prepare_data_batch(raw_data_list)
    features = feature_calc_batch(prep_data_list)
    predictions = predict_all_models(features)
    # This will save the predictions. Look at "predict_all_models" docstring
    # for more info
    save_predictions(predictions)

if __name__=="__main__":
    main()