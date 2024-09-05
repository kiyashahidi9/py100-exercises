def greet(country):
    match country:
        case 'en':
            return 'Hi!'
        case 'fr':
            print('Salut!')

print(greet('en'))