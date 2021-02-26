import pandas as pd
import json
import codecs
import os

baseURL = './xuetong_test'
base = os.listdir(baseURL)
output_file = codecs.open('./xuetong_test/Label.txt', 'w', encoding='utf-8')

for file in base:
    if file.find('.json') > -1:
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

        output_file.write('xuetong_test/'   + img + '.jpg\t' + json.dumps(tags) + '\n')