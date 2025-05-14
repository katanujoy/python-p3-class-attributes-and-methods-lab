class Song:
    count = 0  # Class attribute to keep track of the total number of songs
    genres = []  # Class attribute to store unique genres
    artists = []  # Class attribute to store unique artists
    genre_count = {}  # Class attribute to count songs per genre
    artist_count = {}  # Class attribute to count songs per artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Call class methods to update the class attributes
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
another_song = Song("Hotline Bling", "Drake", "Pop")
third_song = Song("Formation", "Beyonce", "Pop")
fourth_song = Song("99 Problems", "Jay-Z", "Rap")

# Accessing class attributes
print(Song.count)  # Output: 4
print(Song.artists)  # Output: ['Jay-Z', 'Drake', 'Beyonce']
print(Song.genres)  # Output: ['Rap', 'Pop']
print(Song.genre_count)  # Output: {'Rap': 2, 'Pop': 2}
print(Song.artist_count)  # Output: {'Jay-Z': 2, 'Drake': 1, 'Beyonce': 1}
