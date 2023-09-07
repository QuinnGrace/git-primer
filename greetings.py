from datetime import datetime

name = input("What is your name? ")
hour = datetime.now().time().hour
greeting = (
    if 4 <= hour < 12:
        "Good morning"
    elif 12 <= hour < 16:
        "Good afternoon"
    else:
        "Good night"
)
print(f"{greeting}, {name}!")
