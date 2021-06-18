from get_toi_training_set import get_toi_training_set
from create_sim_lc import create_sim_lc
from get_qlp_lc import get_qlp_lc
from plot_diagnostic_train_toi import plot_diagnostic_train_toi

def get_training_set():
    """
    Given a catalog of TOIs, it selects a subset based on selection criteria,
    creates simulated light-curve based on on star and planet parameters.

    In addition, retrieves observed data from QLP light-curves,
    storing these observed data to disk.

    Finally, it produces diagnostic plots of modelled and observed light curves
    of each TOI.
    """

    # Define Training using TOI catalog, selecting a subsample
    toi_training_systems = get_toi_training_set()

    # Model transit using LC simulator given TOI tic ids
    # and orbital parameters
    all_sim_times, all_sim_fluxes = [], []

    for toi in toi_training_systems:

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
