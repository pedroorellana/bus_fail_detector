import pickle

import pandas as pd 

def save_predictions(predictions):
    predictions.to_csv("predictions.csv", index=False)
    return 

def save_model(model_name, model):
    with open(f'models\\{model_name}.pkl', 'wb') as file:
        pickle.dump(model, file)
    return 

def load_model(model_name):
    with open(f'models\\{model_name}.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

def predict_single_model(model_name, features):
    """
    Given a model name and a set of features, load the model, make a prediction, and return a dataframe
    with the prediction and the probability of the prediction
    
    :param model_name: the name of the model you want to use to make predictions
    :param features: The features to use for prediction
    :return: a dataframe with the predictions and the probabilities of the predictions.
    """
    model = load_model(model_name)
    y_predict = model.predict(features)
    y_proba = model.predict_proba(features)[:,1]
    predictions = pd.DataFrame()
    predictions[model_name] = y_predict.tolist()
    predictions[f"{model_name}_prob"] = y_proba.tolist()
    return predictions

def predict_all_models(features):
    """
    It predicts the output for all the models.
    Each columns have the predicted type of error and the next columns his probability.
    1 means the error is occurring.
    
    :param features: The features to use for prediction
    :return: a dataframe with the predictions of the two models.
    """
    pred0 = predict_single_model("satelites_rf_sklearn",features)
    pred1 = predict_single_model("satelites_xgboost",features)
    all_pred = pd.concat([pred0,pred1], axis=1)
    return all_pred

