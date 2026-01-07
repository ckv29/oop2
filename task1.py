import asyncio

async def api_call_1():
    await asyncio.sleep(4)
    print('api_call_1 finished')
    return 'result 1'


async def api_call_2():
    await asyncio.sleep(2)
    print('api_call_2 finished')    
    return 'result 2'

async def main():
    task1 = asyncio.create_task(api_call_1())
    task2 = asyncio.create_task(api_call_2())
    
    res1,res2 = await asyncio.gather(task1,task2)
    print(res1,res2)


asyncio.run(main())