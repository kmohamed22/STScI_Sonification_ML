from get_toi_training_set import get_toi_training_set
from create_sim_lc import create_sim_lc
from get_qlp_lc import get_qlp_lc
from plot_diagnostic_train_toi import plot_diagnostic_train_toi

import pandas as pd
import os.path
import json

def get_training_set():
    """
    Given a catalog of TOIs, it selects a subset based on selection criteria,
    creates simulated light-curve based on on star and planet parameters.

    In addition, retrieves observed data from QLP light-curves,
    storing these observed data to disk.

    Finally, it produces diagnostic plots of modelled and observed light curves
    of each TOI.
    """
    # Asking user for TOI criteria/desired population of TOIs to subsample
    toi_criteria = {'id': "", 'depth': 0.0, 'ecc': 0.0,
                        'semimajor' : 0.0, 'long_peri' : 0.0,
                        'inc_angle': 0.0, 'period': 0.0,
                        'duration': 0.0, 'planet_r' : 0.0,
                        'star_r' : 0.0}

    # Checking if previous selection criteria exist on disk
    choice = input("y/n: Would you like to use the previous selection criteria?")
    if os.path.isfile("toi_criteria.txt") and choice == y:
        # read the previous parameters from txt file to toi_criteria into the txt
        with open('toi_criteria.txt', 'r') as convert_file:
            toi_criteria = json.load(convert_file)

    # Otherwise creating the dictionary and saving it to disk
    else:
        print("There are no previously used selection criteria on disk.")
        toi_criteria['id'] = input("Enter pre-selected/desired TOIs, if any:")
        # Min, Max
        print("Enter the minimum and maximum values desired for each parameter.")
        print("The format is: (minimum value, maximum value)")
        toi_criteria['depth'] = input("Transit Depth Value: ")
        toi_criteria['ecc'] = input("Eccentricity: ")
        toi_criteria['semimajor'] = input("Semi-major Axis: ")
        toi_criteria['long_peri'] = input("Longitude of Periastron: ")
        toi_criteria['inc_angle'] = input("Inclination Angle: ")
        toi_criteria['duration'] = input("Transit Duration Value: ")
        toi_criteria['period'] = input("Orbital Period Value: ")
        toi_criteria['planet_r'] = input("Planet Radius: ")
        toi_criteria['star_r'] = input("Star Radius: ")

        with open('toi_criteria.txt', 'w') as convert_file:
            convert_file.write(json.dumps(toi_criteria))

    # Now converting the dictionary values into floats
    for param in toi_criteria:
        if param != 'id':
            toi_criteria[param] = [float(val) for val in toi_criteria[param].split(', ')]

    # Define Training using TOI catalog, selecting a subsample
    toi_training_systems = get_toi_training_set(toi_criteria)

    # Model transit using LC simulator given TOI tic ids
    # and orbital parameters
    all_sim_times, all_sim_fluxes = [], []

    # goes like: index, row in df.iterrows()
    for index, toi in toi_training_systems.iterrows():

        # Creating simulated LCs given TESS exoplanet system
        (sim_times, sim_fluxes) = create_sim_lc(toi)
        all_sim_times.append(sim_times)
        all_sim_fluxes.append(sim_fluxes)

        # Getting QLP data files if subset, saving to disk
        qlp_list = get_qlp_lc(toi["id"])

        # Plotting the model and data of TOI as sanity check
        plot_diagnostic_train_toi(qlp_list, sim_times, sim_fluxes)

if __name__ == "__main__":
    get_training_set()
