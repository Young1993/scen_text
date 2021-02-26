import pandas as pd
import json
import codecs
import os
import re
import random

baseURL = './xuetong'  # ./xuetong_test
base = os.listdir(baseURL)
train_label = codecs.open('train_label.txt', 'w', encoding='utf-8')
test_label = codecs.open('test_label.txt', 'w', encoding='utf-8')
count = 600

for i, file in enumerate(base):
    if not re.search('\._.*\.json', file) and file.find('.json') > -1:
        # print(i, file)
        img = file.split('.json')[0]
        f = open(os.path.join(baseURL, file))
        content = f.read()
        label = json.loads(content)
        # print(label, len(label))

        tags = []
        for block in label:
            if len(block['area']) <= 8:
                tmp = {"transcription": block['label'],
                       "points": [[block['area'][0], block['area'][1]], [block['area'][2], block['area'][3]],
                                  [block['area'][4], block['area'][5]], [block['area'][6], block['area'][7]]],
                       "difficult": False}
                tags.append(tmp)

        if random.random() >= 0.1:
            count -= 1
            os.system('mv xuetong/' + img + '.jpg' + ' train_imgs/')
            train_label.write('train_imgs/'   + img + '.jpg\t' + json.dumps(tags) + '\n')
        else:
            os.system('mv xuetong/' + img + '.jpg' + ' test_imgs/')
            test_label.write('test_imgs/' + img + '.jpg\t' + json.dumps(tags) + '\n')

        if count < 0:
            break
