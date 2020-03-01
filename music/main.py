from music.entity.album import Album
from music.entity.song import Song

album = Album('albumname', 2020)
song1 = Song('songname 1' , 1)
song2 = Song('songname 2' , 2)

album.songList.append(song1)
album.songList.append(song2)


print(album.albumname)
print(album.albumyear)

for Song in album.songList:
    print(('songname: {} length:{}').format(Song.songName, Song.songLength))