# downstream.py
import pandas as pd
from connect import DATAPATH

def get_rd_data():
    """Get random data from the DB."""

    filename = DATAPATH + "test.ftr"
    data = pd.read_ftr(filename)

    return data