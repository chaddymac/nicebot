intro = input("Hi! My name is NiceBot, What is your name? ")



begin = input(f"Hi {intro}! Nice to meet you. How are you today? ").lower()

with open('badday.txt') as f:
    if begin in f.read():
        print("I hope your day gets better")
    else:
        print("Great!")
