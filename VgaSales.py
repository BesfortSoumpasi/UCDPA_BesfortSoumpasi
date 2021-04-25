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
EU_top = vga_EU.sort_values("EU_Sales", ascending=False)
JP_top = vga_JP.sort_values("JP_Sales", ascending=False)
OS_top = vga_OS.sort_values("Other_Sales", ascending=False)
GS_top = vga_GS.sort_values("Global_Sales", ascending=False)

Wii_NA = vga2.iloc[0]["NA_Sales"]
Wii_UE = vga2.iloc[0]["EU_Sales"]
Wii_JP = vga2.iloc[0]["JP_Sales"]
Wii_OS = vga2.iloc[0]["Other_Sales"]
Wii_GS = vga2.iloc[0]["Global_Sales"]

x = Wii_GS, Wii_OS, Wii_JP, Wii_UE, Wii_NA
y = ("Global", "Other", "Japan", "Europe", "NA")
x1 = Wii_OS, Wii_JP, Wii_UE, Wii_NA # x1 and y1 = Wii sales excluding global sales
y1 = ("Other", "Japan", "Europe", "NA")

SMB_NA = vga2.iloc[1]["NA_Sales"]
SMB_EU = vga2.iloc[1]["EU_Sales"]
SMB_JP = vga2.iloc[1]["JP_Sales"]
SMB_OS = vga2.iloc[1]["Other_Sales"]
SMB_GS = vga2.iloc[1]["Global_Sales"]

x2 = SMB_OS, SMB_JP, SMB_EU, SMB_NA #x2 will stand for sales of mario bros without showing global sales
y2 = ("Other", "Japan", "Europe", "NA")
colors = ["y", "r", "b", "g"]

Wii_vs_SMB = pd.DataFrame({"Wii":(x1),
                           "Super M": (x2)
                           },
                          index=["Other", "Japan", "EU", "NA"])
Wii_vs_SMB.plot(kind="bar")
plt.title("Wii Sports VS Super Mario Bros. Sales")
plt.xlabel("Region")
plt.ylabel("Sales in Millions")
plt.show()