# -*- coding: utf-8 -*-
# ---------------------------------------
# AUTHOR: Hadir Garcia-Castro
# E-MAIL: hadir.garcia@usp.br
# DATE: March 24th, 2018 - May 13th, 2018
# Copyright (C) 2018, hadir.ga
# All rights reserved.
# MIT License (see LICENSE.lic for details)
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
    path = os.path.abspath("/lin105.tsp/lin105.tsp".format(instance_name, instance_name))
    file = open(path, "rt")
    file_lines = file.read().splitlines()
    file.close()
    file_data = []  # create array to separate columns
    for line in file_lines:
        file_data.append(line.split())  # split lines into columns

    return file_data
