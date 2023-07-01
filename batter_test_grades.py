batters = []

def batting_grade(bat): 
    runs = bat['runs']
    average = bat['average']
    ducks = bat['ducks']
    fifty = bat['fifty']
    hundred = bat['hundred']
    sr = bat['strike rate']
    double_hundred = bat['double hundred']

    # Calculate grade based on runs
    if runs >= 10000: 
        runs = 30 * 1
    elif runs >= 8000 and runs < 10000: 
        runs = 30 * 0.90
    elif runs >= 6000 and runs < 8000: 
        runs = 30 * 0.65
    elif runs >= 4000 and runs < 6000: 
        runs = 30 * 0.50
    elif runs >= 2000 and runs < 4000:
        runs = 30 * 0.35
    elif runs >= 1000 and runs < 2000: 
        runs = 30 * 0.15
    else: 
        runs = 30 * 0.05

    # Calculate grade based on strike rate
    if sr >= 90.00: 
        sr = 20 * 1
    elif sr >= 80.00 and sr < 90.00: 
        sr = 20 * 0.92
    elif sr >= 70.00 and sr < 80.00: 
        sr = 20 * 0.78
    elif sr >= 60.00 and sr < 70.00: 
        sr = 20 * 0.63
    elif sr >= 50.00 and sr < 60.00: 
        sr = 20 * 0.50
    elif sr >= 40.00 and sr < 50.00: 
        sr = 20 * 0.45
    elif sr >= 30.00 and sr < 40.00: 
        sr = 20 * 0.20
    else: 
        sr = 20 * 0.1
    
    # calculate the average of batter

    if average >= 50.00: 
        average = 30 * 1
    elif average >= 45.00 and average < 50.00: 
        average = 30 * 0.88
    elif average >= 40.00 and average < 45.00: 
        average = 30 * 0.72
    elif average >= 35.00 and average < 40.00: 
        average = 30 * 0.58
    elif average >= 30.00 and average < 35.00: 
        average = 30 * 0.48
    elif average >= 25.00 and average < 30.00: 
        average = 30 * 0.28
    elif average >= 20.00 and average < 25.00: 
        average = 30 * 0.15
    else: 
        average = 30 * 0.05

    # Calculate the batter's grade
    batters_grade = runs + average + sr - (ducks * 0.07) + (fifty * 0.05) + (hundred * 0.10) + (double_hundred * 0.15)
    
    return batters_grade


def input_batter_data():
    bat = {}
    bat['runs'] = int(input("Enter batter's career runs: "))
    bat['average'] = float(input("Enter batter's career average: "))
    bat['strike rate'] = float(input("Enter batter's career strike rate: "))
    bat['ducks'] = int(input("Enter batter's career ducks: "))
    bat['fifty'] = int(input("Enter batter's career fifties: "))
    bat['hundred'] = int(input("Enter batter's career hundreds: "))
    bat['double hundred'] = int(input("Enter batter's career double hundreds: "))
    bat['batters_grade'] = batting_grade(bat)

    return bat


# Function to rank batters
def rank_batters():
    ranked_batters = sorted(batters, key=lambda x: x['batters_grade'], reverse=True)
    print("\nBatters Ranked by Batter Grade:")
    for i, bat in enumerate(ranked_batters, 1):
        print(f"{i}. Batter: {bat['name']}, Official Grade: {bat['batters_grade']:.2f}/100")


# Main program loop
while True:
    choice = input("\nEnter '1' to input a new batter, '2' to rank batters, or '3' to exit: ")
    if choice == '1':
        bat = input_batter_data()
        bat['name'] = input("Enter batter's name: ")
        batters.append(bat)
    elif choice == '2':
        rank_batters()
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")