"""汉诺塔
"""

def move(first, second, third, n):
    if n == 1:
        print(f"{first} -> {third}")
    else:
        move(first, third, second, n-1)
        print(f"{first} -> {third}")
        move(second, first, third, n-1)


if __name__ == '__main__':
    move('A', 'B', 'C', 20)
