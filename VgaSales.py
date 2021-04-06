import pandas as pd
import numpy as np
import matplotlib as plt
import os

os.chdir(r"C:\Users\besso\OneDrive\Desktop\UCD")

vga = pd.read_csv("vgsales.csv", encoding="UTF-8")

vga1 = vga.drop_duplicates("Name")

vga_publ_check = vga1[vga1["Publisher"].isnull()]
print(vga_publ_check)