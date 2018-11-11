#from app import app
from flask import render_template, flash, redirect, url_for, request, Flask
from forms import Params
from six.moves import cPickle
import time
import numpy as np
import os
from model import Model
from beam import BeamSearch
from config import Config
import flask_wtf
import tensorflow as tf

app = Flask(__name__)
app.config.from_object(Config)

ai = None

@app.before_first_request
def init_model():
    print("GETTING SAMPLE")
    save_dir = r'..\word-rnn-tensorflow\save'
    full_path = os.path.join(save_dir, 'config.pkl')
    print(full_path)
    with open(full_path, 'rb') as f:
        saved_args = cPickle.load(f)
    #print()

    print("ABOUT TO INITIALIZE MODEL")
    global ai
    ai = Model(saved_args, True)
    #return model

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Params()
    song = ""
    if request.method == "POST":
        print("DO THING")
        print(form.prime.data)
        global ai
        print("GETTING GLOBAL")
        song = sample(form.prime.data, ai)
        print("GOT SAMPLE")
    print("DO FIRST THING")
    return render_template('theonlyhtmlfileweneed.html', form=form, song=song)


def sample(prime, model):
    save_dir = r'..\word-rnn-tensorflow\save'
    with open(os.path.join(save_dir, 'words_vocab.pkl'), 'rb') as f:
        print("LOADING words_vocab.pkl")
        words, vocab = cPickle.load(f)
    with tf.Session() as sess:
        print("IN SESSSION")
        tf.global_variables_initializer().run()
        saver = tf.train.Saver(tf.global_variables())
        ckpt = tf.train.get_checkpoint_state(save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            return model.sample(sess, words, vocab, 500, prime, 1, 1, 4, False)

if __name__ == '__main__':
    app.run(threaded=True)
