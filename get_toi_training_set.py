import pandas as pd

def get_toi_training_set(toi_criteria):
    """
    Reads a TOI catalog in a .csv format, selecting a subset of rows using the
    following criteria: single-planet system, main-sequence/non-evolved host star.

    It returns a training set, which is a list of targets with each of
    their TIC ID and orbital parameters.
    """

    # Catalog of all TOIs which we will subsample into a training set
    training_set = pd.read_csv("tois.csv", skiprows = 4)
    # test to make sure that the filtering is working correctly
    #print(len(training_set['Star Radius Value']))

    # Getting subset
    # id's, ignoring for now as well as other parameters
    # we don't have values for in this dataset
    #training_set = training_set[training_set['Transit Depth Value'].between(toi_criteria['depth'][0], toi_criteria['depth'][1]]
    # ecc
    # semimajor
    # long_peri
    # incl_angle
    #training_set = training_set[training_set['Transit Duration Value'].between(toi_criteria['duration'][0], toi_criteria['duration'][1])]
    #training_set = training_set[training_set['Orbital Period Value'].between(toi_criteria['period'][0], toi_criteria['period'][1])]
    #training_set = training_set[training_set['Planet Radius Value'].between(toi_criteria['planet_r'][0], toi_criteria['planet_r'][1])]
    training_set = training_set[training_set['Star Radius Value'].between(toi_criteria['star_r'][0], toi_criteria['star_r'][1])]

    #print(len(training_set['Star Radius Value']))

    return training_set
