"""演示 yield 的用法
"""

import sys

def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b
"""
上述用 yield 来编写的函数可以是无限循环的。
因为在每个 yield 的地方可以返回调用函数。
下一次再调用这个函数的时候，从 yield 的下一个语句开始
执行。

"""

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("need a parameter")
        sys.exit(0)
    numbers = int(sys.argv[1])

    for number, result in enumerate(fib()):
        # print(f"第 {number+1} 次计算的结果是 {result}")
        if number == numbers-1:
            break

    print(f"第{numbers} 次计算的结果是 {result}")

"""
在调用基于 generator 的执行体的时候，注意到不能够用简单的函数方式进行调用，
用函数方式得到的是一个对象，而不是对象的执行。

需要使用 next(generator) 的方式来调用，或者在可以使用 iterator 的地方来使用
生成器。

"""
