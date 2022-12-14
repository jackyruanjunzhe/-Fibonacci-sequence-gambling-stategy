import random

walk_in_casino = 0
money_total = 0
rich_time = 0
while walk_in_casino <= 100000:

    money = 10000
    bet_time = 1
    win_inarow = 0
    bet_1 = 200
    bet_2 = 500
    bet_3 = 300
    bet_4 = 800
    while bet_time <= 300 and money >= 5000 :

        win_range = random.random()  #if win_rage<= 0.5, then we win in gamble

        lose_bet = 1
        if win_range <= 0.499:
            money += bet_1
            win_range =  random.random()

            lose_bet = 2
            if win_range <= 0.499:
                money +=  bet_2
                win_range =  random.random()

                lose_bet = 3
                if win_range <= 0.499:
                    money += bet_3
                    win_range = random.random()

                    lose_bet = 4
                    if win_range <= 0.499:
                        money += bet_4
                        lose_bet = "no lose bet, win all 4"
                    else:
                       money -= bet_4
                       bet_time += 1
                else:
                     money -= bet_3
                     bet_time += 1
            else:
                money -= bet_2
                bet_time += 1



        else:
            money -= bet_1
            bet_time +=1


    print("your final money is ",  money , "you bet" , bet_time, "times")
    if money >= 70000:
        rich_time += 1
    walk_in_casino += 1
    money_total += money
expect_value = money_total / 100000
print("your expect_value is ", expect_value, "money above 70000 time is ", rich_time)
