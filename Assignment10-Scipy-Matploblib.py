# Scipy
#We have the min and max temperatures in a city In India for each months of the year.
#We would like to find a function to describe this and show it graphically, the dataset
#given below.
#Task:
#1. fitting it to the periodic function
#2. plot the fit
#Data
#Max = 39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25
#Min = 21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18

import numpy as np

temp_max = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
temp_min = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])

import matplotlib.pyplot as plt
months = np.arange(12)
plt.plot(months, temp_max, 'ro')
plt.plot(months, temp_min, 'bo')
plt.xlabel('Month')
plt.ylabel('Min and max temperature')

from scipy import optimize
def yearly_temps(times, avg, ampl, time_offset):
    return (avg
            + ampl * np.cos((times + time_offset) * 1.8 * np.pi / times.max()))

res_max, cov_max = optimize.curve_fit(yearly_temps, months,temp_max, [40, 20, 0])
res_min, cov_min = optimize.curve_fit(yearly_temps, months,temp_min, [-40, 20, 0])

days = np.linspace(0, 12, num=365)
plt.figure()
plt.plot(months, temp_max, 'ro')
plt.plot(days, yearly_temps(days, *res_max), 'r-')
plt.plot(months, temp_min, 'bo')
plt.plot(days, yearly_temps(days, *res_min), 'b-')
plt.xlabel('Month')
plt.ylabel('Temperature ($^\circ$C)')
plt.show()
            

# Matploblib
#This assignment is for visualization using matplotlib:
#data to use:
#url=
#https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.cs
#v
#titanic = pd.read_csv(url)
#Charts to plot:
#1. Create a pie chart presenting the male/female proportion
#2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender

import pandas as pd 
import matplotlib.pyplot as plt

url= 'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)
titanic.head()
#1. Create a pie chart presenting the male/female proportion
df = titanic['sex'].value_counts()
df = pd.DataFrame (df)
labels = df.index
plt.pie (df.sex, shadow = True, startangle = 90, labels = labels, explode = (0.1,0), autopct='%1.1f%%' )
plt.legend(labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()
#2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender
import matplotlib.patches as mpatches
kf = titanic [['fare','age','sex']]
kf.head()
kf.info()
col = {'female':'red','male':'yellow'}
kf = kf.dropna(subset=['sex'])
kf.info()
plt.scatter (kf.fare, kf.age,c = kf.sex.map(col), alpha = 0.8)
plt.xlabel ('Fare')
plt.ylabel ('Age')
red_patch = mpatches.Patch(color='red', label='Female')
yellow_patch = mpatches.Patch(color='yellow', label='Male')
patches = [red_patch, yellow_patch]
plt.legend (handles= patches, markerscale = 0.1)
plt.show()

