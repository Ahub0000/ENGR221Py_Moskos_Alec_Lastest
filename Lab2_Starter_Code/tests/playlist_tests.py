import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest

from playlist import Playlist
from song import Song

@pytest.fixture
def songs_list():
    return [Song("Golden", "HUNTR/X"),
            Song("Ordinary", "Alex Warren"),
            Song("What I Want", "Morgan Wallen ft. Tate McRae"),
            Song("Your Idol", "Saja Boys"),
            Song("Soda Pop", "Saja Boys")]

@pytest.fixture
def new_song():
    return Song("Love Me Not", "Ravyn Lenae")

@pytest.mark.playlisttest1
def test_init_playlist(songs_list):
    p = Playlist(songs_list)
    assert (p.num_songs == len(songs_list) and 
            p.songs == songs_list and 
            p.max_num_songs == len(songs_list))
    
@pytest.mark.playlisttest1
def test_init_playlist_empty():
    p = Playlist([])
    assert (p.num_songs == 0 and 
            p.songs == [] and 
            p.max_num_songs == 0)

@pytest.mark.playlisttest2
def test_insert_playlist(songs_list, new_song):
    p = Playlist(songs_list)
    p.insert_song(new_song)
    assert (p.get_song_at_idx(len(songs_list)) == new_song and p.num_songs == len(songs_list) + 1)

@pytest.mark.playlisttest2
def test_insert_empty_playlist(new_song):
    p = Playlist([])
    p.insert_song(new_song)
    assert (p.get_song_at_idx(0) == new_song and p.num_songs == 1)

@pytest.mark.playlisttest2
def test_insert_playlist_multiple(songs_list, new_song):
    p = Playlist(songs_list)
    for _ in range(50):
        p.insert_song(new_song)
    assert (p.get_song_at_idx(len(songs_list)) == new_song and p.num_songs == len(songs_list) + 50)

@pytest.mark.playlisttest3
def test_delete_playlist(songs_list):
    p = Playlist(songs_list + songs_list)
    num_deletes = p.delete_by_title("Golden")
    assert (p.songs[:8] == (songs_list[1:] + songs_list[1:]) and p.num_songs == 2*(len(songs_list) - 1) and num_deletes == 2)

@pytest.mark.playlisttest3
def test_deleteplaylist_absent(songs_list):
    p = Playlist(songs_list)
    p.delete_by_title("Love Me Not")
    assert (p.songs == songs_list and p.num_songs == len(songs_list))