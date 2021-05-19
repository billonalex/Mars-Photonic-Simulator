from astropy import *

"""
This class will represent our model.
We can define our parameters, make the calculations and plot the results
"""
class MarsModel:

    #Constructor
    def __init__(self, baseline, diameter):
        #We initiate our parameters here
        self.baseline = baseline
        self.diameter = diameter

        #We can declare and calculate different paramaters that we may need in the future


    def calculate(self):
        print('Function to make the simulation')

        """
        The idea is to put the biggest calculations here, and to add optional parameters to personalize our model
        Maybe we will want to make calculation many times
        2 possibilities in the main script :

            - Declare only one model and personalize it with parameters required
            - Declare one model per personalization
        """

    #Show result
    def show(self):
        print('Function to plot the result')

        """
        When the calculs are done, this function allows us to show the results.
        """