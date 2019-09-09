# character count
# pprint stands for pretty print
import pprint

messages='It was the bright cold day in April, and the clocks were striking thirteen. Actually it was raining that day'
count={}
for character in messages:
    count.setdefault(character,0)
    count[character]+=1

print(count)
pprint.pprint(count)

# wordcount
wordcount={}
messageList=messages.split()
for msg in messageList:
    if msg not in wordcount:
      wordcount[msg]=1
    else:
        wordcount[msg]+=1
print(wordcount)
