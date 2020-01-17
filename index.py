from flask import Flask, render_template, request
from rake_nltk import Rake
from tweepy import OAuthHandler
import score_texts_emojis_v5
import json
import hashcode

import tensorflow
app = Flask(__name__)

ckey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
csecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
atoken = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
asecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

r = Rake()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main' , methods=['GET'])
def main():
    keyword = request.args.get('keyword')
    happy_buffer,sad_buffer,fear_buffer,love_buffer,angry_buffer,happy_phrases,sad_phrases,fear_phrases,love_phrases,angry_phrases,happy_location,sad_location,fear_location,love_location,angry_location,top_keywords = score_texts_emojis_v5.start(r , auth , keyword , 1000)
    
    happy_hash,sad_hash,fear_hash,angry_hash,love_hash = hashcode.hash_function(happy_location,sad_location,fear_location,love_location,angry_location)
    


    print("tensorboard_accuracy ??=0.75178")
    return render_template('main.html' , happy_buffer=happy_buffer,sad_buffer=sad_buffer,fear_buffer=fear_buffer,love_buffer=love_buffer,angry_buffer=angry_buffer, keyword=keyword ,total_happy=len(happy_buffer),total_sad=len(sad_buffer),total_fear=len(fear_buffer),total_love=len(love_buffer),total_angry=len(angry_buffer),happy_phrases=happy_phrases,sad_phrases=sad_phrases,fear_phrases=fear_phrases,love_phrases=love_phrases,angry_phrases=angry_phrases,top_keywords=top_keywords)

if __name__ == '__main__':
    app.run(threaded=False)
