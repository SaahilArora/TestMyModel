from com.trainmodel.ml.DataFrame.TrainSplitFrame import TrainTestSplit
from com.trainmodel.ml.Model.LinearRegressionModel import LinearRegressionModel


def __trainTestSplit__(filename):
    return TrainTestSplit.testTrainSplitFrame(filename)


class ModelFactory:
    model = None

    def __getModel__(self, filename, modelType, algoType):
        X_train, X_test, y_train, y_test = __trainTestSplit__(filename)
        self.model = LinearRegressionModel(X_train, X_test, y_train, y_test)
        self.model.predict()
        pass

    def getTestR2Score(self):
        return self.model.test_r2Score

    def getTestMAEScore(self):
        return self.model.test_maeScore

    def getTrainR2Score(self):
        return self.model.train_r2Score

    def getTrainMAEScore(self):
        return self.model.train_maeScore
