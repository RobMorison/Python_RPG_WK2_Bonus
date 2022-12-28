# As a developer, I want to make at least five commits on GitHub with descriptive messages.  
# As a user, I want an engaging story to be told using print() statements.  
# As a user, I want Hercules (and each enemy), to have health, attack power, and a List of attack names saved in a Dictionary. 
# As a user, I want the ability to select Hercules’ attack using a menu prompt.  
# As a user, I want the foe’s attack to be chosen at random. 
# As a user, I want the results of each attack to be logged in the terminal. 
# As a developer, I want to use an Attack() function that will terminate when Hercules or an enemy’s health reaches zero.   
# As a developer, I want my RunGame() function to call my other functions in a logical order that will determine game flow.  
# As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!  


restaurants = {
                #"Key" : "Value"
                "Boston": ["Sorellina", "Toro", "Ostra", "Stockyard"],
                "New York" : ["Del Frisco's", "Per Se", "Cote", "Gramercy Tavern"],
                "New Haven" : ["Zinc", "Consiglio's", "Prime 16", "Olea"],
                "Hartford" : ["Republic at The Linden", "The Capital Grille", "Feng Chophouse", "Sorella"],
                "Albany" : ["Barcelona", "Black & Blue Steak and Crab", "Grappa '72", "Athos"]
              }

destination = "New York"
print(f"What are the restaurants in {destination}?")
print(restaurants [destination])

import random

attacks = {
              "Hercules" : ["attack from above", "super human strength", "fists of fury"],
              "Nemean" : ["lions bite", "paws of death", "lions strength"],
              "Leraean Hydra" : ["nine-head attach", "water blaster", "head strangler"],
              "Cerberus" : ["dog bite", "mauler", "dragged to the underworld"]
}


print(attacks["Hercules"][-1])

print(f"Hercules attacked with", (attacks["Hercules"][1]))

print("Hercules attacks with")
user_choice = input(f"select attack") (attacks["Hercules"])
if user_choice = 
           

hercules_health = 100
nemean_health = 100
lernaean_hydra_health = 100
cerberus_health = 100

hercules_attack_power = random.randint(1, 10)
nemean_attack_power = random.randint(1, 5)
lernaean_attack_power = random.randint(1, 5)
cerberus_attack_power = random.randint(1,5)



