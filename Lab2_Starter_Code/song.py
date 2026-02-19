"""
Author: Prof. Alyssa
Filename: song.py
Description: Stores the information for a song
    You do NOT need to modify this file.
"""

class Song():
    # The constructor is run every time a new playlist object is created
    def __init__(self, title, artist):
        self.title = title      # The title of the song
        self.artist = artist    # The artist of the song

    # Enables custom formatting when printing a Song object
    def __str__(self):
        return f"Title: {self.title}\n" \
               f"Artist: {self.artist}"
    
    # Defines custom equivalence comparisons
    def __eq__(self, other):
        if isinstance(other, Song):
            return self.title == other.title and self.artist == other.artist
        return False
    
    # Defines a custom hash for set creation
    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))