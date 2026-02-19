import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest

from nodupesplaylist import NoDupesPlaylist
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

@pytest.fixture
def new_song2():
    return Song("Manchild", "Sabrina Carpenter")

@pytest.fixture
def songs_list_dupes():
    return [Song("Love Me Not", "Ravyn Lenae"),
            Song("Love Me Not", "Ravyn Lenae"),
            Song("Love Me Not", "Ravyn Lenae"),
            Song("Manchild", "Sabrina Carpenter"),
            Song("Manchild", "Sabrina Carpenter")]

@pytest.mark.nodupes1
def test_init_nodupes(songs_list):
    ndp = NoDupesPlaylist(songs_list)
    assert (ndp.num_songs == 5 and set(ndp.songs[:5]) == set(songs_list))

@pytest.mark.nodupes1
def test_init_nodupes_dupes(songs_list_dupes, new_song, new_song2):
    ndp = NoDupesPlaylist(songs_list_dupes)
    assert (ndp.num_songs == 2 and set(ndp.songs[:2]) == set([new_song, new_song2]))

@pytest.mark.nodupes2
def test_search_nodupes(songs_list_dupes):
    ndp = NoDupesPlaylist(songs_list_dupes)
    assert ndp.search_by_title("Love Me Not") != -1

@pytest.mark.nodupes2
def test_search_nodupes_absent(songs_list_dupes):
    ndp = NoDupesPlaylist(songs_list_dupes)
    assert ndp.search_by_title("Golden") == -1

@pytest.mark.nodupes3
def test_insert_nodupes(songs_list, new_song):
    ndp = NoDupesPlaylist(songs_list)
    ndp.insert_song(new_song)
    assert (ndp.num_songs == len(songs_list) + 1 and set(ndp.songs[:6]) == set(songs_list + [new_song]))

@pytest.mark.nodupes3
def test_insert_nodupes_empty(new_song):
    ndp = NoDupesPlaylist([])
    ndp.insert_song(new_song)
    assert (ndp.num_songs == 1 and set(ndp.songs[:1]) == set([new_song]))

@pytest.mark.nodupes3
def test_insert_nodupes_dupes(songs_list_dupes, new_song, new_song2):
    ndp = NoDupesPlaylist(songs_list_dupes)
    ndp.insert_song(new_song)
    assert (ndp.num_songs == 2 and set(ndp.songs[:2]) == set([new_song, new_song2]))

@pytest.mark.nodupes4
def test_delete_nodupes(songs_list_dupes, new_song2):
    ndp = NoDupesPlaylist(songs_list_dupes)
    ndp.delete_by_title("Love Me Not")
    assert (ndp.num_songs == 1 and set(ndp.songs[:1]) == set([new_song2]))

@pytest.mark.nodupes4
def test_delete_nodupes_absent(songs_list_dupes):
    ndp = NoDupesPlaylist(songs_list_dupes)
    ndp.delete_by_title("Golden")
    assert (ndp.num_songs == 2 and set(ndp.songs[:2]) == set(songs_list_dupes))

@pytest.mark.nodupes5
def test_traverse_nodupes(capfd, songs_list_dupes):
    ndp = NoDupesPlaylist(songs_list_dupes)
    ndp.traverse()
    out, _ = capfd.readouterr()
    assert out == "Title: Love Me Not\nArtist: Ravyn Lenae\nTitle: Manchild\nArtist: Sabrina Carpenter\n" or \
           out == "Title: Manchild\nArtist: Sabrina Carpenter\nTitle: Love Me Not\nArtist: Ravyn Lenae\n"
