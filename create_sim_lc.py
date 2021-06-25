import batman
import numpy as np

def create_sim_lc(toi):
    """
    Given a TOI's ID and orbital parameters, returns a modelled light-curve
    consisting of times and corresponding fluxes.

    :param toi: TIC ID and collection of orbital parameters for a given TOI.
    :type toi: dict

    :return: A tuple consisting of (simulated times, simulated fluxes).
    :rtype: tuple
    """

    params = batman.TransitParams()       #object to store transit parameters
    params.t0 = toi[""]                        #time of inferior conjunction
    params.per = toi[""]                       #orbital period
    params.rp = toi[""]                       #planet radius (in units of stellar radii)
    params.a = toi[""]                        #semi-major axis (in units of stellar radii)
    params.inc = toi[""]                      #orbital inclination (in degrees)
    params.ecc = toi[""]                       #eccentricity
    params.w = toi[""]                        #longitude of periastron (in degrees)
    params.limb_dark = "nonlinear"        #limb darkening model
    params.u = [0.5, 0.1, 0.1, -0.1]      #limb darkening coefficients [u1, u2, u3, u4]

    t = np.linspace(-0.025, 0.025, 1000)  #times at which to calculate light curve
    m = batman.TransitModel(params, t, nthreads = 4)    #initializes model




    return (t, m.light_curve(params))
