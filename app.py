import asyncio
import time
import pandas as pd


async def save_data(delay, what):
    # await asyncio.sleep(delay)
    await asyncio.sleep(delay)
    print(f"Writing {what} taking time {delay} {time.strftime('%X')}")
    pd.DataFrame([delay]).to_json(f"test{what}.json")

async def async_wait(wait):
    await asyncio.sleep(wait)

def check_complete(t, tasklist, timeout):
    """
    Note these won't print anything, they will be on another thread
    """
    print([_.done() for _ in tasklist])
    print(timeout - time.time())
    if all([_.done() for _ in tasklist]):
        print("all done")
        return True
    elif time.time() > timeout:
        print('timeout exceeded')
        return True
    else:
        # await asyncio.sleep(5)  # for demo app need this wait, or it will go by too quickly
        return False

# async def model_loop():
def model_loop():
    tasklist =[]
    

    for i in range(4):
        print(f"Model start")
        tasklist.append(asyncio.ensure_future(save_data(i, f'hello {i}')))
        print(f"Result write called {time.strftime('%X')}")
    
    
        # if model_loop is not an async run, just adding ensure future won't actually run them
    
    print("doing more things")
    return tasklist

def main():

    print(f"started at {time.strftime('%X')}")
    # asyncio.run(model_loop())
    
    timeout_length = 2  # seconds of timeout
    timeout = time.time() + timeout_length
    
    tasklist = model_loop()

    # time.sleep(5)
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(tasklist[0])
    while not check_complete(1, tasklist, timeout):  # need this to run to actually execute async writes:
        loop.run_until_complete(async_wait(1))
        # loop.run_until_complete(check_complete(1, tasklist, timeout))  # need this to run to actually execute async writes
        # check_complete(1, tasklist, timeout)  # need this to run to actually execute async writes
        # break

    print(f"finished at {time.strftime('%X')}")


if __name__ == "__main__":
    
    main()