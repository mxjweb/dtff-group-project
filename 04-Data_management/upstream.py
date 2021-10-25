# upstream.py
import numpy as np
import pandas as pd

from connect import DATAPATH

def put_rd_data():
    """Store random data to the DB."""

    df = pd.DataFrame(data=np.random.choice(['foo','bar','baz'], size=(100000,3)), columns=["one", "two", "three"])
    filename = DATAPATH + "test.ftr"
    df.to_feather(filename)