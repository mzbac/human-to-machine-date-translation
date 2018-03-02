import pickle
import torch
from torch.autograd import Variable

SOS_token = 0
EOS_token = 1

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

def evaluate(sentence,encoder,decoder,human_char2index,machine_index2char, max_length=11):
    indexes = [human_char2index[char] for char in sentence]
    input_variable = Variable(torch.LongTensor(indexes).view(-1, 1))
    input_length = input_variable.size()[0]
    encoder.eval()
    decoder.eval()
    # Run through encoder
    encoder_hidden = encoder.init_hidden()
    encoder_outputs, encoder_hidden = encoder(input_variable, encoder_hidden)

    # Create starting vectors for decoder
    decoder_input = Variable(torch.LongTensor([[SOS_token]])) # SOS
    decoder_context = Variable(torch.zeros(1, decoder.hidden_size))


    decoder_hidden = encoder_hidden
    
    decoded_words = []
    
    # Run through decoder
    for di in range(max_length):
        decoder_output, decoder_context, decoder_hidden, decoder_attention = decoder(decoder_input, decoder_context, decoder_hidden, encoder_outputs)

        # Choose top word from output
        topv, topi = decoder_output.data.topk(1)
        ni = topi[0][0]
        if ni == EOS_token:
            #decoded_words.append('<EOS>')
            break
        else:
            decoded_words.append(machine_index2char[ni])
            
        # Next input is chosen word
        decoder_input = Variable(torch.LongTensor([[ni]]))

    
    return decoded_words