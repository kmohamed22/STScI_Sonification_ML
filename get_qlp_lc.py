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

    # Clara: "will allow us to query by TIC id" query_criteria
    # get_product_list
    # astropy.table.vstack can be used to stack the returns for each tic_id

    # if things start timing out do smaller batches

    # download_products will alow us to get lc's, Clara says need to do loop
    # what clara often does is poke through MAST portal to f
    # obs_id == tic id, prob want to filter on project
    # should be able to downsample to get specific observation QLP for that tic_id

    return qlp_list
