import pandas as pd
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import numpy as np
a = NaiveBayesAnalyzer()
import os

dir = '/home/cusp/jn1573/tweets'

def sent(row):
        #print row['Text']
        return TextBlob(row['Text'], analyzer=a).sentiment.p_pos

for subdir, dirs, files in os.walk(dir):
        for filename in files:
                f = os.path.join(subdir, filename)
                print f
                c = pd.read_csv(f, lineterminator='\n')
                if len(c.index) == 0:
                        continue
                c = c.dropna(subset=['Text'])
                #c['p_pos'] = c.apply(sent, 1)
                p_pos = c.apply(sent, 1)
                #print filename[10:-10], len(c.index), np.mean(c['p_pos'])
                print filename[10:-10], len(p_pos), np.mean(p_pos)