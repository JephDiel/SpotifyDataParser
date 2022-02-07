import json
from collections import defaultdict
from json.encoder import INFINITY
import random

with open('Data/StreamingHistory0.json', encoding="utf8") as f0:
    data0 = json.load(f0)
with open('Data/StreamingHistory1.json', encoding="utf8") as f1:
    data1 = json.load(f1)
with open('Data/StreamingHistory2.json', encoding="utf8") as f2:
    data2 = json.load(f2)

totalTime = 0

songs = {}

data = data0 + data1 + data2

links = defaultdict(lambda: defaultdict(lambda: 0.5))

for i in range(len(data) - 1):
    song = data[i]
    next_song = data[i + 1]

    if song['msPlayed'] > 30000:
        links[song['trackName'], song['artistName']][next_song['trackName'], next_song['artistName']] *= 1.01
    else:
        links[song['trackName'], song['artistName']][next_song['trackName'], next_song['artistName']] *= 0.99


print("learning complete")

SAMPLES = 1000

print("Testing on " + str(SAMPLES) + " random samples")
random.seed(314)

correct = 0
incorrect = 0
unknown = 0

for i in range(SAMPLES):
    j = random.randrange(10, len(data) - 1)
    song = data[j]
    next_song = data[j + 1]

    predicted_next_song = ""
    max_link = -INFINITY

    for link in links[song['trackName'], song['artistName']]:
        link_sum = 0
        for k in range(10):
            song = data[j - k]
            # print(link_sum)
            link_sum += links[song['trackName'], song['artistName']][link] / (k + 1)
        
        # link_sum /= 55

        if link_sum > max_link:
            max_link = link_sum
            predicted_next_song = link
    
    if predicted_next_song == (next_song['trackName'], next_song['artistName']):
        correct += 1
        # print("Song:", (song['trackName'], song['artistName']))
        # # print("Actual Next:", (next_song['trackName'], next_song['artistName']))
        # print("Predicted Next:", predicted_next_song)
        # print("Link:", max_link)
        # print()
    else:
        incorrect += 1
    
    # print("Song:", (song['trackName'], song['artistName']))
    # print("Actual Next:", (next_song['trackName'], next_song['artistName']))
    # print("Predicted Next:", predicted_next_song)
    # print("Link:", max_link)
    # print()

print("Correct:", correct)
print("Incorrect:", incorrect)
print("Unknown:", unknown)
print("Accuracy:", str(correct / (correct + incorrect))[2:4] + "%")