# الجزء الأول
def PADEL_COURT_COST(COUTR_TYPE):
    if COUTR_TYPE == "INDOOR":
        return 30
    else:
        return 20

# الجزء الثاني
def RACKETS_COST(RACKET_BRAND):
    if RACKET_BRAND == "BULL PADEL":
        return 100
    elif RACKET_BRAND == "NOX":
        return 140
    else:
        return 200

# الجزء الثالث
def padel_balls_cost(ball_boxes):
    if ball_boxes ==1:
        return 2
    elif ball_boxes ==2:
        return 3.5
    else:
        return 5

#الجزء الرابع 
def padel_game_cost(): 
    COURT_TYPE = (input("the court type"))
    racket_brand = (input("racket_brand"))
    ball_boxes = (int(input("ball_boxes")))
    result=(PADEL_COURT_COST(COURT_TYPE)+RACKETS_COST( racket_brand )+padel_balls_cost(ball_boxes))
    return result

print(padel_game_cost())



    

