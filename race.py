#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 18:38:19 2023

@author: giannidiarbi
 DS2000
 Spring 2023
 HW 2 Problem 2
 race.py
 
 Test case:
     Kayla's location: (5, 2)
     Cooper's location: (1, 2)
     Euclidean distance: (5 - 1) ** 2 + (2 - 2) ** 2 = 16, then take
                         the sqrt to get 4
    Time to reach Cooper: 4 * 10 = 40 minutes 
    
"""
LOCATIONS_FILE = "locations.txt"

def main():
    # Gather data - read in each person's name, x position, and y position
    with open(LOCATIONS_FILE, "r") as infile: 
        name1 = infile.readline().strip()
        x_position1 = int(infile.readline().strip())
        y_position1 = int(infile.readline().strip())
        
        name2 = infile.readline().strip()
        x_position2 = int(infile.readline().strip())
        y_position2 = int(infile.readline().strip())
    
    # Prompt the user for Cooper's location (his x and y value)
    cooper_x = int(input("What is Cooper's x value (1-5)? \n"))
    cooper_y = int(input("What is Cooper's y value? (1-3)? \n"))
    
    # Computation - use Euclidean Distance to compute how far both Kayla and 
    # Laney are from cooper. 
    distance1_squared = (x_position1 - cooper_x) ** 2 + \
        (y_position1 - cooper_y) ** 2
    distance1 = distance1_squared ** 0.5
    
    distance2_squared = (x_position2 - cooper_x) ** 2 + \
        (y_position2 - cooper_y) ** 2
    distance2 = distance2_squared ** 0.5
    
    # Calculate the time required for each person to reach Cooper
    time1 = distance1 * 10
    time2 = distance2 * 10
    
    # Communication - report out the results
    print(name1, "is", round(distance1, 3), "units away from Cooper.")
    print("It will take", name1, round(time1), "minutes to reach him.\n")
    
    print(name2, "is", round(distance2, 3), "units away from Cooper.")
    print("It will take", name2, round(time2), "minutes to reach him.")
main()
