import json

with open('Data/StreamingHistory0.json', encoding="utf8") as f0:
    data0 = json.load(f0)
with open('Data/StreamingHistory1.json', encoding="utf8") as f1:
    data1 = json.load(f1)
with open('Data/StreamingHistory2.json', encoding="utf8") as f2:
    data2 = json.load(f2)

totalTime = 0

songs = {}

data = data0 + data1 + data2

for song in data:
    totalTime += song['msPlayed']
    if (song['trackName'], song['artistName']) in songs:
        songs[(song['trackName'], song['artistName'])] += 1
    else:
        songs[(song['trackName'], song['artistName'])] = 1




songslist = sorted(songs.items(), reverse = True, key = lambda song: song[1])

for i in range(0, 10):
    print("Number " + str(i + 1) + ":\t" + "played: " + str(songslist[i][1]) + " times:")
    print("\t\tTitle:\t" + songslist[i][0][0])
    print("\t\tArtist:\t" + songslist[i][0][1])
    print()

print("Songs Listened: " + str(len(data)))
print("Hours Listened: " + str(totalTime * 2.7778e-7))