# fdaTasks2020
***
### This repository contains a jupyter notebook with all four tasks for the module Fundamentals of Data Analytics for the year 2020. 
The notebook is divided into four clearly defined sections. Each section contains a description of the task accompanied by the solution and relevant references. I provide a walkthrough of the process I take in arriving at the solution. The programming language used for each task is Python. 


## Task 1 - 05/10/2020
**List to dictionry**
***
This task involves writing a function which takes in a list as input and returns a dictionary of unique items in the list as keys and the number of times each item appears as values

## Task 2 - 02/11/2020
**Dice roll simulation**
***
Task 2 involves writing a Python function called `dicerolls()` that simulates rolling dice. The function should take two parameters: the number of dice *k* and the number of times to roll the dice *n*. The function should simulate randomly rolling k dice n times, keeping track of each total face value. It should then return a dictionary with the number of times each possible total face value occurred. I generate plots for visualisation of the output of the function, with *k* set to different values.

## Task 3 - 16/11/2020
**Coin flip simulation**
***
For task 3, the aim is to write some python code that simulates flipping a coin 100 times. This code is then run 1,000 times, keeping track of the number of heads in each of the 1,000 simulations. An appropriate plot is selected to depict the resulting list of 1,000 numbers, showing that it roughly follows a bell-shaped curve.

## Task 4 - 30/11/2020
**Simpson's Paradox**
***
In this task, I demonstrate Simpson's paradox through visualisation. I generate 4 data sets using `numpy.linspace`, each of which represent a positive trend in the relationship between variables. However, when each of theses data sets are taken in aggregate, an overall negative trend is observed. This is best understood through visualisation and in the Jupyter notebook I have plotted the data on a graph. I also explain why I chose the parameters in generating the data sets, and why this results in the phenomenon of Simpson's paradox. 
