import random

dinner = ""
dinner_restaurants = [
    "Chilis",
    "Millers Ale House",
    "Applebees",
    "Texas Roadhouse",
    "Outback",
    "Mulberry",
    "Dominos",
    "Buffalo Wild Wings",
    "PizzaHut",
    "Wendys",
    "Taco Bell",
    "Mcdonalds",
    "Moes",
    "Chipotle",
    "Fat Boy Burrito", 
    "Chick-Fil-A",
    "Wingstop",
    "Wing Zone",
    "Chicken Carnival",
    "KFC",
    "Boston Market",
    "Zorns",
    "Spanky's Food Factory",
    "Cheesecake Factory",
    "La Botega",
    "San Marzano",
    "Galleria",
    "La Piazza",
    "Panera",
    "Croxley's Ale House",
    
]
breakfast = ""
breakfast_restaurants = [
    "Hatch",
    "IHop",
    "Dunkin Donuts",
    "Brownstone Coffee"
    "Munday's"
    "Tim Hortons"
]
desert = ""
desert_restaurants = [
    "Coldstone",
    "Sonic",
    "Dairy Queen",
    "Carvel",
    "Ralphs",
    "Friendly's"
]
   
def setDinner():
    global dinner_restaurants, dinner
    dinner = random.choice(dinner_restaurants)

def getDinner():
    global dinner
    return dinner

def setBreakfast():
    global breakfast_restaurants, breakfast
    breakfast = random.choice(breakfast_restaurants)

def getBreakfast():
    global breakfast
    return breakfast

def setDesert():
    global desert_restaurants, desert
    desert = random.choice(desert_restaurants)

def getDesert():
    global desert
    return desert
    
