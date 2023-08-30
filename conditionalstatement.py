x = int(input("How much cash do you have? "))
asw = input("Can I look into your wallet (y/n)?")

if( x>100000 and not asw == 'y' ):
    print("You rich bastard!")
elif(x>10):
    print("You have more than 10 euros, very nice!")
elif(x==10):
    print("You have exactly 10 euros, nice!")
else:
    print("Your poor bastard!")
