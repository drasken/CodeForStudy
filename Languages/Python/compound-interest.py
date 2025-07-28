"""
Usefult to me to calculate compounf interest
"""


def compound_interest(init_sum: float, interest: float, years: int) -> float:
    "return simple compound interest without additional deposits"

    return round(init_sum * ((1 + interest) ** years), 2)


def compound_with_deposit(init_sum: float, interest: float, years: int, deposit: float) -> float:

    if years <= 1:
        return round((init_sum + deposit) * (1 + interest), 2)
    else:
        new_sum = round((init_sum + deposit) * (1 + interest), 2)
        return compound_with_deposit(new_sum, interest, years - 1, deposit)

# test = compound_with_deposit(1000, 0.05, 10, 200)
# print(test)

def compound_with_DP(init_sum, interest, years, deposit):

    res = [0 for x in range (years + 1)]

    for index, el in enumerate(res):
        if index == 0:
            res[index] = init_sum
        else:
            res[index] = round((res[index - 1] + deposit) * (1 + interest), 2)
    return res


# compound_with_DP(1000, 0.05, 10, 200)
