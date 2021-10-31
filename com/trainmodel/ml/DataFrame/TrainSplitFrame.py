import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class TrainTestSplit:

    @staticmethod
    def testTrainSplitFrame(filename):
        df = pd.read_csv('./data/' + filename)
        X = df.drop(['sale_price'], axis=1).values
        y = df['sale_price'].values
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=66)
        return X_train, X_test, y_train, y_test
