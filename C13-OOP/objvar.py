class Robot:
  '''Represents a robot, with a name.'''

  population = 0

  def __init__(self, name):
    "'Initializes the data.'"
    self.name = name
    print("(Initializing {})".format(self.name))

    Robot.population += 1

  def die(self):
    '''I am dying.'''
    print('{} is being destroyed!'.format(self.name))

    Robot.population -= 1

    if Robot.population == 0:
      print("{} was the last one.".format(self.name))
    else:
      print("There are still {0:d} robots working.".format(Robot.population))

  def sayHi(self):
    '''Greeting'''
    print("Greetings, my name is {}".format(self.name))

  @classmethod
  def howMany(cls):
    '''Prints the current population.'''
    print("We have {0:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.sayHi()
Robot.howMany()

droid2 = Robot("C-3PO")
droid2.sayHi()
Robot.howMany()

droid1.die()
droid2.die()

Robot.howMany()
