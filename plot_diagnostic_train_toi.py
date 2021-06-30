def plot_diagnostic_train_toi(qlp_list, sim_times, sim_fluxes):
    """
    Given a list of QLP observed light-curve file names for a TOI, and the simulated
    times and fluxes for the modelled light-curve, creates phase-folded plots
    with modelled light-curve superimposed on the observed light-curve.

    :param qlp_list: List of file names for a given TOI based on all sectors
    the target was observed in.
    :type: list

    :param sim_times: List of time stamps, in units identical to QLP observational
    data, for simulated light-curve.
    :type: np.arrays

    :param sim_fluxes: List of fluxes, in counts/sec, for simulated light-curve.
    :type: np.arrays
    """

    print("Hello world!")

    # create folder called tests, to keep repo tidy-ed up
    # make test function for each, as "test_plot_diagnostic_train_toi.py" for example
    # pytest needs it like that, https://docs.pytest.org/en/6.2.x/
    # use assert (its a core part of python) (ex: assert output of this func is true)
    # if false , will throw exception, can write tests before functions even if youd like
