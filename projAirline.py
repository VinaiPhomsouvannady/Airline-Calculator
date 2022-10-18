# Name:        Vinai Phomsouvannady

# Class:       CSC 110 - Spring 2017

# Assignment:  Programming Project Design

# Due Date:    November 3, 2017



# Program Title:  Airline Flight Scheduling



# Project Description:

# --------------------

# The objective of this project is to write a program in Python

# that will read in a data file with all flights from Providence to

# Orlando and display information requested by the user. Looping until user

# request to leave





# General Solution:

# -----------------

# Create functions that are called upon to display information requested by

# user. Loop the menu in main() until user enters the correct input to leave.

# The functions will be called upon corresponding to a specific input.



# Pseudocode:

# -----------

# User enters file

# Checks file

# Displays menu and asks to choose one of the following options

# user enters input 1-7

# checks to make sure valid input

# asks for any information needed then calls upon the corresponding function

# Will loop back to the main menu of asking for input

# Loops until user inputs 7 ending the program



# Function Design:

# ----------------

import datetime



def getChoice():

    # This function displays menu gets input and returns it

    print("")

    print("Please choose one of the following options:")

    print("1 -- Find flight information by airline and flight number")

    print("2 -- Find flights shorter than a specified duration")

    print("3 -- Find the cheapest flight by a given airline")

    print("4 -- Find flight departing after a specified time")

    print("5 -- Find the average price of all flights")

    print("6 -- Write a file with flights sorted by departure time")

    print("7 -- Quit")

    choice = checkChoice()

    while choice < 1 or choice > 7:

        print("Entry must be between 1 and 7")

        choice = checkChoice()

    print("")

    return choice



def getData():

    # This function will create lists of the data

    airlineL = []

    flightNumL = []

    departTimeL = []

    arriveTimeL = []

    priceL = []

    inFile = checkFile()

    line = inFile.readline()

    line = line.strip()

    while line != '':

        airline, flightnum, depart, arrive, price = line.split(',')

        price = price[1:len(price)]

        airlineL.append(airline)

        flightNumL.append(int(flightnum))

        departTimeL.append(depart)

        arriveTimeL.append(arrive)

        priceL.append(int(price))

        line = inFile.readline()

        line = line.strip()

    return airlineL,flightNumL, departTimeL, arriveTimeL, priceL



def checkFile():

    # This function will make sure that a proper file is inputted.

    try:

        dataFile = open(input("Please enter a file name: "), 'r')

        return dataFile

    

    except IOError:

        print("Invalid file name try again ...")

        return checkFile()

    



def checkChoice():

    # This function will check to make sure each input in the main

    # function is in the range and is a proper integer

  OK = False

  while OK == False:

    try:

      choice = int(input("Choice ==> "))

      OK = True

    except ValueError:

        print("Entry must be a number")

  return choice



def checkNum(airlineList, airlineNumL, airline):

    # This function will check to make sure each input is a proper airline number

    # is a proper integer

    airlineNum = checkInt()

    index = searchNumIndex(airlineNumL, airlineNum)

    while (airlineNum not in airlineNumL) or (airlineList[index]!=airline):

        print("Invalid Entry")

        airlineNum = checkInt()

        index = searchNumIndex(airlineNumL, airlineNum)

    return airlineNum, index

    



def checkInt():

    # checks to make sure flight integer

  OK = False

  while OK == False:

    try:

      choice = int(input("Enter flight number: "))

      OK = True

    except ValueError:

        print("Invalid input -- try again")

  return choice



def checkDur():

    # checks to make sure dur integer

  OK = False

  while OK == False:

    try:

      choice = int(input("Enter maximum duration: "))

      OK = True

    except ValueError:

        print("Entry must be a number")

  return choice



def checkAirline(airlineList):

    # This function will check to make sure each input is a proper airline

    # name

    airlineName = input("Enter airline name: " )

    while airlineName not in airlineList:

        print("Invalid input -- try again")

        airlineName = input("Enter airline Name: ")

    return airlineName



def checkTime():

    #checks to make sure proper time format

    timeformat = "%H:%M"

    timeInput = input("Enter earlier departure time: ")

    try:

        validtime = datetime.datetime.strptime(timeInput, timeformat)

        return timeInput

    except ValueError:

        print("Invalid time - Try again")

        return checkTime()



def searchNumIndex(airlineNumL, airlineNum):

    #searches for index

    m = -1

    for i in range(len(airlineNumL)):

        if airlineNum == airlineNumL[i]:

            m = i

    return m

    

#11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

def specFlight(departTimeL, arriveTimeL, priceL, index):

    # asks for input in main

    # This will search through the list to find information about the

    #flight.

    #lets the user know if airline or flight number does not exist.

    departTime = departTimeL[index]

    arriveTime = arriveTimeL[index]

    price = priceL[index]

    return departTime, arriveTime, price





#2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222

def shorterFlights(maxTime, departTimeL, arriveTimeL):

    # This function will find all flights that have a shorter time than

    # the max time

        # HH = 0-24,   MM = 00-60

    shortL = []

    for i in range(len(departTimeL)):

        if maxTime>(convert(arriveTimeL[i])-convert(departTimeL[i])):

            shortL.append(i)    

    return shortL



#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

