import json
from datetime import datetime, timedelta

# add keywords! make sure they are lower case
keywords = [
    'school',
    'weather'
]
 
# update this file to whatever file you're passing in
f = open('./dataset.json')
data = json.load(f)

links = set()
for entry in data:
    article_date = datetime.strptime(entry['date'].split('T')[0], '%Y-%m-%d')
    if article_date >= (datetime.now() - timedelta(days=6*365)):
        links.update([entry['url'] for word in keywords if word in entry['title'].lower()])

for link in links:
    print(link)
 
f.close()