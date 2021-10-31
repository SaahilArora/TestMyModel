class Model:
    test_r2Score = None
    test_maeScore = None

    train_r2Score = None
    train_maeScore = None

    def __init__(self, X_train, X_test, y_train, y_test):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

    def predict(self):
        pass

    def setTestR2Score(self, score):
        self.test_r2Score = score

    def setTestMAEScore(self, score):
        self.test_maeScore = score

    def setTrainR2Score(self, score):
        self.train_r2Score = score

    def setTrainMAEScore(self, score):
        self.train_maeScore = score

    def getTestR2Score(self):
        return self.test_r2Score

    def getTestMAEScore(self):
        return self.test_maeScore

    def getTrainR2Score(self):
        return self.train_r2Score

    def getTrainMAEScore(self):
        return self.train_maeScore
