zodiac_years = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
m, y = input().split()
m, y = int(m), int(y)
print(zodiac_years[(y + 7 + (m > 1)) % 12]) # (m > 1) --? True == 1, False == 0
