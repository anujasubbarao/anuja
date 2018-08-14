string=raw_input()
char=0
word=0
for i in string:
      char=char+1
      if(i==' '):
            word=word+1
print(char-word)
