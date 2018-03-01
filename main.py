import sys
import math
import numpy as np
from car import Car

def readFile(filename):
    '''
    This method read the file and gives back the data.
    '''

    with open(filename, 'r') as file:
        print(file.name)
        paramenters = file.readline()
        rows, cols, vehicles, rides, bonus, steps = [int(n) for n in paramenters.split()]

        lists = []

        # lists.append(file.readline())

        # a, b, c, d, e, f = [int(n) for n in file.readline().split()]

        # lists.append((a,b,c,d,e,f))

        for ride in range(rides):
            rideInfo = file.readline()
            start_x, start_y, finish_x, finish_y, start_time, finish_time = [int(n) for n in rideInfo.split()]
            lists.append([(start_x, start_y), (finish_x, finish_y), start_time, finish_time, ride])

        return rows, cols, vehicles, rides, bonus, steps, lists

def distanceCalc(point1, point2):
    '''
    Returns the distance between two points
    '''
    distance = abs(point1[0] - point2[0]) + abs(point1[1]- point2[1])

    return distance

def purify(ride):
    if (distanceCalc(ride[0], ride[1]) < ride[3] - ride[2]):
        return ride
    else:
        return []

def purifyList(bigList):
    newList = []
    for element in bigList:
        if (purify(element) != []):
            newList.append(element)
    return newList

def sortListByDistanceTo00(rideList):
    
    for index in range(1,len(rideList)):
        currentvalue = rideList[index]
        position = index

        while position>0 and distanceCalc(rideList[position-1][0],(0,0))>distanceCalc(currentvalue[0], (0,0)):
            rideList[position]=rideList[position-1]
            position = position-1

        rideList[position]=currentvalue
    return rideList


def timeToReachStart(ride):
    timeAvailable = ride[3] - ride [2] - distanceCalc(ride[0], ride[1]) - 1
    return timeAvailable

def rechable(ride, pos_x, pos_y, currentTime):
     if ( distanceCalc(ride[0],(pos_x, pos_y)) < timeToReachStart(ride) + currentTime - ride[2] ):
        return 1
     else:
        return 0

def findClosestRide(rideList, pos_x, pos_y, currentTime):
    currentClosest = rideList[0]
    for ride in rideList:
        if (rechable(ride, pos_x, pos_y, currentTime)):
            if distanceCalc(currentClosest[0], (pos_x, pos_y)) > distanceCalc(ride[0], (pos_x, pos_y)):
                currentClosest = ride
    return currentClosest


def assignNewRide(currentCar, rideList):
    nextRide = findClosestRide(sortedDistanceList)
    currentCar.aimAt_x = nextRide[]
    currentCar.aimAt_y = sortedDistanceList[count][0][1]
    currentCar.rideNumber = sortedDistanceList[count][4]

    return currentCar

##########################################################

##### Read the File
rows, cols, vehicles, rides, bonus, steps, ridesList = readFile(sys.argv[1])

print('rows', rows)
print('cols', cols)
print('vehicles', vehicles)
print('rides', rides)
print('bonus', bonus)
print('steps', steps)

##### Purify list
# print(ridesList)

purifiedList = purifyList(ridesList)

# print(purifiedList)

print(distanceCalc(ridesList[0][0], ridesList[0][1]))

###### Sort purifiedList 
sortedDistanceList = sortListByDistanceTo00(purifiedList)

print(sortedDistanceList)

print(sortedDistanceList[0][0][0])

###### initialize car-objects
carList = []

for id in range(vehicles):
    newCar = Car([],[],id)    
    carList.append(newCar)



print(carList)

# send the cars to the destinations
for count in range(vehicles):
    carList[count].aimAt_x = sortedDistanceList[count][0][0]
    carList[count].aimAt_y = sortedDistanceList[count][0][1]
    carList[count].rideNumber = count

for count in range(vehicles):
    sortedDistanceList.pop(0)


finishedRidesList = []

for tick in range(steps):
    # check if any car has nothing to do
    for count in range(vehicles):
        if (carList[count].aimAt_x == []):
            nextRide = findClosestRide(sortedDistanceList)
            carList[count].aimAt_x = sortedDistanceList[count][0][0]
            carList[count].aimAt_y = sortedDistanceList[count][0][1]
            carList[count].rideNumber = sortedDistanceList[count][4]
        else:
            if ( carList[count].pos_x == carList[count].aimAt_x ) and ( carList[count].pos_y == carList[count].aimAt_y ):
                finishedRidesList.append((carList[count].rideNumber, carList[count].id))
                carList[count].aimAt_x = []
                carList[count].aimAt_y = []
        