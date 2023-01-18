# !/usr/bin/env python

import gzip
import json

with gzip.open('news.txt.gz', 'rb') as f:
    file_content = f.read()
    news = json.loads(file_content)
    print("This file contains {} items of MRN_STORY content, starting {} and ending {}:".format(len(news['Items']), min([n['data']['firstCreated'] for n in news['Items']]), max([n['data']['firstCreated'] for n in news['Items']])))
    for item in news['Items']:
        print(f"""Headline \"{item['data']['headline']}\" was first created {item['data']['firstCreated']} and does {"" if True in item['data']['subjects'] else "not"} have subject code \"N2:KR\".""")