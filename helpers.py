# helpers.py
# by Jacob Wolf, Chris Proctor, Jenny Han, and Krate Ng
# Functions which support summarizing data with a line lab

# =============================================================================
# ☕️ More-Than-You-Need-To-Know Lounge ☕️
# =============================================================================
# Welcome to the More-Than-You-Need-To-Know Lounge, a chill place for code that
# you don't need to understand.

# Thanks for stopping by, we hope you find something that catches your eye.
# But don't worry if this stuff doesn't make sense yet -- as long as we know
# how to use code, we don't have to understand everything about it.

# Of course, if you really like this place, stay a while. You can ask a
# teacher about it if you're interested.
# =============================================================================

import matplotlib.pyplot as plt
import numpy as np


def clamp_point(x, domain):
    """
    Takes a value and a (min, max) domain and returns the value if it is inside the domain, the domain min if the value
    is smaller than the domain, or the domain max if the value is larger than the domain.
    input: int or float, (int or float, int or float)
    output: int or float
    """
    if x < domain[0]:
        return domain[0]
    if x > domain[1]:
        return domain[1]
    return x

def clamp_database(db, x_domain, y_domain):
    """
    Takes the values in df and clamps them to the specified x_domain. For example, let's say x_domain = (0, 100).
    If 4424 was in the df, it would be rewritten as 100. If -2 was in the df, it would be rewritten as 0.
    input: dataframe, tuple
    output: dataframe
    """
    for i in range(len(db)):
        x_clamp = clamp_point(db.iloc[i][0], x_domain)
        y_clamp = clamp_point(db.iloc[i][1], y_domain)
        db.iloc[i, 0] = x_clamp
        db.iloc[i, 1] = y_clamp
    return db

def create_graph(x_label, y_label):
    """
    Creates a pyplot graph with bottom left corner (0,0) and top right corner (1,1). Sets the axeses labels
    based on x_label and y_label. Returns the axes so it can be added to by future function calls.
    input: sting, string
    output: matplotlib Axes
    """
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    return ax

def jitter_list(values, standard_deviation=None):
    """
    Adds normally distributed jitter to a single-dimensional list of values for the purpose of plotting ordinal
    or categorical values.
    input: list, float
    output: list
    """
    jitter = np.random.normal(scale=standard_deviation or np.sqrt(np.std(values)), size=len(values))
    jitter_list = [values[i]+jitter[i] for i in range(len(values))]
    return jitter_list


def draw(data_points_list, ax, jitter = False):
    """
    Plots the points on a matplotlib Axes ax. Data points list should be something like
    [[10, 30], [45, 55], [-20, 10]]. Optionally addes jitter to the list to make the magnitude
    of ordinal or categorical values more obvious in the plot.
    input: list, matplotlib Axes, optional boolean
    output: none
    """
    x, y = zip(*data_points_list)
    if jitter:
        x = jitter_list(x, 0.1)
        y = jitter_list(y, 0.1)
    ax.scatter(x, y, alpha=0.5)

def draw_line(slope, y_intercept, ax):
    """
    Draws a line with the given slope and y-intercept.
    If you have already drawn a scatter plot, will draw the line over that graph.
    input: int or float, int or float, matplotlib Axes
    output: none
    """
    xmin, xmax = plt.xlim()
    ax.plot([xmin, xmax], [y_intercept + slope * xmin, y_intercept + slope * xmax])


def add_loss(loss, ax):
    """
    Adds text to a matplotlib Axes ax to display the loss of a regression line. Text is
    position just outside the plot bounds in the top right corner.
    input: int or float, matplotlib Axes
    output: none
    """
    ax.text(1.05,.95,'loss: {}'.format(loss), bbox=dict(facecolor='red', alpha=0.5), horizontalalignment='left', verticalalignment='top', transform=ax.transAxes)
