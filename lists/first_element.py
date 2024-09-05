def first(list):
    if not list:
        return 'Please enter a valid list'

    return list[-1]

print(first(['Earth', 'Moon', 'Mars']))  # Earth