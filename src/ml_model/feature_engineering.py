import numpy as np
import pandas as pd

def add_rolling_features(data, window=5):
    """
    data: 2D numpy array (timesteps x features)
    Returns: original features + rolling mean + rolling std, concatenated
    """
    df = pd.DataFrame(data)
    
    rolling_mean = df.rolling(window=window, min_periods=1).mean()
    rolling_std = df.rolling(window=window, min_periods=1).std().fillna(0)
    
    combined = np.hstack([
        df.values,
        rolling_mean.values,
        rolling_std.values
    ])
    
    return combined

if __name__ == "__main__":
    from preprocess import load_machine_data
    
    train, test, labels = load_machine_data()
    
    train_fe = add_rolling_features(train)
    test_fe = add_rolling_features(test)
    
    print("Original train shape:", train.shape)
    print("Enhanced train shape:", train_fe.shape)
    print("Original test shape:", test.shape)
    print("Enhanced test shape:", test_fe.shape)
