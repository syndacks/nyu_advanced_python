#!/usr/bin/env python3

""" homework_1.1.py:  calculate average, max, min and standard deviation
    for a year's worth of data pulled from the Weather Underground
    2017-10-03  David Blaikie (dbb212@nyu.edu)      """

import pytest
import sys

DEBUG = True                           # when development is complete,
                                        # set to False


FILENAME_TEMPLATE = 'weather_{}.csv'

CITIES = { 'Los Angeles': 'losangeles',
           'Chicago':     'chicago',
           'Honolulu':    'honolulu',
           'New York':    'newyork' }


def validate_input(args):
    """ read symbol from command line arguments;
        if no arg is offered, raise IndexError
        if year is not 4 digits, raise ValueError """

    try:
        city = args[1]
    except IndexError:
        # re-raising the exception, but adding a descriptive message
        raise IndexError('please enter a city')

    if not city in CITIES:
        raise ValueError('city "{}" must be in cities: {}'.format(city, ', '.join(CITIES)))

    return CITIES[city]

#------TEST------#
def test_validate_input():
    """tests for validate_input"""

    # assert the four main cities return proper CITIES dict values
    assert validate_input(['foo.py', 'Chicago']) == 'chicago'
    assert validate_input(['foo.py', 'Los Angeles']) == 'losangeles'
    assert validate_input(['foo.py', 'Honolulu']) == 'honolulu'
    assert validate_input(['foo.py', 'New York']) == 'newyork'
    # no city passed as arg
    with pytest.raises(IndexError):
        validate_input(['foo.py'])
    # incorrect city name
    with pytest.raises(ValueError):
        validate_input(['foo.py', 'LosAngeles'])
    with pytest.raises(ValueError):
        validate_input(['foo.py', 'Brooklyn'])


def acquire_data(city):
    """  given a city, read corresponding file
         and return data without header line    """

    filename = FILENAME_TEMPLATE.format(city)

    text = open(filename).read()
    lines = text.splitlines()

    data_lines = lines[1:]

    return data_lines


#------TEST------#
def test_acquire_data():
    """tests for acquire_data"""

    # should return an array of data
    assert type(acquire_data("chicago")) == list
    # should have at least 100 data points
    assert len(acquire_data("newyork")) > 100


def get_data_from_lines(data_lines):
    """ given data lines from file, isolate the column of interest
        return a list of int values """

    temps = []
    for line in data_lines:
        fields = line.split(',')
        temp = int(fields[2])
        temps.append(temp)
    return temps


#------TEST------#
def test_get_data_from_lines():
    """test for get_data_from_lines"""

    mocked_data_lines = ['2016-1-1,31,26,20,22,17,11,72,66,53,30.27,30.21,30.14,10,10,6,24,15,30,T,5,Snow,250',
                         '2016-1-2,33,28,22,23,19,16,78,66,52,30.17,30.09,29.98,10,10,10,22,12,30,0.00,1,,251']
    # assert that we are picking the temp data at index 2
    assert get_data_from_lines(mocked_data_lines) == [26, 28]


def calculate_avg_min_max(temps):
    """ calculate average temp from data """

    temp_average = sum(temps) / len(temps)
    return temp_average, min(temps), max(temps)


#------TEST------#
def test_calculate_avg_min_max():
    """tets for calculate_avg_min_max"""

    mocked_temps = [26, 29]
    # assert that we are getting the average, min, max of mocked_temps
    assert calculate_avg_min_max(mocked_temps) == (27.5, 26, 29)


def calculate_std_dev(temps, temp_average):
    print ("std_dev_temps", temps)
    print ("std_dev_temp_average", temp_average)
    """ given a list of temps and their average, calculate variance """

    variance_sum = 0
    for temp in temps:
        variance = (temp - temp_average) ** 2
        variance_sum += variance

    variance = variance_sum / len(temps)
    standard_deviation = variance ** 0.5

    return standard_deviation


