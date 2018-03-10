import math

class Car:

    def __init__(self, aim_x, aim_y, numberID):
        self.ridesNumberList = []
        self.pos_x = 0
        self.pos_y = 0
        self.available = True
        self.id = numberID
        self.currentTime = 0


    #### Functions for Car ####
    def distanceCalc(self, point1, point2):
        '''
        Returns the distance between two points
        '''
        distance = abs(point1[0] - point2[0]) + abs(point1[1]- point2[1])

        return distance

    def getDistCarRide(self, ride):
        '''
        Return the distance between the car and the starting point of the ride.
        '''
        return self.distanceCalc((self.pos_x, self.pos_y), ride[0])

    def reachable(self, ride):
        '''
        Checks if a ride can be done in time.
        '''
        pathToStart = self.distanceCalc((self.pos_x, self.pos_y), ride[0])
        pathToFinish = self.distanceCalc(ride[0], ride[1])

        return self.currentTime + pathToStart + pathToFinish < ride[3]

    def reachable2(self, ride):
        '''
        Checks if a ride can be done in time.
        '''
        pathToStart = self.distanceCalc((self.pos_x, self.pos_y), ride[0])

        return self.currentTime + pathToStart < ride[2]

    def getIoNextRide(self, ridesList):
        '''
        Gets the index of the next possible ride:
        '''
        index = []
        for count in range(len(ridesList)):
            if self.reachable(ridesList[count]):
                index = count
                break

        return index

    def getIoNextRideB(self, ridesList):
        '''
        Gets the index of the next possible bonus ride:
        '''
        index = []
        for count in range(len(ridesList)):
            if self.reachable2(ridesList[count]):
                index = count
                break

        return index
        
    def getIoNextRideClosest(self, ridesList):
        '''
        Gets the index of the next possible and closest ride:
        '''
        index = []
        currentclosest = 999999999999
        for count in range(len(ridesList)):
            distanceToStart = self.getDistCarRide(ridesList[count])
            if self.reachable(ridesList[count]) and distanceToStart < currentclosest:
                index = count
                currentclosest = self.getDistCarRide(ridesList[count])

        return index

    def timePassed(self, ride):
        '''
        Adjusts the currentTime of the car to time needed for the ride
        '''
        pathToStart = self.distanceCalc((self.pos_x, self.pos_y), ride[0])
        pathToFinish = self.distanceCalc(ride[0], ride[1])

        self.currentTime += pathToStart + pathToFinish

    def takeNextRide(self, ridesList):
        '''
        Takes the next possible ride in ridesList and sets sef.available false, when no ride is possible
        '''
        index = self.getIoNextRideClosest(ridesList)
        if index == []:
            self.available = False
            return ridesList
        
        self.timePassed(ridesList[index])
        self.ridesNumberList.append(ridesList[index][4])
        # self.ridesNumberList.sort()

        # removes the taken ride from the list
        ridesList.pop(index)

        return ridesList


    #### Getter and Setter for the class #####

    def getRidesNumberList(self):
        return self.ridesNumberList

    def getPosition_x(self):
        return self.pos_x
    
    def getPosition_y(self):
        return self.pos_y

    def available(self):
        return self.available
    
    def getID(self):
        return self.id