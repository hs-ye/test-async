import asyncio
import time
import pandas as pd

async def save_data(delay, what):
    # await asyncio.sleep(delay)
    await asyncio.sleep(delay)
    print(f"{what} delay {delay} {time.strftime('%X')}")
    pd.DataFrame([delay]).to_json(f"test{delay}.json")

async def check_complete(t, tasklist, timeout):
    """
    Note these won't print anything, they will be on another thread
    """
    print([_.done() for _ in tasklist])
    print(timeout - time.time())
    if time.time() > timeout:  # timeout no longer works here
        print('timeout exceeded')
        return False
    await asyncio.sleep(5)
    return True

# async def model_loop():
def model_loop():
    tasklist =[]
    loop = asyncio.get_event_loop()
    for i in range(4):
        print(f"Doing things")
        
        tasklist.append(asyncio.ensure_future(save_data(i, f'hello {i}')))
        # tasklist.append(asyncio.create_task(
        #     save_data(i, f'hello {i}')))
        # # await tasklist[i]  # doesn't work
        print(f"Doing other things {time.strftime('%X')}")
    all_done = [False] * len(tasklist)
    timeout = time.time() + 1
    

    while not all([_.done() for _ in tasklist]):
        if loop.run_until_complete(check_complete(1, tasklist, timeout)):
            # this loop above is a blocking loop, will not run until complete
            print('should be breaking')
            break  # timeout exceeded
        #     await asyncio.sleep(1)
    
    # for i in range(4):
    #     await tasklist[i]  # works...but requires al ltasks to be defined
    # await asyncio.gather(*tasklist)  # does the same as above
    # await asyncio.sleep(5)

def main():

    print(f"started at {time.strftime('%X')}")
    # asyncio.run(model_loop())
    model_loop()

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    # await task1
    # await task2

    print(f"finished at {time.strftime('%X')}")


if __name__ == "__main__":
    
    main()