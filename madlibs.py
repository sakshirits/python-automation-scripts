text= 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
text1=text.replace("."," ")
l=text1.split()
for i in range(len(l)):
    if l[i]=='ADJECTIVE':
        x=input('Enter an adjective:')
        l[i]=x
    if l[i]=='NOUN':
        x=input('Enter a noun:')
        l[i] =x
    if l[i] =='VERB':
        x=input('Enter a verb:')
        l[i]=x

        print(" ".join(

        ))