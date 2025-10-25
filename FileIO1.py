'''T = open('FileIO1.txt','r')
while True:
 Vname = T.readline()
 Vname = T.readlines()
 if not Vname:
  break
 print(Vname)
'''
 #  Writelines:
'''T = open('Filewritels.txt','w')
Vname = (' Line 1\n Line 2\n Line 3\n Line 4\n Line 5\n')
T.writelines(Vname)
T.close()'''
f = open('FileIO1.txt', 'r')
while True:
    line = f.readlines()
    if not line:
        break
    print(line)

