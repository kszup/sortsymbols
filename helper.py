import pandas as pd
from termgraph import termgraph as tg

def open_data(fileName):
    data = pd.read_csv(fileName, sep=",")
    return data

def total_calories(data):
    # Sum up calories by date and then reset the index so that we can continue to work with dataset
    tc = data.groupby(by=["date"])["calories"].sum().reset_index()
    return tc

def cal_plotter(totals,limit):
    # Add arguments for termgraph to plot graph
    args = {'filename': '', 'title': None, 'width': 50,
            'format': '{:<5.2f}', 'suffix': '', 'no_labels': False,
            'color': None, 'vertical': False, 'stacked': True, 'histogram': False,
            'different_scale': False, 'calendar': False, 'start_dt': None, 
            'custom_tick': '', 'delim': '','verbose': True, 'version': False}
    len_categories = 2 
    colors = [94,91]

    # Populate data in format required by termgraph
    labels = []
    caloric_intake = []
    for i in totals.date: labels.append(str(i))
    for i in totals.calories: 
        if i<=limit: caloric_intake.append([i,0])
        if i>limit: caloric_intake.append([limit,i-limit])
    
    # Normalize data so that it will fit in terminal
    normalize_caloric_intake = tg.normalize(caloric_intake, args["width"])
    
    # Finally plot the graph
    tg.stacked_graph(labels, caloric_intake, normalize_caloric_intake, len_categories, args, colors)



