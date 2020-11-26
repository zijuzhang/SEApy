# scenario.py
#
# Input file, defines scenario options
#
# Rahul Kalampattel
# Created: 26/11/2020
# Updated: 26/11/2020

import numpy as np

# TX properties
tx_depth = 15           # m
tx_frequency = 20000    # Hz
tx_source_level = 200   # dB
tx_speed_range = 20     # knots
tx_beampattern = np.array([
    [-180,  10], [-170, -10], [-160,   0], [-150, -20], [-140, -10], [-130, -30],
    [-120, -20], [-110, -40], [-100, -30], [-90 , -50], [-80 , -30], [-70 , -40],
    [-60 , -20], [-50 , -30], [-40 , -10], [-30 , -20], [-20 ,   0], [-10 , -10],
    [  0 ,  10], [ 10 , -10], [ 20 ,   0], [ 30 , -20], [ 40 , -10], [ 50 , -30],
    [ 60 , -20], [ 70 , -40], [ 80 , -30], [ 90 , -50], [100 , -30], [110 , -40],
    [120 , -20], [130 , -30], [140 , -10], [150 , -20], [160 ,   0], [170 , -10],
    [180 ,  10]
])

# RX properties
rx_bandwidth = 10           # dB
rx_depth = 15               # m
rx_detection_threshold = 5  # dB
rx_directivity_index = 10   # dB
rx_range = 2000             # m
