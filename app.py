import asyncio
import time
import pandas as pd

async def save_data(delay, what):
    # await asyncio.sleep(delay)
    await asyncio.sleep(delay)
    print(f"{what} delay {delay} {time.strftime('%X')}")
    pd.DataFrame([delay]).to_json(f"test{delay}.json")


async def model_loop():
    tasklist =[]
    for i in range(4):
        print(f"Doing things")
        
        tasklist.append(asyncio.ensure_future(save_data(i, f'hello {i}')))
        # tasklist.append(asyncio.create_task(
        #     save_data(i, f'hello {i}')))
        # # await tasklist[i]  # doesn't work
        print(f"Doing other things {time.strftime('%X')}")
    all_done = [False] * len(tasklist)
    timeout = time.time() + 2

    while not all([_.done() for _ in tasklist]):
        print([_.done() for _ in tasklist])
        await asyncio.sleep(1)
        if timeout < time.time():
            break
    # for i in range(4):
    #     await tasklist[i]  # works...but requires al ltasks to be defined
    # await asyncio.gather(*tasklist)  # does the same as above
    # await asyncio.sleep(5)

def main():

    print(f"started at {time.strftime('%X')}")
    asyncio.run(model_loop())

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    # await task1
    # await task2

    print(f"finished at {time.strftime('%X')}")


if __name__ == "__main__":
    
    main()