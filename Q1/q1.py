import csv
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    
    f_nation = open("NationWide_2022.csv")
    f_seoul = open("Seoul_2022.csv")
    f_daejun = open("Daejun_2022.csv")
    f_jeju = open("Jeju_2022.csv")
    f_busan = open("Busan_2022.csv")

    nation = csv.reader(f_nation)
    seoul = csv.reader(f_seoul)
    daejun = csv.reader(f_daejun)
    jeju = csv.reader(f_jeju)
    busan = csv.reader(f_busan)

    next(nation)
    next(seoul)
    next(daejun)
    next(jeju)
    next(busan)

    na = []
    se = []
    da = []
    je = []
    bu = []

    for row in nation:
        na.append(float(row[-1]))

    for row in seoul:
        se.append(float(row[-1]))

    for row in daejun:
        da.append(float(row[-1]))

    for row in jeju:
        je.append(float(row[-1]))

    for row in busan:
        bu.append(float(row[-1]))
    f_nation.close()
    f_busan.close()
    f_seoul.close()
    f_jeju.close()
    f_daejun.close()
    
    plt.title("temperature 2022")
    plt.xlabel("month")
    xdata=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    plt.ylabel("temperature average (celcius)")
    
    plt.plot(xdata, na, label="NationWide")
    plt.plot(xdata, se, label="Seoul")
    plt.plot(xdata, da, label="Daejun")
    plt.plot(xdata, je, label="Jeju")
    plt.plot(xdata, bu, label="Busan")
    plt.legend()
    plt.show()
    
