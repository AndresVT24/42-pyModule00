# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ervillca <ervillca@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/10 01:38:54 by ervillca          #+#    #+#              #
#    Updated: 2026/05/10 01:41:03 by ervillca         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def print_day(current: int) -> None:
        if current > days:
            return
        print(f"Day {current}")
        print_day(current + 1)

    print_day(1)
    print("Harvest time!")
