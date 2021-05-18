from astropy import *

"""
This class will represent our model.
We can define our parameters, make the calculations and plot the results
"""
class MarsModel:

    #Constructor
    def __init__(self, baseline, diameter):
        self.baseline = baseline
        self.diameter = diameter

    def calculate(self):
        print('Function to make the simulation')

    #Show result
    def show(self):
        print('Function to plot the result')