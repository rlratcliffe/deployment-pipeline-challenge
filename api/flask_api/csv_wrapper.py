import pandas as pd

class CSVWrapper:

    def readCSV(self, filePath):
        return pd.read_csv(filePath)