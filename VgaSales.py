import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(r"C:\Users\besso\OneDrive\Desktop\UCD")

vga = pd.read_csv("vgsales.csv", encoding="UTF-8")

vga1 = vga.drop_duplicates("Name")

vga2 = vga1.dropna()

vga_NA = vga2[["Name", "Year", "NA_Sales"]]
vga_EU = vga2[["Name", "Year", "EU_Sales"]]
vga_JP = vga2[["Name", "Year", "JP_Sales"]]
vga_Ot = vga2[["Name", "Year", "Other_Sales"]]
vga_GL = vga2[["Name", "Year", "Global_Sales"]]
