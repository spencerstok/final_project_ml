import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
import glob

##https://www.relataly.com/stock-market-prediction-with-multivariate-time-series-in-python/1815/#h-univariate-vs-multivariate-time-series

##df = pd.read_csv("reddit_classified_split.csv")


file_list = glob.glob("stock_dfs/*.csv")

stock_data = pd.read_csv("stock_comment_count/AMC.csv")

##stock_data['t'] = [x for x in range(len(stock_data))]
##df['t-1'] = df['t'].shift(1)

print(stock_data)
                   

##def series_to_supervised(data, n_in=1, n_out=1, dropnan = True):
    

                   
##print(stock_data.index.name)


X = stock_data[["Volume", "volume_change", "stock_change", "comment_volume", "polarity_avg", "subjectivity_avg"]]
##X = stock_data.drop("Date", "Open", "High", "Low", "Close", axis = 1)
y = stock_data[["Close"]]



X_train = X[:int(X.shape[0]*0.7)]
X_test = X[int(X.shape[0]*0.7):]
y_train = y[:int(X.shape[0]*0.7)]
y_test = y[int(X.shape[0]*0.7):]

tscv = TimeSeriesSplit(n_splits = 2)

i = 1
score = []
for tr_index, val_index in tscv.split(X_train):
    X_tr, X_val = X_train[tr_index], X_train[val_index]
    y_tr, y_val = y_train[tr_index], y_train[val_index]
    for mf in np.linspace(100, 150, 6):
        for ne in np.linspace(50, 100, 6):
            for md in np.linspace(20, 40, 5):
                for msl in np.linspace(30, 100, 8):
                    rfr = RandomForestRegressor(
                        max_features=int(mf),
                        n_estimators=int(ne),
                        max_depth=int(md),
                        min_samples_leaf=int(msl))
                    rfr.fit(X_tr, y_tr)
                    score.append([i,
                                  mf, 
                                  ne,
                                  md, 
                                  msl, 
                                  rfr.score(X_val, y_val)])
    i += 1

print(score)

##for train_index, test_index in tscv.split(X):
##    print("TRAIN:", train_index, "TEST:", test_index)
##    X_train, X_test = X[train_index], X[test_index]
##    y_train, y_test = y[train_index], y[test_index]
