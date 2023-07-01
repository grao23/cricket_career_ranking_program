#cricket player test match
bowlers = []

def bowler_grade(bowlers):
    wickets =  bowlers['wickets']
    economy = bowlers['economy']
    strike_rate = bowlers['strike rate']
    average = bowlers['average']
    four_wicket_haul  = bowlers['four wicket haul']
    five_wicket_haul  = bowlers['five wicket haul']
    ten_for_match = bowlers['ten for match']

    if wickets >= 600: 
        wickets = 30 * 1
    elif wickets >= 500 and wickets < 600 : 
        wickets = 30 * 0.80
    elif wickets >= 400 and wickets < 500 : 
        wickets = 30 * 0.65
    elif wickets >= 300 and wickets < 400 : 
        wickets = 30 * 0.50
    elif wickets >= 200 and wickets < 300: 
        wickets = 30 * 0.37
    elif wickets >= 150 and wickets < 200: 
        wickets = 30 * 0.30 
    elif wickets >= 75 and wickets < 150:
        wickets = wickets * 0.15
    else:
        wickets = 30 * 0.08

    if economy == 3.00: 
        economy = 20 * 0.70
    elif economy <= 2.50 and economy >= 2.00: 
        economy = 20 * 1
    elif economy <= 2.99 and economy >= 2.50: 
        economy = 20 * 0.80
    elif economy >= 3.01 and economy < 3.50: 
        economy = 20 * 0.55
    elif economy >= 3.50 and economy < 4.00: 
        economy = 20 * 0.35
    else:
        economy = 20 * 0.15

    
    if strike_rate <= 40.00: 
        strike_rate = 25 * 1
    elif strike_rate >= 40.00 and strike_rate <= 50.00 : 
        strike_rate = 25 * 0.75
    elif strike_rate >= 50.00 and strike_rate <= 60.00 : 
        strike_rate = 25 * 0.55
    elif strike_rate >= 60.00 and strike_rate <= 70.00 : 
        strike_rate = 25 * 0.30
    else:
        strike_rate = 25 * 0.15


    if average <= 10.00: 
        average = 25 * 1
    elif average >= 10.00 and average <=20.00 : 
        average = 25 * 0.80
    elif average >= 20.00 and average < 25.00 : 
        average = 25 * 0.70
    elif average >= 25.00 and average < 30.00: 
        average = 25 * 0.60
    elif average >= 30.00 and average < 40.00 : 
        average = 25 * 0.43
    elif average >= 40.00 and average < 50.00: 
        average = 25 * 0.25
    else:
        average = 25 * 0.10

    bowlers_grade = ((wickets) + (economy) + (strike_rate) + (average) + ( four_wicket_haul * 0.05) + (five_wicket_haul * 0.05) + (ten_for_match * 0.10))

    return bowlers_grade

def input_bowler_data():
    bowl= {}
    bowl['wickets'] = int(input("Enter bowlers career wickets: "))
    bowl['economy'] = float(input("Enter bowlers career economy: "))
    bowl['average'] = float(input("Enter bowlers career average: "))
    bowl['strike rate'] = float(input("Enter bowlers career strike rate: "))
    bowl['four wicket haul'] = int(input("Enter bowlers career 4 wicket hauls: "))
    bowl['five wicket haul'] = int(input("Enter bowlers career 5 wicket hauls "))
    bowl['ten for match'] = int(input("Enter bowlers career 10 wickets taken in a test match: "))
    bowl['bowlers_grade'] = bowler_grade(bowl)

    return bowl

# Function to rank bowlers
def rank_bowlers():
    ranked_bowlers = sorted(bowlers, key=lambda x: x['bowlers_grade'], reverse=True)
    print("\nBowlers Ranked by bowler Grade:")
    for i, bowl in enumerate(ranked_bowlers, 1):
        print(f"{i}. Bowler: {bowl['name']}, Offical Grade: {bowl['bowlers_grade']:.2f}/100")

# Main program loop
while True:
    choice = input("\nEnter '1' to input a new bowler, '2' to rank bowlers, or '3' to exit: ")
    
    if choice == '1':
        bowl = input_bowler_data()
        bowl['name'] = input("Enter bowlers's name: ")
        bowlers.append(bowl)
    elif choice == '2':
        rank_bowlers()
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")