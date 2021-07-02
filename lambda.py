people = [
    {"name": "Kevin", "house": "ranch"},
    {"name": "Tom", "house": "Two Story"},
    {"name": "Jason", "house": "Mid-Century"}
]

#def f(person):
#    return person["name"]

people.sort(key=lambda person: person["house"])

print(people)