import sys
import numpy as np
import pandas as pd
import emoji
from colorama import Fore, Style

print(Fore.RED + "running the script!" + Style.RESET_ALL)

scores = np.array([3,4,5,6,7,8])
avg = np.mean(scores)

message = emoji.emojize("Python is working :zany_face: ")


print(f"AVG VALUES {avg} -- {message}!!!!")


print("hello made changes!")



