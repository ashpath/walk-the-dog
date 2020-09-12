__author__ = 'Victoria'

#Classes for implementation of Seasons, Encounters
import random

#Define an object to hold information about seasons. This includes what the season is, temperature, and weather.
class Season(object):
    def __init__(self, timeofyear, weather, temperature):
        self.timeofyear = timeofyear
        self.weather = weather
        self.temperature = temperature

    #Set the season. Rooms will gain certain properties based on season.
    #Spring: More random encounters with things like birds & garbage.
    #Summer: More people at the park. Its too hot to wear your coat. I recommend using shorts.
    #Fall: Leaves on the ground. More random encounters with things like sticks and wasps.
    #Winter: Snow! Don't leave without your coat & scarf, its cold outside. Save your shorts for summer.
    def gen_season(self):
        random.seed(None)
        random_num = random.randint(1, 4)

        if random_num == 1:
            self.timeofyear = 'spring'
        elif random_num == 2:
            self.timeofyear = 'summer'
        elif random_num == 3:
            self.timeofyear = 'fall'
        else:
            self.timeofyear = 'winter'

        return self.timeofyear

    #Determine the ambient temperature. This is used to determine the best clothing to wear.
    def get_temp(self):
        if self.timeofyear == 'spring':
            self.temperature = 'warm'
        elif self.timeofyear == 'summer':
            self.temperature = 'hot'
        elif self.timeofyear == 'fall':
            self.temperature = 'cool'
        else:
            self.temperature = 'cold'

        return self.temperature

    #Randomly generates some weather based on the season.
    def gen_weather(self):
        random.seed(None)
        random_num = random.randint(1, 3)

        if self.timeofyear == 'spring':
            if random_num == 1:
                self.weather = 'rain'
            elif random_num == 2:
                self.weather = 'overcast'
            else:
                self.weather = 'sunny'
        elif self.timeofyear == 'summer':
            if random_num == 1:
                self.weather = 'rain'
            else:
                self.weather = 'sunny'
        elif self.timeofyear == 'fall':
            if random_num == 1:
                self.weather = 'windy'
            elif random_num == 2:
                self.weather = 'fog'
            else:
                self.weather = 'overcast'
        else:
            if random_num == 1:
                self.weather = 'lightsnow'
            elif random_num == 2:
                self.weather = 'blizzard'
            else:
                self.weather = 'overcast'

        return self.weather

#Create a class to handle encounters.
class Encounters(Season):
    #Inherit data about the season for encounter rates & types of encounters.
    def __init__(self, timeofyear, weather, temperature, humans, dog_walkers, strays, cats):
        super(Encounters, self).__init__(timeofyear, weather, temperature)
        self.humans = humans
        self.dog_walkers = dog_walkers
        self.strays = strays
        self.cats = cats

    #How many people will you encounter while outside? Randomly select a number. Higher in Summer, lower
    #in Winter. There is a chance for 0 people in winter because its cold, and strays are more likely to be out looking
    #for food.
    def gen_enc_values(self):
        random.seed(None)
        #its hot
        if self.timeofyear == 'summer':
            self.humans = random.randint(3, 5)
            self.dog_walkers = random.randint(1, 6)
            self.cats = random.randint(2, 5)
            #Compare the values to return number of strays (dogs without a human).
            if self.dog_walkers > self.humans:
                self.strays = self.dog_walkers - self.humans
                self.dog_walkers = self.dog_walkers - self.strays
            else:
                self.strays = 0
        #its cold
        elif self.timeofyear == 'winter':
            self.humans = random.randint(0, 2)
            self.dog_walkers = random.randint(0, 5)
            self.cats = random.randint(0, 3)
            if self.dog_walkers > self.humans:
                self.strays = self.dog_walkers - self.humans
                self.dog_walkers = self.dog_walkers - self.strays
            else:
                self.strays = 0
        #its reasonable. Fall and spring have the same encounter list.
        else:
            self.humans = random.randint(1, 3)
            self.dog_walkers = random.randint(0, 3)
            self.cats = random.randint(1, 3)
            if self.dog_walkers > self.humans:
                self.strays = self.dog_walkers - self.humans
                self.dog_walkers = self.dog_walkers - self.strays
            else:
                self.strays = 0