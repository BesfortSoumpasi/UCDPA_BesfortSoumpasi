import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(r"C:\Users\besso\OneDrive\Desktop\UCD")

vga = pd.read_csv("vgsales.csv", encoding="UTF-8")

vga1 = vga.drop_duplicates("Name")

vga2 = vga1.dropna()

print(vga2.isnull().sum())