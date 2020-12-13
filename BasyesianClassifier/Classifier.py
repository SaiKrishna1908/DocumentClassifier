import json
import os

class bayes_classifier:
    def __init__(self):
        if not os.path.exists('config.json'):
            print('Not config file found')
            os.mkdir('../config.json')

    def classify(self, path):
        print('Classification logic')



