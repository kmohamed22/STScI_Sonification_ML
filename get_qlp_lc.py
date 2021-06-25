def get_qlp_lc(toi_id):
    """
    Given a TOI ID, retrieves and writes to disk all availible QLP light-curves
    .fits files from MAST for this give TIC star.

    :param toi_id: TIC ID to retrieve QLP light-curves for given TOI.
    :type toi_id: str

    :return: List of file names of QLP light-curves written to disk.
    :rtype: list
    """

    # Susan Mullally vetting package to see if signal is from planet or not
    # "is light change from target or background objects"
    qlp_list = []

    return qlp_list
