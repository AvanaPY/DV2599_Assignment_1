# DV2599 - Assignment 1

Made by: 
* Emil Karlström, DVAMI19h
* Samuel Jonsson, DVAMI19h

## Prerequisites

In order to run the program, make sure to have `pandas` and `numpy` installed, you may install it using python3 with this command if not:

`python3 -m pip install pandas numpy`

## spambase.csv

Due to the given data in the assignment lacking a header, we include a `spambase.csv` file which includes all the original data along with the headers for ease-of-use. 

## Running the program

To run the program, execute this line of code:

`python3 main.py`

## Defaults

By default the program uses four bins per column and uses 1% of the data to train the model. One may change the train-validation ratio by changing the `ratio` variable passed into the `training_validation_split` function.