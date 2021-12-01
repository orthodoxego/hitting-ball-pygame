class Score:

    def __init__(self):
        self.__score = 0
        self.__max_score = self.getMaxScoreFromFile()

    @property
    def max_score(self):
        return self.__max_score

    @property
    def score(self):
        if self.__score < 0:
            self.__score = 0
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def __iadd__(self, other):
        if isinstance(other, int):
            self.__score += other
            if self.__score > self.__max_score:
                self.__max_score = self.__score
                self.writeToFileMaxScore()
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, int):
            self.__score -= other
            return self
        return NotImplemented

    def getMaxScoreFromFile(self):
        try:
            f = open("score.dat", "r", encoding="UTF-8")
            sc = int(f.readline())
            f.close()
            return sc
        except:
            f = open("score.dat", "w", encoding="UTF-8")
            f.write("0")
            f.close()
            return 0

    def writeToFileMaxScore(self):
        try:
            f = open("score.dat", "w", encoding="UTF-8")
            f.write(str(self.__max_score))
            f.close()
        except:
            print("Ошибка записи файла.")