from random import randint, choice
#from prime import isPrime

print("your computer will create a small population of creatures. It will they show the data for the creatures below. Eventually the population will die or become very sucessful. ")

class dinoSquirrel:
  def __init__(self, speed, intelligence, strength, camo, claws, teeth, size, name,age, gender, carrier, live):
    self.name = name
    self.speed = speed
    self.intelligence = intelligence
    self.strength = strength
    self.camo = camo
    #their ability to camoflage with the surroundings
    self.claws = claws
    #whether they have teeth or not
    self.teeth = teeth
    #whether they have teeth or not
    self.size = size
    self.age = age
    #self.lifespan = lifespan
    self.gender = gender
    self.carrier = carrier
    foo = (int(camo)*20+randint(1,20))+ (intelligence*6)+(speed*4)
    if foo < 100:
      self.live = foo
    else:
      self.live = foo - ((foo%100)+10)
    #whether they are a disease carrier or not
    '''def __calcLife__():
      return randint(10, 20) + (self.speed/3) + (self.strength)/5 + (self.intelligence)/3 + (self.size/3)
    lifespan = __calcLife__()'''

#a more flexible yet slower version of the randint function
def Xrand(num, greater):
  if num > greater:
    return randint(greater, num)
  if num == greater:
    return num
  if num < greater:
    return randint(num, greater)
  
#the code to reproduce
def reproduce(creatures):
  #pretty self explanatory
  males = []
  females = []
  for i in range(len(creatures)):
    if creatures[i].gender == "Female":
      females.append(creatures[i])
    if creatures[i].gender == "Male":
      males.append(creatures[i])
  notPregnant = females
  offspring = []
  if len(males) == 0 or len(females) == 0:
    print("Not enough males or females to reproduce, enter god mode to continue")
    quit()
  while len(notPregnant) > 0:
    father = choice(males)
    mother = choice(notPregnant)

    #The below code will not work because if you put a greater number in front of a smaller number in randint, it will return an error
    for i in range(randint(0, 2)):
      creatures.append(dinoSquirrel(
      Xrand(mother.speed, father.speed)+randint(1,3)-2,
      Xrand(mother.intelligence, father.intelligence)+randint(1,3)-2, 
      Xrand(mother.strength, father.strength)+randint(1,3)-2, 
              choice([mother.camo, father.camo, True, False]), 
              Xrand(mother.claws, father.claws)+randint(1,3)-2, 
              Xrand(mother.teeth,father.teeth)+randint(1,3)-2, 
              Xrand(mother.size,father.size)+randint(1,3)-2, choice(list(names)),0, choice(["Male", "Female"]), choice([True, False]), 0))
  return creatures

namesGender = {
  "bob":"Male",
  "george":"Male",
  "clifford":"Male",
  "odie":"Male",
  "hobbes":"Male",
  "garfield":"Male",
  "ace":"Male",
  "andy":"Male",
  "argo":"Male",
  "bandit":"Male",
  "barkley":"Male",
  "beethoven":"Male",
  "balto":"Male",
  "jane":"Female",
  "sophie":"Female",
  "lady":"Female",
  "lassie":"Female",
  "agnes":"Female",
  "pencil":"Female",
  "arlene":"Female",
  "belle":"Female",
  "bitsy":"Female",
  "daisy":"Female",
  "dutchess":"Female",
  "marley":"Female",
  "winnie":"Female"
}

def createCreatures():
  monster = dinoSquirrel(randint(1,5),randint(1,5), randint(1,5), choice([True, False]), randint(1,5), randint(1,5), randint(1,5), choice(list(namesGender.keys())),0, "undefinded", choice([True, False]), 0)
  monster.gender = namesGender[monster.name]
  return monster


names = namesGender.keys()

creatures = [createCreatures() for i in range (3)]

def output(creature):
  attrs = vars(creature)
  print(', '.join("%s: %s: " % item for item in attrs.items()))

def hunt(species, rounds):
  survivors = []
  for creature in species:
    if rounds < 5:
      if creature.live > randint(1, 50+(10*rounds)):
        survivors.append(creature)
    else:
      if creature.live > randint(1, 100):
        survivors.append(creature)
  return survivors
    
rounds = 0

def Engine():
  global creatures, names, rounds
  rounds += 1
  print("round: " + str(rounds))
  for i in range(len(creatures)):
    print ("<------------->")
    output(creatures[i])
    creatures[i].age += 1
  print ("<------------->")
  creatures = hunt(creatures, rounds)
  print ("\n")
  print("these are the survivors:")
  for i in range(len(creatures)):
    print ("<------------->")
    output(creatures[i])
    creatures[i].age += 1
  print ("<------------->")
  total = 0
  for i in range(len(creatures)):
    total += creatures[i].live
  if len(creatures) == 0:
    quit()
  print ("the average survival rate is: " + str(int(total/(len(creatures)))))
  creatures = reproduce(creatures)
  if input("again? ") == "y":
    print('\n')
    Engine()
  #whether they get hunted = speed, intelligence, camo
  #for i in range (len(creatures)):

Engine()
