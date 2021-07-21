from random import randint, choice

class Animal:
    def __init__(self, speed, strength, threshold, hunger):
        self.speed = speed
        self.strength = strength
        self.threshold = threshold
        self.hunger = hunger
    
    def hunt(self):
        num = randint(0, 100) - (self.speed/10) - (self.strength/10)
        if (num < 0):
            num = 0
        return num

class Environment:
    creatures = []

    def __init__(self, foodPerCycle):
        self.constant = foodPerCycle
        self.food = foodPerCycle

    def addCreature(self, creature):
        self.creatures.append(creature)
    
    def showData(self):
        total = 0
        speed = 0
        strength = 0
        threshold = 0
        for creature in self.creatures:
            total += 1
            speed += creature.speed
            strength += creature.strength
            threshold += creature.threshold
        
        print("Total Creatures: " + str(total))
        print("Average Speed: " + str(round(speed/total, 2)))
        print("Average Strength: " + str(round(strength/total, 2)))
        print("Average Threshold: " + str(round(threshold/total, 2)))
        print("\n")
    
    def generateHunger(self):
        for creature in self.creatures:
            creature.hunger += 1
    
    def killCreatures(self):
        for creature in self.creatures:
            if (creature.hunger > creature.threshold):
                self.creatures.remove(creature)

    def generateChild(self, animalOne, animalTwo):
        speed = (animalOne.speed + animalTwo.speed/2) + randint(-1, 1)
        strength = (animalOne.strength + animalTwo.strength/2) + randint(-1, 1)
        threshold = (animalOne.threshold + animalTwo.threshold/2)
        if (speed > 5 and threshold > 5):
            speed = .9 * speed
            threshold = threshold / (1 + ((speed - 5)/10))
        if (strength > 5):
            strength = .9 * strength
            threshold = threshold / (1 + ((strength - 5)/10))
        return Animal(speed, strength, threshold, 0)
    
    def reproduce(self):
        indexes = []
        reproduced = 0
        for i in range(len(self.creatures)):
            indexes.append(i)
        
        for index in indexes:
            reproducing = randint(1, 5)
            if (reproducing == 1):
                indexes.remove(index)
                otherCreature = choice(indexes)
                child = self.generateChild(self.creatures[index], self.creatures[otherCreature])
                self.creatures.append(child)
                reproduced += 1
    
    def cycle(self):
        indexes = []
        for i in range(len(self.creatures)):
            indexes.append(i)
        
        self.generateHunger()
        
        while (self.food > 0 and len(indexes) > 0):
            index = choice(indexes)
            indexes.remove(index)
            creature = self.creatures[index]
            if (creature.hunt() <= self.food):
                creature.hunger = 0
                self.food -= 1
    
        self.killCreatures()
        self.food = self.constant
        self.reproduce()

environment = Environment(3)

for i in range(1000):
    environment.addCreature(Animal(randint(1,2), randint(1,2), 3, 0))

environment.showData()

action = input("Cycle [Y/n]: ")

while (action == "Y"):
    environment.cycle()
    if (len(environment.creatures) == 0):
        print("All creatures died")
        break
    environment.showData()
    action = input("Cycle [Y/n]: ")
