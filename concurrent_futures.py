"""
Multi-thread using concurrent futures, high level api
"""
from concurrent import futures
from time import sleep, time


def do_task(name, t):
    sleep(t)
    print(f"did task {name} in time {t}")
    return name + str(t)

def executor_map():
    exe = futures.ThreadPoolExecutor(3)  # controls how many workers there are
    print("Program start")
    names = "abcde"
    ts = range(5, 0, -1)
    res = exe.map(do_task, names, ts)
    real_results = list(res)
    print(real_results)

if __name__ == "__main__":

    start = time()
    executor_map()
    print(f"Took {time() - start} sec")

    # for 
    #     ex.submit(do_task, i)
    #     for i in range(5, 0, -1)
    # ]

# for f in futures.as_completed(wait_for):
#     print('main: result: {}'.format(f.result()))
    
