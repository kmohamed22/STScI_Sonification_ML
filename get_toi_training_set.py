import pandas as pd

def get_toi_training_set(toi_criteria):
    """
    Reads a TOI catalog in a .csv format, selecting a subset of rows using the
    following criteria: single-planet system, main-sequence/non-evolved host star.

    It returns a training set, which is a list of targets with each of
    their TIC ID and orbital parameters.
    """

    training_set = pd.read_csv("tois.csv", skiprows = 4)
    #print(training_set.columns)
    # Getting Objects in interval ranges
    # simple method, could use pd.IntervalIndex if want bounded between two values
    # for now, let's try with just one parameter
    training_set = training_set[training_set["Transit Depth Value"] <= toi_criteria["depth"]]
    # ecc
    # semimajor
    # long_peri
    # inclination angle
    training_set = training_set[training_set["Orbital Period Value"] <= toi_criteria["period"]]
    training_set = training_set[training_set["Transit Duration Value"] <= toi_criteria["duration"]]
    training_set = training_set[training_set["Planet Radius Value"] <= toi_criteria["planet_r"]]
    training_set = training_set[training_set["Star Radius Value"] <= toi_criteria["star_r"]]

    return training_set
