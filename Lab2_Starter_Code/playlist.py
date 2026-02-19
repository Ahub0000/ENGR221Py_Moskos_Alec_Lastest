"""
Author: YOUR NAME
Filename: playlist.py
Description: Implementation of a playlist as an array with duplicates
"""

from song import Song

class Playlist:
    def __init__(self, initial_songs):
        # capacity = size of the initial list
        self.max_num_songs = len(initial_songs)

        # number of actual songs currently stored
        self.num_songs = self.max_num_songs

        # make an internal array and copy songs in (NO list methods)
        self.songs = [None] * self.max_num_songs
        for i in range(self.max_num_songs):
            self.songs[i] = initial_songs[i]

    # Return the number of songs in the playlist
    def get_num_songs(self):
        return self.num_songs

    # Return the current songs list
    def get_songs(self):
        return self.songs

    # Return the song at index idx or None if idx is outside of bounds
    def get_song_at_idx(self, idx):
        if 0 <= idx and idx < self.num_songs:
            return self.songs[idx]
        return None

    # Set index idx to the given song (do nothing if out of bounds)
    def set_song_at_idx(self, idx, song):
        if 0 <= idx and idx < self.num_songs:
            self.songs[idx] = song

    # Insert a song to the end of the playlist
    def insert_song(self, song):
        # If the playlist is full, extend capacity
        if self.num_songs == self.max_num_songs:
            new_max = self.max_num_songs * 2
            new_songs = [None] * new_max

            for i in range(self.num_songs):
                new_songs[i] = self.songs[i]

            self.songs = new_songs
            self.max_num_songs = new_max

        self.songs[self.num_songs] = song
        self.num_songs += 1

    # Return the index of the given song title, or -1 if not found
    def search_by_title(self, song_title):
        for i in range(self.num_songs):
            if self.songs[i].title == song_title:
                return i
        return -1

    # Delete ALL occurrences of the title and return how many deleted
    def delete_by_title(self, song_title):
        count_deleted = 0
        i = 0

        while i < self.num_songs:
            if self.songs[i] is not None and self.songs[i].title == song_title:
                count_deleted += 1

                for j in range(i, self.num_songs - 1):
                    self.songs[j] = self.songs[j + 1]

                self.songs[self.num_songs - 1] = None
                self.num_songs -= 1
                # don't increment i
            else:
                i += 1

        return count_deleted

    # Print all songs in the playlist
    def traverse(self):
        for i in range(self.num_songs):
            print(self.songs[i])
