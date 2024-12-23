a = 5 == 5 #true,რადგან 5 ტოლია 5-ს.
print(a)

b = 10 != 20 #true, რადგან 10 არ არის ტოლი 20-ზე.
print(b)

c = 4 > 3 and 2 < 5 #true, რადგან ორივე პირობა სწორია.
print(c)

d = 10 > 20 or 5 < 8 #true, რადგან ერთი პირობა მაინც სწორია.
print(d)

e = not (7 > 3) #false, not გვიბრუნებს საპირისპიროს.
print(e)

f = "hello" == "world" #false,რადგან hello არ არის ტოლი world-ის.
print(f)

g = 15 >= 10 #true, რადგან 15 მეტია ან ტოლია 10-ზე .
print(g)

h = 8 <= 8 #true, რადგან 8 = 8-ზე.
print(h)

i = 3 > 1 and 2 == 2 and 4 != 5 #true, რადგან ყველა პირობა სწორია.
print(i)

j = not (10 < 5 or 2 == 2) #false, რადგან (10 < 5 ან 2 == 2) სწორი, მაგრამ not აბრუნებს საპირისპიროს.
print(j)
