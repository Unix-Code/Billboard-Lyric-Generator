from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import Params
from six.moves import cPickle
import time
import numpy as np
import os
from app.model import Model
from app.beam import BeamSearch

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Params()
    song = ""
    if request.method == "POST" and form.prime != "":
        print("DO THING")
        song = sample(form.prime)
        print("GOT SAMPLE")
    print("DO FIRST THING")
    return render_template('theonlyhtmlfileweneed.html', form=form, song=song)

def sample(prime):
    print("GETTING SAMPLE")
    save_dir = r'word-rnn-tensorflow\save'
    full_path = os.path.join(os.getcwd(), save_dir, 'config.pkl')
    print(full_path)
    with open(full_path, 'rb') as f:
        saved_args = cPickle.load(f)
    #print()
    with open(os.path.join(save_dir, 'words_vocab.pkl'), 'rb') as f:
        print("LOADING words_vocab.pkl")
        words, vocab = cPickle.load(f)
    print("ABOUT TO INITIALIZE MODEL")
    model = Model(saved_args, True)
    with tf.Session() as sess:
        print("IN SESSSION")
        tf.global_variables_initializer().run()
        saver = tf.train.Saver(tf.global_variables())
        ckpt = tf.train.get_checkpoint_state(save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            return model.sample(sess, words, vocab, 500, prime, 1, 1, 4, False)
