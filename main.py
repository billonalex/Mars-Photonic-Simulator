from model import MarsModel

if(__name__ == "__main__"):

    """
    Here is the first option to declare and make a simulation !
    """

    my_model = MarsModel(baseline=10, diameter=1)

    my_model.calculate()
    my_model.show()
