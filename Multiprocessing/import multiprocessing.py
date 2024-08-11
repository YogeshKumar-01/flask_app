import multiprocessing

def squre(n):
    return n**2

if __name__ == '__main__':
    with multiprocessing.Pool(processes = 4) as pool:
        out = pool.map( squre , [1,2,3,4,5,6,7,8,9])
        print(out)