import operator
from random import randint
from math import log2


def listscalarmul(l, scalar):
    #print(l, scalar)
    return list(x * scalar for x in l)


def listadd(l1, l2):
    return list(map(operator.add, l1, l2))

class Planet:
    planet_ID=0
    def __init__(self):
        #self.mass=randint(1,10**5)*10**10
        self.mass =  10 ** 15
        #self.radius=randint(10,50)
        self.radius = 20
        #self.velocity=list(randint(0,0) for _ in range(2))
        self.velocity = [0,5-Planet.planet_ID*10]
        self.path=[]
        #self.velocity = [0,0]
        self.color=tuple(randint(0,255) for _ in range(3))
        #self.location=list(randint(200,800) for _ in range(2))
        #self.location = list(randint(200, 800) for _ in range(2))
        self.location = [700-Planet.planet_ID*400,500]
        #print("planet id is ",self.planet_ID)
        self.planet_index=self.planet_ID
        Planet.planet_ID+=1
        self.planetDetails()
        self.path.append(self.location)
        # doing this as it requires two points
        self.path.append(self.location)
        self.accel = [0,0]


    def planetDetails(self):
        print("This is Planet: ",self.planet_index,end=" ")
        print("Mass: ", self.mass,end=" ")
        print("Location: ", self.location,end=" ")
        print("Velocity: ", self.velocity)

    def updatePlanet(self):
        accel=self.accel
        if abs(accel[0])<1:
            time=1
        else:
            time = 1/(100*int(abs(accel[0])))
        self.location = listadd(self.location,
                                listadd(listscalarmul(self.velocity, time), listscalarmul(accel, 0.5 * time ** 2)))
        self.path.append(self.location)
        self.velocity = listadd(self.velocity, listscalarmul(accel, time))
        self.planetDetails()

    def updateAcceleration(self,accel):
        self.accel = accel

class Universe:
    planets=[]
    gravitational_constant=6.67*(10**-11)

    def __init__(self):
        for i in range(2):
            self.planets.append(Planet())

    def sqDistanceCalculator(self,loc1,loc2):
        return loc2[0]-loc1[0],loc2[1]-loc1[1],sum([(x[0]-x[1])**2 for x in zip(loc1,loc2)])

    def calculateAcceleration(self,planet_index):
        ego_planet = self.planets[planet_index]
        accel=[0,0]
        for i,p in enumerate(self.planets):
            if i!=planet_index:
                x_diff,y_diff,sq_dist = self.sqDistanceCalculator(ego_planet.location,p.location)
                print(x_diff,y_diff,sq_dist)
                temp_acc=self.gravitational_constant*p.mass/(sq_dist)
                accel=listadd(accel,[temp_acc*x_diff/(sq_dist**0.5),temp_acc*y_diff/(sq_dist**0.5)])
        return accel

    def updateUniverse(self):

        for i,p in enumerate(self.planets):
            accel = self.calculateAcceleration(i)
            print("acceleration of planet ",i," is ",accel)
            p.updateAcceleration(accel)

        for i,p in enumerate(self.planets):
            p.updatePlanet()