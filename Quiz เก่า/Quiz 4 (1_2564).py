D, M = input().split("/")
D = int(D); M = int(M)
if(D >= 21 and M == 3) or (D <= 19 and M == 4):
    print("Aries")
if(D >= 20 and M == 4) or (D <= 20 and M == 5):
    print("Taurus")  
if(D >= 21 and M == 5) or (D <= 21 and M == 6):
    print("Gemini")
if(D >= 22 and M == 6) or (D <= 22 and M == 7):
    print("Cancer")
if(D >= 23 and M == 7) or (D <= 22 and M == 8):
    print("Leo")  
if(D >= 23 and M == 8) or (D <= 22 and M == 9):
    print("Virgo")   
if(D >= 23 and M == 9) or (D <= 23 and M == 10):
    print("Libra")   
if(D >= 24 and M == 10) or (D <= 21 and M == 11):
    print("Scorpius")   
if(D >= 22 and M == 11) or (D <= 21 and M == 12):
    print("Sagittarius")  
if(D >= 22 and M == 12) or (D <= 19 and M == 1):
    print("Capricornus")  
if(D >= 20 and M == 1) or (D <= 18 and M == 2):
    print("Aquarius")
if(D >= 19 and M == 2) or (D <= 20 and M == 3):
    print("Pisces")
