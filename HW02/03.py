def hanoi(n, src, inter, dest, rods):
    if n > 0:
        hanoi(n - 1, src, dest, inter, rods)

        disk = rods[src].pop()
        rods[dest].append(disk)
        print(f"Перемістити диск з {src} на {dest}: {disk}")
        print(f"Проміжний стан: {rods}")

        hanoi(n - 1, inter, src, dest, rods)

def main():
    try:
        n = int(input("Введіть кількість дисків (n): "))
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Введіть ціле число більше за 0.")
        return
    
    rods = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }

    print(f"Початковий стан: {rods}")
    hanoi(n, 'A', 'B', 'C', rods)
    print(f"Кінцевий стан: {rods}")

if __name__ == '__main__':
    main()