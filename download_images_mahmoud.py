import urllib.request
import requests

x = []
with open('imagenet.synset.txt', 'r') as f:
    for line in f:
        x.append(line.rstrip())

print(len(x))
pathToSave = '/Users/mac/Desktop/Downloaded/'
imageNumber = 1
for i in range(len(x)):
    try:
        pathToSave = '/Users/mac/Desktop/Downloaded/'
        extension = x[i][-4:]
        fileName = '%d'%i +extension
        fullPath = pathToSave + fileName
        with open(fullPath,'wb') as f:
            f.write(requests.get(x[i], allow_redirects=True, timeout=100).content)
        print(fileName)
    except Exception as e:
        print(e)
