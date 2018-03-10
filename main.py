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


def writeFile(filename, _output):
    '''
    This method writes the input to a given file-location.
    '''

    with open(filename, 'w') as file:
        file.write(_output)


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

def sortListByBeginTime(rideList):
    ##
    less = []
    equal = []
    greater = []

    if len(rideList) > 1:
        pivot = rideList[0][2]
        for ride in rideList:
            if ride[2] < pivot:
                less.append(ride)
            if ride[2] == pivot:
                equal.append(ride)
            if ride[2] > pivot:
                greater.append(ride)
        # Don't forget to return something!
        return sortListByBeginTime(less)+equal+sortListByBeginTime(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return rideList

def sortListByEndTime(rideList):
    ##
    less = []
    equal = []
    greater = []

    if len(rideList) > 1:
        pivot = rideList[0][3]
        for ride in rideList:
            if ride[3] < pivot:
                less.append(ride)
            if ride[3] == pivot:
                equal.append(ride)
            if ride[3] > pivot:
                greater.append(ride)
        # Don't forget to return something!
        return sortListByBeginTime(less)+equal+sortListByBeginTime(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
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


##########################################################

##### Read the File
nameOfFile = sys.argv[1]
inputFile = "data/" + nameOfFile
outputFile = "output/" + nameOfFile

rows, cols, vehicles, rides, bonus, steps, ridesList = readFile(inputFile)

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
#sortedDistanceList = sortListByDistanceTo00(purifiedList)
#print(sortedDistanceList)
#print(sortedDistanceList[0][0][0])

sortedTimeList = sortListByEndTime(purifiedList)
# print(sortedTimeList)
print(sortedTimeList[0][0][0])

###### initialize car-objects
carList = []

for id in range(vehicles):
    newCar = Car([],[],id)    
    carList.append(newCar)

# print(carList)

###### Assign the rides to each car
# for car in carList:
    # sortedTimeList = car.takeNextRide(sortedTimeList)

for car in carList:
    while car.available:
        sortedTimeList = car.takeNextRide(sortedTimeList)



###### Output the fullfilled rides

output = ""

for count in range(len(carList)):
    output += str(len(carList[count].ridesNumberList)) + ' '

    for number in carList[count].ridesNumberList:
        output += str(number) + ' '
    
    output += '\n'

#print(output)
print(outputFile)
writeFile(outputFile, output)