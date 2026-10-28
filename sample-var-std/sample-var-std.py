import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    var_sample = float(np.var(x, ddof=1))
    std_dev = float(np.sqrt(var_sample))

    return {
        "variance": var_sample,
        "standard_deviation": std_dev
    }    