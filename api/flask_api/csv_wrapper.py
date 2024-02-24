import pandas as pd

class CSVWrapper():

    def readCSV(filePath):
        return pd.read_csv(filePath)