'''T= open('FileIO2.txt','r')
T.seek(6)
print(T.tell())
data = T.read(6)

print(data)'''

T= open('FileIO3.txt','w')
T.write('Tejas3Khaire!')
T.truncate(5)

To = open('FileIO3.txt','r')
print(To.readlines())


