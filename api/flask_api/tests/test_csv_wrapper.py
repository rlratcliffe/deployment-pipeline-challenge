import sys

sys.path.append('../flask_api')

from flask_api.csv_wrapper import CSVWrapper
import pandas as pd

def test_parsecsv():
    assert type(CSVWrapper.readCSV("tests/mockdata/source.csv")) == pd.DataFrame