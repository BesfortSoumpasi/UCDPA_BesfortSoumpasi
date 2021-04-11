import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(r"C:\Users\besso\OneDrive\Desktop\UCD")

vga = pd.read_csv("vgsales.csv", encoding="UTF-8")

vga1 = vga.drop_duplicates("Name")

vga2 = vga1.dropna()

vga_NA = vga2[["Name", "NA_Sales"]]
vga_EU = vga2[["Name", "EU_Sales"]]
vga_JP = vga2[["Name", "JP_Sales"]]
vga_OS = vga2[["Name", "Other_Sales"]]
vga_GS = vga2[["Name", "Global_Sales"]]

NA_top = vga_NA.sort_values("NA_Sales", ascending=False)
UE_top = vga_EU.sort_values("EU_Sales", ascending=False)
JP_top = vga_JP.sort_values("JP_Sales", ascending=False)
OS_top = vga_OS.sort_values("Other_Sales", ascending=False)
GS_top = vga_GS.sort_values("Global_Sales", ascending=False)

print(vga2.loc[vga2["Name"] == "Wii Sports"])