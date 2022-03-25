import numpy as np
import pickle
from keras.preprocessing.sequence import pad_sequences
from tensorflow import keras

MODEL_FILE_ROOT = "/deploy/models"


#model = keras.models.load_model(MODEL_FILE_ROOT+'/gru')

with open(MODEL_FILE_ROOT+'/gru_model.pkl', 'rb') as handle:
    model = pickle.load(handle)

with open(MODEL_FILE_ROOT+'/text_tokenizer.pkl', 'rb') as handle:
    loaded_tokenizer = pickle.load(handle)

def prepare_text_for_predict(text, tokenizer, MAX_NB_WORDS=75000,MAX_SEQUENCE_LENGTH=500):
  np.random.seed(7)
  sequences = tokenizer.texts_to_sequences(text)
  text = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
  return text

def predict_with_trained_model(model, tokenizer, text):
  text_seq = prepare_text_for_predict(text,tokenizer)
  pred = model.predict(text_seq[:1])
  prediction=np.argmax(pred,axis=1)
  return prediction

def humanize_output(risk_category):
    if risk_category == 0:
        return "Don't worry, there is no risk (Category 0)"
    elif risk_category == 1:
        return "Don't worry, there is little risk (Category I)"
    elif risk_category == 2:
        return "There is a mild risk. (Category II)"
    elif risk_category == 3:
        return "There is risk ! (Category III)"
    elif risk_category == 4:
        return "Be careful, it is risky !! (Category IV)"


def predict_with_dl_model(text):
    prediction = predict_with_trained_model(model, loaded_tokenizer, text)
    return humanize_output(prediction)