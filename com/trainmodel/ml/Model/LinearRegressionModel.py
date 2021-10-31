from sklearn.linear_model import LinearRegression
from sklearn import metrics

from com.trainmodel.ml.Loggers.Logger import Logger
from com.trainmodel.ml.Model.Model import Model


class LinearRegressionModel(Model):

    y_test = None
    X_test = None
    y_train = None
    X_train = None

    def __init__(self, X_train, X_test, y_train, y_test):
        super(LinearRegressionModel, self).__init__(X_train, X_test, y_train, y_test)
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

    def predict(self):
        clf = LinearRegression()
        clf = clf.fit(self.X_train, self.y_train)
        test_prediction = clf.predict(self.X_test)
        train_prediction = clf.predict(self.X_train)
        self.setTestR2Score(metrics.r2_score(self.y_test, test_prediction))
        self.setTestMAEScore(metrics.mean_absolute_error(y_true=self.y_test, y_pred=test_prediction))

        self.setTrainR2Score(metrics.r2_score(self.y_train, train_prediction))
        self.setTrainMAEScore(metrics.mean_absolute_error(y_true=self.y_train, y_pred=train_prediction))
        pass
