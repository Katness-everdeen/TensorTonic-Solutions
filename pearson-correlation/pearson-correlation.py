import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    X = np.asarray(X, dtype=float)
    mean = np.mean(X,axis = 0)
    X_centered = X-mean
    covariance = (X_centered.T @ X_centered) / (X.shape[0] - 1)
    std = np.std(X, axis = 0,ddof = 1)
    std_product = np.outer(std,std)
    correlation = covariance / std_product
    correlation[std_product == 0] = np.nan
    return correlation
    