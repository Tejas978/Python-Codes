'''T = open('Hello.txt','r')  # r mode is default...,'rt','rb'
Vname = T.read()
print(Vname)
T.close()'''

'''T = open('Hello.txt','w')             # Saved Gets Deleted And new gets Paste
T.write('Hello Tejas Be Positive')
T.close()
'''
T = open('Hello.txt','a')             # Saved Gets Deleted And new gets Paste
T.write('\n Hello Tejas God is with You if you have Faith')
T.close()
