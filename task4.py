import asyncio

async def main():
    semaphore = asyncio.Semaphore(2)
    tasks = []
    tasks = [test_func(i,semaphore) for i in range(1,6)]         
    await asyncio.gather(*tasks)



async def test_func(n,semaphore):
    print(f' coroutine {n} ask ascess')
    async with semaphore:
        print(f' coroutine {n} started!')
        await asyncio.sleep(2)
        print(f' coroutine {n} finished!')


asyncio.run(main())