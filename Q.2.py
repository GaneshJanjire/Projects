import re


def get_age(address):
    age = re.search(r'agedabout (\d+) years', address)
    if age:
        return int(age.group(1))

    age = re.search(r'age (\d+)yrs', address)
    if age:
        return int(age.group(1))

    age = re.search(r'aged about (\d+),', address)
    if age:
        return int(age.group(1))

    age = re.search(r'(\d+)yrs,', address)
    if age:
        return int(age.group(1))

    age = re.search(r'age(\d+),', address)
    if age:
        return int(age.group(1))

    return None


addresses = [
    "13/35 agedabout 60 years, residing at D.NO 59 Eswaran Koil St",
    "16th street R.Kesavan age 46yrs, residing at D.NO 59 Eswaran Koil St",
    "Room no 43 R.Kesavan aged about 37 years, residing at D.NO 59 Eswaran Koil St",
    "Door no 32 R.Kesavan 56yrs, residing at D.NO 59 Eswaran Koil St",
    "12-4-67 , R.Kesavan aged about 61, residing at D.NO 59 Eswaran Koil St",
    "R.Kesavan age63, residing at D.NO 59 Eswaran Koil St",
    "R.Kesavan aged 9, residing at D.NO 59 Eswaran Koil St",
]

expected_outputs = [60, 46, 37, 56, 61, 63, 9]

for i, address in enumerate(addresses):
    output = get_age(address)
    print(f'Example {i + 1}: {output} {"Correct" if output == expected_outputs[i] else "Incorrect"}')