#CONTINUE
for i in range (1,10):
    if i == 6:
        print ('nilai i adalah', 6)
        continue
        #print ('cek bro') #ga kebaca dan bahkan problem
    print ('nilai saat ini adalah:', i)

else:
    print ('akhir dari loop')



#PASS
for i in range (1,10):
    if i == 6:
        print ('nilai i adalah', 6)
        pass
        print ('cek bro') #ga kebaca
    print ('nilai saat ini adalah:', i)

else:
    print ('akhir dari loop')