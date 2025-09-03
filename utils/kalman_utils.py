import numpy as np
from sklearn.metrics import mean_squared_error
from pykalman import KalmanFilter

def tune_kalman_filter(train_data):
    min_mse = float('inf')
    best_params = {}
    for obs_cov in [100, 500, 1000]:
        for trans_cov in [10, 50, 100, 200]:
            kf = KalmanFilter(
                initial_state_mean=train_data.iloc[0],
                observation_covariance=obs_cov,
                transition_covariance=trans_cov,
                transition_matrices=1,
                observation_matrices=1
            )
            state_means, _ = kf.filter(train_data.values)
            mse = mean_squared_error(train_data, state_means)
            if mse < min_mse:
                min_mse = mse
                best_params = {
                    'observation_covariance': obs_cov,
                    'transition_covariance': trans_cov
                }
    return best_params
