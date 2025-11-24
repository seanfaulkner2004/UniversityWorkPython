'''Assignment 2
SEAN FAULKNER COSC-131-S1
Part 2'''
import numpy as np
import matplotlib.pyplot as plt


def data_tuple_from_line(line_str):
    """Creates a tuple from a line of string"""
    in_id,in_date,size,cost,subsidy,zip_code,city,state = line_str.split(',')
    city = city.title()
    size = float(size)
    cost = float(cost)
    subsidy = float(subsidy)
    result = (in_id,in_date,size,cost,subsidy,zip_code,city,state)
    return result


def is_valid_line_data(line_data_tuple):
    """Checks whether all the values of the data is valid"""
    result = True
    for data in line_data_tuple:
        if data == -1 or data == '-1':
            result = False
    return result


def read_solar_data(filename):
    """Reads a file of infomation on solar data"""
    infile = open(filename)
    data = infile.read()
    infile.close()
    contents = data.splitlines()
    contents = contents[1:]
    valid_entrys = []
    for content in contents:
        solar_data = data_tuple_from_line(content)
        if is_valid_line_data(solar_data) == True:
            valid_entrys.append(solar_data)
    return valid_entrys


def installs_by_state(solar_data):
    """Counts the amount of solar installations per state"""
    counts = dict()
    for data in solar_data:
        in_id,in_date,size,cost,subsidy,zip_code,city,state = data
        if state in counts:
            counts[state] +=1
        else:
            counts[state] = 1
    return counts


def installs_by_year(solar_data):
    """Counts the amount of solar installations per year"""
    counts = dict()
    for data in solar_data:
        in_id,in_date,size,cost,subsidy,zip_code,city,state = data
        year, month, day = in_date.split('-')
        year = int(year)
        if year in counts:
            counts[year] +=1
        else:
            counts[year] = 1
    return counts


def total_kw_by_year(solar_data):
    """Finds the total size of solar installations per year"""
    counts = dict()
    for data in solar_data:
        in_id,in_date,size,cost,subsidy,zip_code,city,state = data
        year, month, day = in_date.split('-')
        year = int(year)
        size = float(size)
        if year in counts:
            counts[year] += size
        else:
            counts[year] = size
    return counts


def cost_of_installations_per_year(solar_data):
    """Finds the total cost of solar installations per year"""
    counts = dict()
    for data in solar_data:
        in_id,in_date,size,cost,subsidy,zip_code,city,state = data
        year, month, day = in_date.split('-')
        year = int(year)
        cost = float(cost)
        subsidy = float(subsidy)
        total = cost - subsidy
        if year in counts:
            counts[year] += total
        else:
            counts[year] = total
    return counts


def first_step(solar_data):
    """sdfkjdfvbkgh"""
    first_dict = dict()
    for data in solar_data:
        in_id,in_date,size,cost,subsidy,zip_code,city,state = data
        year, month, day = in_date.split('-')
        year = int(year)
        size = float(size)
        cost = float(cost)
        subsidy = float(subsidy)
        if year in first_dict:
            first_dict[year].append((size, cost, subsidy))
        else:
            first_dict[year] = [(size, cost, subsidy)]
    return first_dict


def second_step(first_dict):
    """sdkfvuhdfevgky"""
    second_dict = dict()
    for year, values in first_dict.items():
        num_of_installs = 0
        average_net_cost = 0
        for value in values:
            num_of_installs += 1
            total_kw, cost, subsidy = value
            total_cost = cost - subsidy
            net_cost = total_cost/total_kw
            average_net_cost += net_cost
        average_net_cost_per_year = average_net_cost/num_of_installs
        second_dict[year] = average_net_cost_per_year
    return second_dict


def average_net_cost_per_kw_by_year(solar_data):
    """Finds the average net cost per solar installation per year"""
    first_dict = first_step(solar_data)
    second_dict = second_step(first_dict)
    return second_dict


def bar_graph_from_dict(data_dict, title, xlabel, ylabel):
    """Plots a bar graph from a provided dictionary"""
    xs = []
    ys = []
    for key in sorted(data_dict.keys()):
        xs.append(key)
    for item in xs:
        value = data_dict[item]
        ys.append(value)    
    xs = np.array(xs)
    ys = np.array(ys)
    x_ticks = xs
    axes = plt.axes()
    axes.bar(xs,ys,color='darkgreen')
    axes.set_title(title)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_xticks(x_ticks)
    axes.set_xticklabels(xs)
    plt.show()


def plot_from_dict(data_dict, title, xlabel, ylabel):
    """Plots a graph with provided dictionary"""
    xs = []
    ys = []
    for key in sorted(data_dict.keys()):
        xs.append(key)
    for item in xs:
        value = data_dict[item]
        ys.append(value)    
    xs = np.array(xs)
    ys = np.array(ys)
    x_ticks = xs
    axes = plt.axes()
    axes.plot(xs,ys,marker='o',linestyle='-',color='darkgreen')
    axes.set_title(title)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_xticks(x_ticks)
    axes.set_xticklabels(xs, rotation=90)
    axes.grid(True)
    plt.tight_layout()
    plt.show()


def plot_yearly_installs_vs_costs(cost_dict, installs_dict):
    """Plots the average cost per year against yearly 
    number of installations"""
    xs_keys = []
    ys_keys = []
    xs = []
    ys = []
    for key in sorted(cost_dict.keys()):
        xs_keys.append(key)
    for key in xs_keys:
        value = cost_dict[key]
        xs.append(value)
    for key in sorted(installs_dict.keys()):
        ys_keys.append(key)
    for key in ys_keys:
        value = installs_dict[key]
        ys.append(value)
    xs = np.array(xs)
    ys = np.array(ys)
    axes = plt.axes()
    axes.plot(xs,ys,linestyle='',color='darkgreen',marker='o')
    axes.set_title('Installs vs Average cost per kW')
    axes.set_xlabel('Average net cost ($/kW)')
    axes.set_ylabel('Yearly number of installs')
    axes.grid(True)
    plt.tight_layout()
    plt.show


def fit_line_to_installs_vs_year(yearly_installs_dict, last_year_to_include):
    """Fits a trendline to the function yearly number of installations"""
    xs = []
    ys = []
    for key in sorted(yearly_installs_dict.keys()):
        if key <=last_year_to_include:
            xs.append(key)
    for item in xs:
        value = yearly_installs_dict[item]
        ys.append(value) 
    xs = np.array(xs)
    ys = np.array(ys)
    x_ticks = xs
    a, b = np.polyfit(xs, np.log(ys), 1)
    y_bst = np.exp((a*xs)+b)
    axes = plt.axes()
    axes.plot(xs,ys,marker='o',linestyle='-',color='darkgreen',label='actual')
    axes.plot(xs,y_bst,color='orange',linestyle='--',marker='+',label='fitted')
    axes.set_title(f'Installs up to {last_year_to_include}')
    axes.set_xlabel('Year')
    axes.set_ylabel('Yearly number of installs')
    axes.set_xticks(x_ticks)
    axes.set_xticklabels(xs, rotation=90)
    axes.grid(True)
    axes.legend()
    plt.tight_layout()
    plt.show()
    
solar_data = read_solar_data('data_500_a.txt')
data_dict = installs_by_state(solar_data)
bar_graph_from_dict(data_dict, 'Installs by state', 'State', 'Number of installs')