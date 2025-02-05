def round_ans(val):
    """
    Rounds the answer to the nearest whole number
    :param val: Number to be rounded
    :return: Rounded number
    """
    var_rounded = (val * 2 + 1) // 2
    return f"{var_rounded:.0f}"


def to_celsius(to_convert):
    """
    Converts Fahrenheit to Celsius
    :param to_convert: Number to be converted
    :return: Converted number
    """
    ans = (to_convert - 32) * 5 / 9
    return round_ans(ans)


def to_fahrenheit(to_convert):
    """
    Converts Celsius to Fahrenheit
    :param to_convert: Number to be converted
    :return: Converted number
    """
    ans = to_convert * 1.8 + 32
    return round_ans(ans)


# # Main Routine / testing starts here
# to_c_test = [0, 100, -459]
# to_f_test = [0, 100, 40, -273]

# for item in to_f_test:
#     ans = to_fahrenheit(item)
#     print(f"{item}°C is {ans}°F")

# print()

# for item in to_c_test:
#     ans = to_celsius(item)
#     print(f"{item}°F is {ans}°C")
