def ft_harvest_total() -> None:
    num1 = int(input("Day 1 harvest: "))
    num2 = int(input("Day 2 harvest: "))
    num3 = int(input("Day 3 harvest: "))
    num1 = num1 + num2 + num3
    print(f"Total harvest: {num1}")
