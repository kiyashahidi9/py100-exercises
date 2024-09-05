weather = input('What kinda weather is it? ')

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print('getcho umbrella')
    case 'windy':
        print('time to get blown away!')
    case 'torrential downpour':
        print('hold on tight!')
    case _:
        print('oh deary me..')