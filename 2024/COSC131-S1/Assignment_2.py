'''Assignment 2
SEAN FAULKNER COSC-131-S1
Part 1'''
import numpy as np
import matplotlib.pyplot as plt
import datetime
YEARS = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]

def cos_d(degrees):
    """ To save us converting to radians all the time """
    return np.cos(np.radians(degrees))


def sin_d(degrees):
    """ To save us converting to radians all the time """
    return np.sin(np.radians(degrees))


def asin_d(n):
    """ Returns the degrees such that sin(degrees) == n 
    This is also know as the inverse sin function or arcsin.
    The stanard asin function returns the value in radians.
    This function converts the result to degrees
    """
    return np.degrees(np.arcsin(n))


def times_across_day(number_of_times):
    """Number of times taken in a day"""
    return np.linspace(0,24,number_of_times)


def nice_date_str(day_num):
    """ Returns a human readable date string for the date that is
    day_num days after 1 Jan 2023. For example, 
    day 0 is 01 Jan and day 364 is 31 Dec
    The day number should be and int value between 0 and 364, inclusive.
    NOTE: day_num must be an int (not a float or np.int64 etc).
    We are using 2023 so that it's not a leap year - to keep things simple.
    Values greater than 364 will roll over into subsequent years!
    Don't worry too much about how this works.
    """
    base_date = datetime.date(2023, 1, 1)
    delta = datetime.timedelta(days=day_num)
    the_date = base_date + delta
    return the_date.strftime('%d %b')


def solar_declination(day_num, solar_hour):
    """ Returns the angle of the sun's rays and the
    plane of the earth's equator, for the given day
    number and solar hour.
    """
    n = day_num + solar_hour / 24
    beta = 360/365 * (n + 10)
    return -23.44 * cos_d(beta)


def solar_hour_angle(solar_hour):
    """ This function returns the angle implied by
    a given hourly time, relative to the solar noon.
    For hours before noon (12) the angle should be
    negative and for hours after noon it should be
    positive.
    """
    return 15 * (solar_hour - 12)


def solar_elevation(latitude, day_num, solar_hour):
    """ Returns the elevation of the sun relative to the ground """
    hour_angle = solar_hour_angle(solar_hour)
    declination = solar_declination(day_num, solar_hour)
    elevation = asin_d(sin_d(latitude) * sin_d(declination) +
                 cos_d(latitude) * cos_d(hour_angle) * cos_d(declination))
    return elevation


def plot_elevations_over_day(latitude, day_num, number_of_points):
    """Plots a graph which projects the path of the sun across a certian
    latitude"""
    date = nice_date_str(day_num)
    solar_hour = times_across_day(number_of_points)
    y_ticks = np.arange(-90,91,10)
    x_ticks = np.arange(0,25,1)
    ys = solar_elevation(latitude, day_num, solar_hour)
    xs = solar_hour
    axes = plt.axes()
    axes.plot(xs,ys, marker ='o', linestyle = '', color = 'orange' )
    axes.set_title(f'Solar elevations for day={date}, latitude={latitude:.2f}')
    axes.set_ylabel('Solar elevation (degrees)')
    axes.set_xlabel('Solar hour')
    axes.set_xticks(x_ticks)
    axes.set_xticklabels(x_ticks)
    axes.set_yticks(y_ticks)
    axes.set_yticklabels(y_ticks)
    axes.grid(True)
    plt.show()


def multi_plot_elevations_over_day(latitude, day_nums, number_of_points):
    """Plots multiple graphs of elevations over list of days"""
    solar_hour = times_across_day(number_of_points)
    y_ticks = np.arange(-90,91,10)
    x_ticks = np.arange(0,25,1)
    xs = solar_hour
    axes = plt.axes()
    for day_num in day_nums:
        date = nice_date_str(day_num)
        ys = solar_elevation(latitude, day_num, solar_hour) 
        axes.plot(xs,ys, marker = None, linestyle = '-', label = date)
    axes.set_title(f'Solar elevations for latitude={latitude:.2f}')
    axes.set_ylabel('Solar elevation (degrees)')
    axes.set_xlabel('Solar hour')
    axes.set_xticks(x_ticks)
    axes.set_xticklabels(x_ticks)
    axes.set_yticks(y_ticks)
    axes.set_yticklabels(y_ticks)
    axes.legend()
    axes.grid(True)
    plt.show()


def plot_noon_elevations_over_year(latitude):
    """Plots the elevation at noon for each day of the year at a provided
    latitude"""
    xs = np.arange(0,365,1)
    ys = solar_elevation(latitude, xs, 12)
    x_ticks = np.arange(0, 361, 30)
    y_ticks = np.arange(-90,91,10)
    x_tick_labels = [0,30,60,90,120,150,180,210,240,270,300,330,360]
    day_strings = []
    i=0
    while i<len(x_tick_labels):
        x_tick_label = x_tick_labels[i]
        date = nice_date_str(x_tick_label)
        day_strings.append(date)
        i+=1
    axes = plt.axes()
    axes.plot(xs,ys,linestyle = '-', color = 'orange')
    axes.set_title(f'Daily noon solar elevations at latitude={latitude:.2f}')
    axes.set_ylabel('Noon solar elevation (degrees)')
    axes.set_xlabel('Day')
    axes.set_xticks(x_ticks)
    axes.set_xticklabels(day_strings, rotation=90)
    axes.set_yticks(y_ticks)
    axes.set_yticklabels(y_ticks)
    axes.grid(True)
    plt.tight_layout()
    plt.show()


def multi_plot_noon_elevations_over_year(latitudes):
    """Plots multiple graphs of elevation at noon for each day of the year over
    a list of multiple latitudes"""
    xs = np.arange(0,365,1)
    axes = plt.axes()
    for latitude in latitudes:
        ys = solar_elevation(latitude, xs, 12)
        axes.plot(xs,ys,linestyle = '-', label = f'lat={latitude:.2f}')
    x_ticks = np.arange(0, 361, 30)
    y_ticks = np.arange(-90,91,10)
    x_tick_labels = [0,30,60,90,120,150,180,210,240,270,300,330,360]
    day_strings = []
    i=0
    while i<len(x_tick_labels):
        x_tick_label = x_tick_labels[i]
        date = nice_date_str(x_tick_label)
        day_strings.append(date)
        i+=1
    axes.set_title('Daily noon solar elevations')
    axes.set_ylabel('Noon solar elevation (degrees)')
    axes.set_xlabel('Day')
    axes.set_xticks(x_ticks)
    axes.set_xticklabels(day_strings, rotation=90)
    axes.set_yticks(y_ticks)
    axes.set_yticklabels(y_ticks)
    axes.grid(True)
    axes.legend()
    plt.tight_layout()
    plt.show()


def num_daylight_values(elevations):
    """Returns the amount of values above zero"""
    return len(elevations[elevations>0])

multi_plot_noon_elevations_over_year([-90, -60, -30, 0])