# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ervillca <ervillca@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/10 00:42:26 by ervillca          #+#    #+#              #
#    Updated: 2026/05/10 01:48:21 by ervillca         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    for i in range(days):
        print(f"Day {i+1}")
    print("Harvest time!")
