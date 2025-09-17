import asyncio

async def fun1():
    await asyncio.sleep(2)
    print("hello 1")
async def fun2():
    await asyncio.sleep(2)
    print("hello 2")
async def fun3():
    await asyncio.sleep(5)
    print("hello 3")

async def main(): 
    await asyncio.gather(fun1(), fun2(), fun3())

asyncio.run(main())