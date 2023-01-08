'''
Projekt 1.py = první projet do Engeto

author = Daniela Horucková
email = horuckova.d@seznam.cz
discord = LuckyDany#2774
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Vyžádá si od uživatele přihlašovací jméno a heslo

user_name = input("User name: ")
password = input ("Password: ")
delimiter =  "-" * 40
print(delimiter)

# zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů

registered_users = {"user": "password", "bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

registered = user_name in registered_users and password == registered_users[user_name]

# pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty

if registered:
    print("Welcome to the app, " + user_name + "! \nWe have 3 texts to be analyzed.")

# pokud není registrovaný, upozorni jej a ukonči program

else:
    print("Sorry, you are unregistered user. Terminating the program!")
    quit()

print(delimiter)

# Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS

number = input("Enter a number btw. 1 and 3 to select: ")

# Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí

if number.isnumeric() and len(number) == 1:
    number = int(number)
    if number < 1 or number > 3:
        print("You input a wrong number. Terminating the program!")
        quit()   

# pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí 

else:
    print("Your input must be a number. Terminating the program!")
    quit()

print(delimiter)

# Pro vybraný text spočítá následující statistiky:

choise = (TEXTS[number - 1])
choise = choise.replace("-", " ")
words = choise.split() 

clean_words = list()

for clean in words:
    clean_words.append(clean.strip(",.:;@/"))

#     počet slov


print(f"There are {len(clean_words)} words in the selected text.")


#     počet slov začínajících velkým písmenem,

titlecase = 0
for title in clean_words:
    if title[0].isupper():
        titlecase = titlecase + 1
print(f"There are {titlecase} titlecase words.")

#     počet slov psaných velkými písmeny,

uppercase = 0
for upper in clean_words:
    if upper.isupper() and upper.isalpha():
        uppercase = uppercase + 1
print(f"There are {uppercase} uppercase words.")

#     počet slov psaných malými písmeny,

lowercase = 0
for lower in clean_words:
    if lower.islower():
        lowercase = lowercase + 1
print(f"There are {lowercase} lowercase words.")

#     počet čísel (ne cifer),

numeric = 0
for num in clean_words:
    if num.isnumeric():
        numeric = numeric + 1
print(f"There are {numeric} numeric strings.")

#     sumu všech čísel (ne cifer) v textu.

suma = 0
for numbers in clean_words:
    if numbers.isnumeric():
        suma = suma + int(numbers)
        
print(f"The sum of all the numbers {suma}.")
print(delimiter)

# Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. 

length = list()

for delka in clean_words:
    length.append(len(delka))

occurrences = {}

for number in length:
    if number not in occurrences:
        occurrences[number] = 1
    else:
        occurrences[number] = occurrences[number] + 1

result = list()
for x in occurrences:
    result.append((x, occurrences[x]))

# vytisk vysledku

max_star = (sorted(occurrences.values())[-1])

print("LEN|","OCCURENCES".ljust(max_star-2),"|NR.")
print(delimiter)

for number in sorted(result):
    stars = "*" * (number[1])
    print(f"{str(number[0]).rjust(3)}|{stars.ljust(max_star)}|{number[1]}")
print(delimiter)
