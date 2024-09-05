def local_greet(locale):
    language = locale.split('_')[0]
    dialect = locale.split('.')[0].split('_')[1]

    match language:
        case 'en':
            return detect_dialect(dialect)
        case 'fr':
            return 'Salut!'

def detect_dialect(country):
    match country:
        case 'US':
            return "Hey!"
        case 'GB': 
            return "Hello!"
        case 'AU':
            return "Howdy!"
        

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!