import sys
import numpy as np
import pandas as pd
import emoji
from colorama import Fore, Style

print(Fore.BLUE + "running the script!" + Style.RESET_ALL)

scores = np.array([3,4,5,6,7,8])
avg = np.mean(scores)

message = emoji.emojize("Python is working :snake:")


print(f"Average values {avg} -- {message}")





