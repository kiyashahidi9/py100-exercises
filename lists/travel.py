destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(city, cities):
    for place in cities:
        if place == city:
            return True

    return False

print(contains('Barcelona', destinations))
print(contains('Nashville', destinations))