#الجزء الاول
def padel_court_cost(court_type):
    if court_type == 'indoor':
        return 30
    elif court_type == 'outdoor':
        return 20
     
#الجزء الثاني
def rackets_costs(racket_brand):
    if racket_brand == 'bullpadel':
        return 100
    elif racket_brand == 'nox':
        return 140
    elif racket_brand == 'siux':
        return 200

#الجزء الثالث
def padel_balls_cost(ball_boxes):
    if ball_boxes == 1:
        return 2
    elif ball_boxes == 2:
        return 3.5
    elif ball_boxes == 3:
        return 5
    
#الجزء الرابع
def padel_game_cost():
    court_type = input('would you like an indoor court or outdoor? ')
    racket_brand = input('racket brand options (bullpadel/nox/sius) please choose 1 ')
    ball_box = int(input('how many ball boxes do you need? (max :3) '))
    cost = padel_court_cost(court_type) + rackets_costs(racket_brand) + padel_balls_cost(ball_box)
    return cost

print(padel_game_cost())


    
