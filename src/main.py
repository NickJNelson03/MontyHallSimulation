import numpy as np
import matplotlib.pyplot as plt

def simulation(trials):

    stay_wins = 0
    switch_wins = 0

    car_apperances = {}

    for _ in range(trials):
        doors = ["goat", "car", "goat"]

        n = len(doors)

        np.random.shuffle(doors)

        car_location = doors.index("car") + 1 # The +1 allows it to align door 1,2,3 appropriately
        car_apperances[car_location] = 1 + car_apperances.get(car_location, 0)

        user_choice = np.random.randint(0,3)

        selective_door = [door for door in range(n) if doors[door] == "goat" and door != user_choice]

        host_choice = np.random.choice(selective_door)

        # Our assumption is that if you switch doors everytime, you'll have a 1/3 higher expectation than if you stay.

        switch_door = [switch for switch in range(n) if switch != user_choice and switch != host_choice][0]

        if doors[switch_door] == "car":
           switch_wins +=1 
        else:
            stay_wins +=1 
        

    return stay_wins, switch_wins, car_apperances

def win_percentage(wins, trials):

    return (wins / trials) * 100


def main():

    trials = 1000 # Law of large numbers says as you increase the trials, the sample average will converge to the theoretical probability

    stay_wins, switch_wins, car_tracker = simulation(trials) 

    
    winning_percentage = [win_percentage(stay_wins, trials), win_percentage(switch_wins, trials)]
    actions = ["Stay", "Switch"]

    # Each door usage
    colors = ["red", "green", 'orange']

    door_number = [f"Door {i}" for i in sorted(car_tracker.keys())]
    data = car_tracker.values()

    plt.figure(figsize=(10,7))
    plt.pie(data, labels = door_number, autopct='%1.1f%%' )
    plt.title("Car Placement Distribution(Across Doors)")
    plt.legend(door_number)
    plt.show()


    # Winning Probability based on the Player Strategy
    plt.bar(actions[0], winning_percentage[0], color="violet")
    plt.bar(actions[1], winning_percentage[1],color = "blue")
    plt.title("Monty Hall Simulation")
    plt.xlabel("Player Strategy")
    plt.ylabel("Winning Percentage")
    plt.show()

    return 

main()