def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def print_day(current: int) -> None:
        if current > days:
            return
        print(f"Day {current}")
        print_day(current + 1)

    print_day(1)
    print("Harvest time!")
