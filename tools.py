

def get_subject_timeseries():
    """get txt files in aal dir, remove vermis and cerebellum"""
    pass


def calc_cost_thresh(edges):
    """ return list of lists
    list[0] sorted thresholds
    list[1] associated cost
    """
    pass

def calc_partial_correl(aal_timeseries):
    """ use pcorr from fslnets to get partial correlations"""
    pass

def theshold_matrix(matrix, threshold):
    """return binary matrix size of matrix thresholded at threshold"""
    pass

def get_mod_value(bin_matrix):
    """ make graph, run newman, 
    return modularity value"""
    pass

def write_costs_mods():
    """ save the modularity at each cost in numpy array
    size 2 X ncosts
    0, : -> modularity
    1, : -> real cost
    """
    pass

def integrate_graph_metrics():
    """
    start with modularity, 
    add others
    shortest path (with some nan)
    largest component 
    betweenness centrality
    number of disconnections
    number of participation coeff """
    pass
    