#------TEST------#
def test_calculate_std_dev():
    """tests for calculate_std_dev"""

    mocked_temps = [26, 28, 28, 29, 28, 32, 40, 43, 36, 16, 14, 14, 16, 37, 38, 23, 8, 4, 10, 19, 24, 27, 30, 31, 36, 33, 31, 36, 31, 43, 42, 39, 38, 34, 27, 31, 34, 40, 29, 19, 15, 17, 17, 12, 16, 24, 32, 32, 34, 54, 51, 40, 37, 39, 36, 35, 32, 42, 51, 43, 27, 24, 31, 31, 35, 44, 55, 66, 59, 47, 45, 49, 47, 49, 56, 53, 51, 43, 42, 39, 41, 56, 43, 36, 38, 45, 54, 46, 48, 54, 58, 44, 36, 51, 35, 38, 47, 39, 37, 31, 43, 46, 40, 47, 51, 57, 63, 66, 68, 55, 64, 64, 51, 51, 63, 73, 58, 47, 48, 48, 48, 48, 51, 55, 52, 52, 65, 60, 57, 56, 63, 62, 63, 56, 46, 48, 59, 53, 56, 57, 61, 66, 66, 69, 77, 78, 75, 77, 77, 73, 76, 75, 73, 71, 74, 71, 72, 73, 62, 62, 66, 80, 84, 71, 74, 79, 81, 73, 75, 76, 81, 83, 76, 73, 74, 75, 81, 83, 81, 67, 68, 72, 69, 68, 70, 74, 79, 79, 78, 79, 73, 74, 83, 83, 79, 79, 71, 70, 77, 79, 79, 82, 83, 83, 82, 84, 81, 80, 81, 78, 76, 75, 75, 77, 81, 82, 84, 81, 75, 75, 80, 81, 83, 86, 80, 80, 77, 75, 79, 80, 79, 78, 74, 69, 69, 74, 79, 78, 75, 78, 79, 82, 80, 74, 70, 70, 69, 72, 79, 85, 85, 77, 75, 69, 66, 71, 76, 71, 71, 75, 75, 73, 76, 78, 73, 77, 73, 72, 76, 65, 63, 58, 64, 64, 62, 63, 64, 69, 73, 69, 61, 55, 57, 62, 68, 58, 50, 56, 63, 69, 77, 68, 63, 54, 48, 50, 60, 50, 48, 49, 48, 55, 66, 51, 51, 70, 62, 59, 55, 58, 59, 58, 58, 51, 54, 49, 44, 47, 51, 47, 51, 62, 53, 35, 31, 34, 36, 42, 41, 38, 41, 41, 48, 52, 42, 40, 38, 33, 33, 34, 34, 27, 22, 23, 23, 30, 24, 15, 13, 6, 17, 23, 8, 5, 23, 30, 33, 33, 36, 38, 43, 29, 34, 34, 31, 35]
    mocked_temp_avgerage = 54.73224043715847
    # assert we are getting the standard deviation of mocked_temps and mocked_temp_avgerage
    assert calculate_std_dev(mocked_temps, mocked_temp_avgerage) == 20.086544959824828


def report_temps(city, temp_average, temp_max, temp_min, std_dev):
    """ given all elements to be repoted, print them """

    print('Summary of daily temperature data for {} in year 2016:'.format(city))
    print('Average temp:  {}'.format(temp_average))
    print('Max temp:  {}'.format(temp_max))
    print('Min temp:  {}'.format(temp_min))
    print('Standard deviation:  {}'.format(std_dev))


#------TEST------#
def test_report_temps():
    """test for report tempts"""
    report_temps('Chicago', 53, 89, 13, 20)
    with pytest.raises(TypeError):
        report_temps('Chicago', 53, 89, 13, 20, 20)


def main():
    """ the main event """

    city =         validate_input(sys.argv)
    data_lines =   acquire_data(city)
    data =         get_data_from_lines(data_lines)
    temp_average, temp_min, temp_max = calculate_avg_min_max(data)
    temp_std_dev = calculate_std_dev(data, temp_average)

    report_temps(city, temp_average, temp_max, temp_min, temp_std_dev)




if __name__ == '__main__':

    try:
        main()
    except Exception as e:    # can trap any exception
        if DEBUG:             # if DEBUG flag is True,
            raise             # re-raises caught exception
        else:
            exit(e.args[0])   # otherwise exits with exception message
