from flask import Flask
from flask import request
from flask import json
from utils import load_obj
from utils import evaluate
from model import EncoderRNN, AttnDecoderRNN
import torch as t

app = Flask(__name__)
human_char2index = load_obj('./human_char2index')
machine_index2char = load_obj('./machine_index2char')
human_n_chars = 41
machine_n_chars = 13
hidden_size = 500
n_layers = 2
dropout_p = 0.05
attn_model = 'general'

@app.route('/', methods=['GET'])
def index():
    #payload = json.loads(request.get_data().decode('utf-8'))
    prediction = predict(request.args['date'])
    data = {}
    data['data'] = prediction
    return json.dumps(data)

def load_model():
    encoder = EncoderRNN(human_n_chars, hidden_size, n_layers)
    decoder = AttnDecoderRNN(attn_model, hidden_size, machine_n_chars, n_layers, dropout_p=dropout_p)
    encoder.load_state_dict(t.load('encoder.pth'))
    decoder.load_state_dict(t.load('decoder.pth'))
    return encoder, decoder

def predict(dateStr):
    encoder, decoder = load_model()
    return ''.join(evaluate(dateStr,encoder,decoder,human_char2index, machine_index2char))

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)