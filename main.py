import random
from random import choice
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 20

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(auto)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
        self.job = Job(option_work)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
        self.satiety += 5
        self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return

        self.money += self.job.salary
        self.gladness += self.job.gladness

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
        self.satiety += 10
        self.home.food -= 10

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 50
            self.car.fuel = 100
        elif manage == "food":
            print("I bought food")
            self.money -= 20
            self.home.food += 20
        elif manage == "delicacies":
            print("I am happy")
            self.money -= 10
            self.gladness += 20
            self.satiety += 2

    def days_indexes(self, day):
        day = f"Today the {day} of {self.name}'s life"
        print(f"{day:-^50}")
        indexes_name = f"{self.name}'s indexes"
        print(f"{indexes_name:-^50}")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:-^50}")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        if self.gladness <= 0:
            print("Depression...")
            return False
        if self.satiety <= 0:
            print("Death...")
            return False
        if self.money <= -100:
            print("Bankrupt")
            return False

    def live(self,day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settle in the house!")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I working {self.job.work} salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1,4)
        if self.satiety < 10:
            print("time to eat")
            self.eat()
        elif self.gladness < 5:
            print("time to chill")
            self.chill()
        elif self.money <= 5:
            print("time to eat")
            self.work()
        elif self.car.strength <= 5:
            print("time to repair")
            self.to_repair()
        if dice == 1:
            print("Time to chill")
            self.chill()
        if dice == 2:
            print("Lets work")
            self.work()
        if dice == 3:
            print("Cleaning home")
            self.clean_home()
        if dice == 4:
            print("I am happy!")
            manage = "delecacies"
            self.shopping(manage)


    def chill(self):
        self.gladness += 10
        self.money -= 50

    def to_repair(self):
        self.car.strength += 5
        self.money -= 10

    def clean_home(self):
        self.home.mess -= 5
        self.gladness += 2


class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Auto:
    def __init__(self, auto):
        self.brand = choice(list(auto))
        self.fuel = auto[self.brand]["fuel"]
        self.strength = auto[self.brand]["strength"]
        self.consumption = auto[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False


class Job:
    def __init__(self, option_work):
        self.work = choice(list(option_work))
        self.salary = option_work[self.work]['salary']
        self.gladness = option_work[self.work]['gladness']


option_work = {"Developer C++": {"salary": 50, 'gladness': 10},
               "Developer Python": {"salary": 40, 'gladness': 20}, }

auto = {"BMW": {"fuel": 50, "strength": 100, "consumption": 18},
        "OPEL": {"fuel": 30, "strength": 60, "consumption": 12},
        "FORD": {"fuel": 35, "strength": 80, "consumption": 10}, }

nick = Human("Nick")
for day in range(1,366):
    if nick.live(day) == False:
        break
