# Find all close matches of input string from a list
from difflib import get_close_matches
def myclosemathes(word, pattern):
        print(get_close_matches(word, pattern, n= 4, cutoff = 0.12))
word= "156.96"
pattern = ["102.595", "1239", "156.96", "126"]

myclosemathes(word, pattern)