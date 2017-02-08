"""
Utils
"""

def convert_number_to_text(number):
    number = split_number(number)
    number_spelled = []
    for i, n in enumerate(number):
        number_spelled.insert(0, spell_number(n, i * 3))
    return ' '.join(list(filter(None, number_spelled)))


def spell_number(number, power):
    number = number.zfill(3)
    number_spelled = [
        get_hundreth_number_spelling(int(number[0]) * 100),
        get_tenth_number_spelling(number[1:]),
        get_power_name(power, int(number))
    ]
    return ' '.join(list(filter(None, number_spelled)))


def split_number(number):
    kilos = []
    while number:
        kilos.append(number[-3:])
        number = number[:-3] if len(number) > 2 else ''
    return kilos


def get_power_name(power, number):
    if not power or not number:
        return None
    power_str = {
        3: ('tysiąc', 'tysiące', 'tysięcy'),
        6: ('milion', 'miliony', 'milionów'),
        9: ('miliard', 'miliardy', 'miliardów'),
        12: ('bilion', 'biliony', 'bilionów'),
        15: ('biliard', 'biliardy', 'biliardów'),
        18: ('trylion', 'tryliony', 'trylionów'),
        21: ('tryliard', 'tryliardy', 'tryliardów')
    }.get(power)
    if number == 1:
        return power_str[0]
    last_digit = int(str(number)[-1])
    if last_digit >= 2 and last_digit <= 4:
        return power_str[1]
    return power_str[2]


def get_single_number_spelling(number):
    return {
        1: 'jeden',
        2: 'dwa',
        3: 'trzy',
        4: 'cztery',
        5: 'pięć',
        6: 'sześć',
        7: 'siedem',
        8: 'osiem',
        9: 'dziewięć'
    }.get(int(number))


def get_tenth_number_spelling(number):
    if number[0] == '0':
        return get_single_number_spelling(number)
    if int(number[0]) == 1:
        return {
            10: 'dziesięć',
            11: 'jedenaście',
            12: 'dwanaście',
            13: 'trzynaście',
            14: 'czternaście',
            15: 'piętnaście',
            16: 'szesnaście',
            17: 'siedemnaście',
            18: 'osiemnaście',
            19: 'dziewiętnaście'
        }.get(int(number))

    tenth_number = {
        20: 'dwadzieścia',
        30: 'trzydzieści',
        40: 'czterdzieści',
        50: 'pięćdziesiąt',
        60: 'sześćdziesiąt',
        70: 'siedemdziesiąt',
        80: 'osiemdziesiąt',
        90: 'dziewięćdziesiąt'
    }.get(int(number[0]) * 10)
    if int(number[1]) == 0:
        return tenth_number
    return ' '.join([
        tenth_number,
        get_single_number_spelling(int(number[1]))
    ])


def get_hundreth_number_spelling(number):
    return {
        100: 'sto',
        200: 'dwieście',
        300: 'trzysta',
        400: 'czterysta',
        500: 'pięćset',
        600: 'sześćset',
        700: 'siedemset',
        800: 'osiemset',
        900: 'dźiewięćset',
    }.get(int(number))