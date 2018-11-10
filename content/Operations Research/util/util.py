# -*- coding: utf-8 -*-
# ---------------------------------------
# Author: Hadir Alexander Garcia Castro
# Author e-mail: hadir.ga@outlook.com
# Date: March 24th, 2018 - May 13th, 2018
#
# Copyright (C) 2018, hadir.ga
# All rights reserved.
# Apache License, Version 2.0 (see LICENSE.lic for details)
# ---------------------------------------

import os
from math import sqrt, floor
from datetime import datetime


def euclidean_distance(x0, y0, x1, y1, scale=1):
    """
    Calculate the euclidean distance between two (x,y) points and
    multiply it by a scale factor, all positive integers.
    
    :param x0: dimension x of first point.
    :param y0: dimension y of first point.
    :param x1: dimension x of second point.
    :param y1: dimension y of second point.
    :param scale: multiplier scale, 1 as default.
    :return distance:
    """
    # if not (x0 >= 0 or y0 >= 0 or x1 >= 0 or y1 >= 0):
    if x0 < 0 or y0 < 0 or x1 < 0 or y1 < 0:
        raise Exception("(x, y) dimensions out of range")

    if not scale > 0:
        raise Exception("Scale is out of range")

    distance = sqrt((x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1))
    scaled_distance = int(floor(distance * scale))

    return scaled_distance


def mtx_distance(xlat, ylng, scale):
    """
    Calculates the distance matrix between each pair of nodes.
    It is a matrix of [V]x[V].
    
    Parameters
        xlat: list of int
            x dimension representing latitude coordinates
        ylng: list of int
            y dimension representing longitude coordinates
    :return mtx
    """
    # Number of nodes
    size_nodes = len(xlat)

    # Matrix of distances initialization
    mtx = [[0 for j in range(size_nodes)] for i in range(size_nodes)]

    for i in range(size_nodes):
        for j in range(i, size_nodes):
            if i == j:
                mtx[i][j] = 0
            else:
                mtx[i][j] = euclidean_distance(xlat[i], ylng[i],
                                               xlat[j], ylng[j],
                                               scale=scale)
                mtx[j][i] = mtx[i][j]
    return mtx


def read_file(instance_name):
    """
    Read a text file into the instance folder.
    :param instance_name:
    :return data: 2D array with separated data [row, column]
    """
    path = os.path.abspath("./instances/{}/{}".format(instance_name, instance_name))
    file = open(path, "rt")
    file_lines = file.read().splitlines()
    file.close()
    file_data = []  # create array to separate columns
    for line in file_lines:
        file_data.append(line.split())  # split lines into columns

    return file_data


def draw_graph(instance, solution):
    """
    This is to drawing the network graph.
    """
    import matplotlib.pyplot as plt
    import networkx as nx
    
    n = instance.nnodes
    seq = solution.sequence

    # Create the graph
    G = nx.Graph()

    # Create the nodes and their positions
    V = {i: (instance.xlng[i], instance.ylat[i]) for i in range(n)}
    G.add_nodes_from(V)

    Vlabels = {i: "{}:{}".format(i, V[i]) for i in range(n)}

    # Create the graph"s edges
    E = {(seq[i], seq[i+1]): (seq[i], seq[i+1]) for i in range(n)}
    G.add_edges_from(E)

    # Draw the graph
    nx.draw_networkx_nodes(G, pos=V, node_size=100, node_color="r", node_shape="o")
    nx.draw_networkx_labels(G, pos=V, labels=Vlabels, font_size=5)
    nx.draw_networkx_edges(G, pos=V, edgelist=E)

    # axis
    min_x = min(instance.x_lng)
    max_x = max(instance.x_lng)
    min_y = min(instance.y_lat)
    max_y = max(instance.y_lat)

    plt.axis([min_x - 10, max_x + 10,
              min_y - 10, max_y + 10])

    ax = plt.gca()
    ax.axes.get_xaxis().set_ticklabels([])
    ax.axes.get_yaxis().set_ticklabels([])

    # The title
    plt.title("{}::{}".format(instance.name, solution.type))
    # plt.text(0.1, 10.5, "text graph")
    plt.tight_layout()

    # Save and close
    plt.savefig(r"../solution/tsp/{date}_{ID}_{name}_{sol_type}.pdf".format(
        date=datetime.now().strftime("%Y%m%d_%H%M%S"), ID=instance.ID,
        name=instance.name, sol_type=solution.type))
    plt.show()
    plt.close()

    del nx, plt


#EOF
