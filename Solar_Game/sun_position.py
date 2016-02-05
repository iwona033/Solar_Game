import numpy as np

def calc_declination(day):
    delta = np.deg2rad(23.45) * np.sin(np.deg2rad((360.0/365) * (day - 81)))
    return delta

def calc_deltaT_GMT(longitude):
    deltaT_GMT = 24.0 * longitude/360.0
    return deltaT_GMT
    

def calc_B(day):
    B = np.deg2rad((360/365) * (day - 81))
    return B

def calc_EoT(day):
    EoT = 9.87 * np.sin(2 * calc_B(day)) - 7.53 * np.cos(calc_B(day)) - 1.5 * np.sin(calc_B(day))
    return EoT

def calc_LSTM(longitude):
    LSTM = 15 * calc_deltaT_GMT(longitude)
    return LSTM

def calc_TC(longitude, day):
    TC = 4 * (longitude - calc_LSTM(longitude)) + calc_EoT(day)
    return TC

def calc_LST(longitude, day, LT):
    LST = LT + calc_TC(longitude, day)/360
    return LST


def calc_HRA(longitude, day, LT):
    HRA = np.deg2rad(15) * (calc_LST(longitude, day, LT) - 12)
    return HRA


def calc_elevation(latitude, longitude, day, LT):
    delta = calc_declination(day)
    phi = np.deg2rad(latitude)
    HRA = calc_HRA(longitude, day, LT)
    elevation = np.arcsin(np.sin(delta) * np.sin(phi) + np.cos(delta) * np.cos(phi) * np.cos(HRA))
    return elevation

def elevation_to_panel_angle(elevation):
    panel_angle = 90 - elevation
    return panel_angle

def calc_panel_angle(latitude, longitude, day, LT):
    elevation = np.rad2deg(calc_elevation(latitude, longitude, day, LT))
    panel_angle = elevation_to_panel_angle(elevaation)
    return panel_angle