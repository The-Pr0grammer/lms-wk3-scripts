import sys
import re


word=sys.argv[1]
pattern=rf'{word.replace("_","[a-z]")}'

print(pattern)

def find_word(input):
        with open('/usr/share/dict/words') as w_list:
                for w in w_list:
                        len(w) == 6 and re.search(pattern, w, re.IGNORECASE) and print(w)



find_word(word)