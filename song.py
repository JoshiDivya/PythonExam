class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        if self.next!=None:
            return True
        return False

first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("Third Eye")

first.next_song(second);
second.next_song(third);
third.next_song(first)

print(first.is_repeating_playlist())