def get_toi_training_set():
    """
    Reads a TOI catalog in a .csv format, selecting a subset of rows using the
    following criteria: single-planet system, main-sequence/non-evolved host star.

    It returns a training set, which is a list of targets with each of
    their TIC ID and orbital parameters.
    """

    training_set = []

    training_set_system = {'id': "", 'depth': 0.0, 'ecc': 0.0,
                        'inc_angle': 0.0, 'period': 0.0,
                        'duration': 0.0}

    training_set.append(training_set_system)


    return training_set
