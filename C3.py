
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from calendar import monthrange

#plt.figure(figsize=(12, 10), dpi=720)

data = "Z:/My Files/C3/Weather_all.csv"

def b_t_dt(x):#byte to date time
    return dt.datetime.strptime(x.decode(), "%Y-%m-%d %H:%M:%S")

#columns and their significance
###########################################
#time Y-m-d h:m:s
#temperature in celcius
#cloud base in metres   ((unreliable))
#bool rain/no rain      ((unreliable))
#bool clouds/no clouds  ((unreliable))
#wind direction in compass deg
#wks temp in celcius
#wind speed in kmh^-1
#wind peak in kmh^-1
#wind average in kmh^-1
#main wind direction in compass deg
#internal air temp in celcius
#internam humidity in %
#second external air temp in celcius
#external humidity in percentage
###########################################
times,temps,wind = np.genfromtxt(data,delimiter=',',usecols=(0,1,9),converters={0:b_t_dt},skip_header=1,unpack=True)



#def averaging(time,data,startyear=2015,endyear=2022):

    

#values,dates,dateyears = averaging(times,winddir,2016,2021)


def average_something(variable , time ,  avgmethod = 'mean' , months = np.arange(1,12+1,1) , years = np.arange(2015,2022+1,1) ):
    values = [] # function which can be applied to any variable such as temp or windspeed
    dates = []
    datayears =[]
    averages = []
    if avgmethod == 'mean':
        averagefunction = np.nanmean
    elif avgmethod == 'median':
        averagefunction = np.nanmedian
    for year in years: #years loop
        for month in months: #months loop
            days = np.arange(1,monthrange(year,month)[1]+1, 1) #deducing how many day in that month 
    #        print(month)
            for day in days:
                selection = np.logical_and(time >= dt.datetime(year,month,day,0,0), time < dt.datetime(year,month,day,23,59))
    #            print(year,month,day)  #selecting all the times in a single day
                #np.sum(selection)
                values.append(np.mean(variable[selection])) #calculating the mean of the variable in that day
                dates.append(dt.date(2016,month,day)) #generalizing all into one year
                datayears.append(year)
    for day in range(365):
        picked_data = values[day::365]
        averages.append(averagefunction(picked_data))#finding the median of all of the data for one day
    return values, dates, datayears, averages


plottemps, plotdates, plotyears, plotaverages_temp = average_something(temps, times, 'median')

plotwinds, plotdates, plotyears, plotaverages_winds = average_something(wind, times, 'median')

plt.figure(dpi=360)
plt.plot(plotdates, plottemps, "k")
plt.xlabel("Date")
plt.ylabel(r'Average temp$^{\circ}$')
plt.title("Mean temperatures of every day in year")
plt.show()


plt.figure(dpi=360)
plt.plot(range(365),plotaverages_temp)
plt.xlabel("Day in year")
plt.ylabel(r'Temp$^{\circ}$')
plt.title("Temperature profile for year based on all years")
plt.show()


plt.figure(dpi=360)
plt.plot(plotdates, plotwinds, "k.")
plt.xlabel("Day in year")
plt.ylabel("avg. wind speed")
plt.title("Mean wind speeds of every day in year")
plt.show()

#blue-winter
#green-spring
#yellow-summer
#orange-fall]]#
plt.figure(dpi=360)
plt.bar(np.arange(0,58+1,1), plotaverages_winds[0:58+1],color='b',label="winter")
plt.bar(np.arange(60,151+1,1), plotaverages_winds[60:151+1], color='g',label="spring" )
plt.bar(np.arange(152,243+1,1), plotaverages_winds[152:243+1],color='y',label="summer")
plt.bar(np.arange(244,334+1,1), plotaverages_winds[244:334+1],color='orange',label="fall")
plt.bar(np.arange(335,364+1,1), plotaverages_winds[335:364+1],color='b')
plt.legend()
plt.xlabel("Days in a year")
plt.ylabel(r'Wind speed in kmh$^-1$')
plt.title("Wind speed profile for year based on all years")
plt.show()