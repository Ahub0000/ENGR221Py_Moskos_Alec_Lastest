from song import Song

class NoDupesPlaylists:
    def __init__(self, initial_songs):
        self.max_num_songs = max(1, len(initial_songs))  # starting size
        self.songs = [None] * self.max_num_songs  # array of songs
        self.num_songs = 0                         # number of songs stored

        for s in initial_songs:        #loop through input
            #only add if title is not already in playlist
            if self.search_by_title(s.title) == -1: 
                #resize array if it is full
                if self.num_songs == self.max_num_songs: #resize
                    new = [None] * (self.max_num_songs)
                    for i in range (self.num_songs):
                        new[i] = self.songs[i]    #copy old songs
                    self.songs = new
                    self.max_num_songs *= 2       #update size
                
                self.songs[self.num_songs] = s    #add songs
                self.num_songs += 1               #increase count
    
    def search_by_title(self, title):
        #look for song title in playlist
        for i in range(self.num_songs):
            if self.songs[i].title == title:
                return i   #return index if found
            return -1      #return -1 if not found
    
    def insert_song(self, song):
        #do not insert if array is full
        if self.search_by_title(song.title) != -1:
            return
        #resize array if full
        if self.num_songs == self.max_num_songs:
            new = [None] * (self.max_num_songs * 2)
            for i in range(self.num_songs):
                new[i] = self.songs[i]   # copy songs
            self.songs = new
            self.max_num_songs *= 2

        self.songs[self.num_songs] = song  #insert at end
        self.num_songs += 1       #update count

    def delete_by_title(self, title):
        idx = self.search_by_title(title)    #find song index

        if idx == -1:
            return False              # song not found
        #shift songs left to remove gap
        for i in range(idx, self.num_songs - 1):    
            self.songs[i] = self.songs[i + 1]      
        
        self.songs[self.num_songs - 1] = None       #clear last slot
        self.num_songs -= 1                          #decrease count
        return True
    
    def traverse(self):
        #print all songs in the playlist
        for i in range(self.num_songs):
            print(f"Title: {self.songs[i].title}")
            print(f"Artist: {self.songs[i].artist}")

