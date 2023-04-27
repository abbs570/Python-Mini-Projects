#!/usr/bin/env python3

print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()
  
print("Okay! Lets play :) ")
score = 0  
# question 1
answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    
#question 2
answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    
#question 3
answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    
# question 4
answer = input("What does PSU stand for? ")
if answer == "power supply":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")
print("You got a " + str((score/4) * 100) + "%.")