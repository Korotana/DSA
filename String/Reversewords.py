def reverseWords(self, s):
    # code here
    words = s.split()

    words.reverse()

    return ' '.join(words)

s = "  i like this program very much  "
reverseWords(s)