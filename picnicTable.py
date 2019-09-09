picnicItems={'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

def printPicnicTable(picnicItems,leftwidth,rightwidth):
    print('PICNIC ITEMS'.center(leftwidth+rightwidth,'-'))
    for k,v in picnicItems.items():
        print(k.ljust(leftwidth,'.')+ str(v).rjust(rightwidth))


printPicnicTable(picnicItems,12,8)



