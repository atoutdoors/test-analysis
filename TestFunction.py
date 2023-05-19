

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import requests
import json
import sys
import numpy as np
from datetime import datetime
from get_cal_sn import get_cal
import openpyxl


wmo = 1489

dp = get_cal(wmo)

print(dp)