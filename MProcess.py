import multiprocessing
import requests
import concurrent.futures

def downloadfile(url,name):
    print("Started Downloading{name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg","wb").write(response.content)
    print("Finished Downloading{name}")

url = "https://picsum.photos/2000/3000"

'''pros = []
for i in range (4):
    downloadfile(url,i)
    p = multiprocessing.Process(target = downloadfile,args  = [url,i])
    p.start()
    pros.append(p)

for p in pros:
    p.join()'''

with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range[10]]
    l2 = [i for i in range[10]]
    results = executor.map(downloadfile, l1, l2)
    for r in results:
     print(r)