def cheapestFlight(airline, priceL, airlineL):

    # This function will find the cheapest flight in the given airline

    indexes = []

    for i in range(len(airlineL)):

        if airline == airlineL[i]:

            indexes.append(i)

    cheap = indexes[0]

    chpINDX = 0

    for i in range(1,len(indexes)):

        if cheap>indexes[i]:

            cheap = indexes[i]

            chpINDX = i

    return chpINDX



#444444444444444444444444444444444

def afterTime(departTime, departTimeL):

    # This function will provide the user with a list of flights that depart

    # after the specified time. Makes sure the time is valid. HH:MM.

    # HH = 0-24,   MM = 00-60

    afterL = []

    for i in range(len(departTimeL)):

        if convert(departTime)<convert(departTimeL[i]):

            afterL.append(i)

    return afterL





#55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555

def averagePrice(priceL):

    # This function finds the average price of all the flights of a specific

    # airline

    sum = 0

    for i in priceL:

        sum = sum+i

    average = sum/len(priceL)   

    return average




#666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666

def sort(theList):

    # This function will create a file called time-sorted-flights.csv

    # writing the flights sorted by departure time.

    # create a list of indexes that you sort based on departure time

    index = []

    for z in range(len(theList)):

        index.append(int(z))

    for i in range(1, len(theList)):

        save = theList[i]

        savecomp = convert(theList[i])

        save2 = index[i]

        j = i

        while j > 0 and convert(theList[j - 1]) > savecomp:

            # comparison

            theList[j] = theList[j - 1]

            index[j] = index[j-1]

            j = j - 1

	    # swap

        theList[j] = save

        index[j] = save2

    return index



def write(airlineL,flightNumL, departTimeL, arriveTimeL, priceL, sortL):

    #write data to file

    name = "time-sorted-flights.csv"

    newFile = open(f"{name}", 'w')

    for i in range(len(sortL)):

        newFile.write(f"{airlineL[sortL[i]]},{flightNumL[sortL[i]]}, {departTimeL[i]}, {arriveTimeL[sortL[i]]}, ${priceL[sortL[i]]}\n")

    newFile.close()

    return



def convert(depotime):

    #converts time to minutes

    hour, minute = depotime.split(':')

    hour = int(hour)*60

    minute = int(minute)

    depo = hour+minute

    return depo



def main():

    # The main function implements the pseudocode by using the functions

    # defined above.

    # looping using a while loop

    # asks for user input

    # check to make sure each input is correct

        # Call the function to get the data from the data file and store the results in three lists

    airlineL,flightNumL, departTimeL, arriveTimeL, priceL = getData()

    choice = getChoice()

    while choice != 7:

        if choice == 1:

            airline = checkAirline(airlineL)

            flightNum, index = checkNum(airlineL, flightNumL, airline)

            # Call the function to find flight

            print("")

            departTime, arriveTime, price = specFlight(departTimeL, arriveTimeL, priceL, index)

            print("AIRLINE FLT# DEPART ARRIVE PRICE")

            print(airline.ljust(7), str(flightNum).ljust(4), departTime.rjust(6),arriveTime.rjust(6)," $",str(price).rjust(2))

            choice = getChoice()




            

        elif choice == 2:

            maxdur = checkDur()

            shortL = shorterFlights(maxdur, departTimeL, arriveTimeL)

            print("")

            if len(shortL)>0:

                print("The flights that meet your criteria are: ")

                print("")

                print("AIRLINE FLT# DEPART ARRIVE PRICE")

                for i in shortL:

                    print(airlineL[i].ljust(7), str(flightNumL[i]).ljust(4), departTimeL[i].rjust(6),arriveTimeL[i].rjust(6),"$",str(priceL[i]).rjust(2))

            else:

                print("No flights meet your criteria")

            choice = getChoice()


            

        elif choice == 3:

            airline = checkAirline(airlineL)

            cheap = cheapestFlight(airline, priceL, airlineL)

            print("")

            print("The flights that meet your criteria are: ")

            print("")

            if cheap>-1:

                    print("AIRLINE FLT# DEPART ARRIVE PRICE")

                    print(airlineL[cheap].ljust(7),str(flightNumL[cheap]).ljust(4),departTimeL[cheap].rjust(6),arriveTimeL[cheap].rjust(6),"$",str(priceL[cheap]).rjust(2))

            else:

                print("No flights meet your criteria")

            choice = getChoice()





            

        elif choice == 4:

            depTime = checkTime()

            afterL = afterTime(depTime, departTimeL)

            if len(afterL)>0:

                print("The flights that meet your criteria are:")

                print("")

                print("AIRLINE FLT# DEPART ARRIVE PRICE")

                for i in afterL:

                    print(airlineL[i].ljust(7),str(flightNumL[i]).ljust(4), departTimeL[i].rjust(6),arriveTimeL[i].rjust(6),"$",str(priceL[i]).rjust(2))

            else:

                print("No flights meet your criteria")

            choice = getChoice()





        elif choice == 5:

            average  = averagePrice(priceL)

            average = "{:.2f}".format(average)

            print("The average price is $", average," ")

            choice = getChoice()





            

        elif choice == 6:

            sortL = sort(departTimeL)

            write(airlineL,flightNumL, departTimeL, arriveTimeL, priceL, sortL)

            print("Sorted data has been written to file: time-sorted-flights.csv")

            choice = getChoice()



    print("Thank you for flying with us")

