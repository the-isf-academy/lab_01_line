import matplotlib.pyplot as plt
import numpy as np


def clamp_point(x, domain):
    if x < domain[0]:
        return domain[0]
    if x > domain[1]:
        return domain[1]
    return x

def clamp_database(db, x_domain, y_domain):
    for i in range(len(db)):
        x_clamp = clamp_point(db.iloc[i][0], x_domain)
        y_clamp = clamp_point(db.iloc[i][1], y_domain)
        db.iloc[i, 0] = x_clamp
        db.iloc[i, 1] = y_clamp
    return db

def create_graph(x_label, y_label):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    return ax

def jitter_list(values, standard_deviation=None):
    jitter = np.random.normal(scale=standard_deviation or np.sqrt(np.std(values)), size=len(values))
    jitter_list = [values[i]+jitter[i] for i in range(len(values))]
    return jitter_list


def draw(data_points_list, ax):
    """
    Plots the points. Data points list should be something like
    [[10, 30], [45, 55], [-20, 10]]
    """
    x, y = zip(*data_points_list)
    jitter_x = jitter_list(x, 0.1)
    jitter_y = jitter_list(y, 0.1)
    ax.scatter(jitter_x, jitter_y, alpha=0.5)

def draw_line(slope, y_intercept, ax):
    """
    Draws a line with the given slope and y-intercept.
    If you have already drawn a scatter plot, will draw the line over that graph.
    """
    xmin, xmax = plt.xlim()
    ax.plot([xmin, xmax], [y_intercept + slope * xmin, y_intercept + slope * xmax])


def add_loss(loss, ax):
    ax.text(1.05,.95,'loss: {}'.format(loss), bbox=dict(facecolor='red', alpha=0.5), horizontalalignment='left', verticalalignment='top', transform=ax.transAxes)
