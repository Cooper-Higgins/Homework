users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
jonathan_twitter = users["Jonathan"]["twitter"]
print (jonathan_twitter)

# 2. Get Erik's hometown
erik_hometown = users["Erik"]["home_town"]
print (erik_hometown)

# 3. Get the list of Erik's lottery numbers
erik_lottery = users["Erik"]["lottery_numbers"]
print (erik_lottery)

# 4. Get the species of Avril's pet Monty
avril_pet_species = users["Avril"]["pets"][0]["species"]
print (avril_pet_species)

# 5. Get the smallest of Erik's lottery numbers
erik_lottery = users["Erik"]["lottery_numbers"]
erik_lottery.sort()
print(erik_lottery[0])

# 6. Return a list of Avril's lottery numbers that are even
avril_lottery = users["Avril"]["lottery_numbers"]
even_avril_lottery = []

for number in avril_lottery: 
    if(number % 2 == 0):
      even_avril_lottery.append(number)
print(even_avril_lottery)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
erik_lottery.append(7)
print(erik_lottery)

# 8. Change Erik's hometown to Edinburgh
erik_home_town = users["Erik"]["home_town"]
erik_home_town = "Edinburgh"
print(erik_home_town)

# 9. Add a pet dog to Erik called "fluffy"
erik_pets = users["Erik"]["pets"]
erik_pets.append({"species: dog, name: fluffy"})
print (erik_pets)

# 10. Add another person to the users dictionary
jane = {"name": "jane", 
        "twitter": "janedoe", 
        "home_town": "wick"}
print(jane)