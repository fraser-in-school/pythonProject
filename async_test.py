import asyncio

async def your_function(parameter):
    # 在这里执行你的函数逻辑
    print(f"函数被调用，参数为: {parameter}")
    await asyncio.sleep(10)  # 模拟函数执行

async def main():
    parameters = [1, 2, 3, 4, 5]  # 参数列表

    # 创建一个任务列表，每个任务调用函数一次，传递不同的参数
    rets = []
    for i in range(len(parameters)):
        rets.append(your_function(parameters))
        print(i)

    # 并发执行任务
    await asyncio.gather(*rets)

if __name__ == '__main__':
    # map = {}
    # map[1] = 2
    # if 1 in map:
    #     print(4)
    # else:
    #     print(2)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
