import asyncio

semaphore = asyncio.Semaphore(3)

async def test_func(n):
    print(f' coroutine {n} ask ascess')
    async with semaphore:
        print(f' coroutine {n} started!')
        await asyncio.sleep(2)
        print(f' coroutine {n} finished!')




async def main():
    tasks = []
    tasks = [test_func(i) for i in range(1,6)]         
    await asyncio.gather(*tasks)


asyncio.run(main())