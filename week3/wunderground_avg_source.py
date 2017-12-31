#!/usr/bin/env python3

""" homework_1.1.py:  calculate average, max, min and standard deviation
    for a year's worth of data pulled from the Weather Underground
    2017-10-03  David Blaikie (dbb212@nyu.edu)      """

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


def _test_main():
    # tests for validate_input
    assert validate_input('Los Angeles') == 'losangeless'


def acquire_data(city):
    """  given a city, read corresponding file
         and return data without header line    """

    filename = FILENAME_TEMPLATE.format(city)

    text = open(filename).read()
    lines = text.splitlines()

    data_lines = lines[1:]

    return data_lines


def get_data_from_lines(data_lines):
    """ given data lines from file, isolate the column of interest
        return a list of int values """

    temps = []
    for line in data_lines:
        fields = line.split(',')
        temp = int(fields[2])
        temps.append(temp)
    return temps


def calculate_avg_min_max(temps):
    """ calculate average temp from data """

    temp_average = sum(temps) / len(temps)
    return temp_average, min(temps), max(temps)


def calculate_std_dev(temps, temp_average):
    """ given a list of temps and their average, calculate variance """

    variance_sum = 0
    for temp in temps:
        variance = (temp - temp_average) ** 2
        variance_sum += variance

    variance = variance_sum / len(temps)
    standard_deviation = variance ** 0.5

    return standard_deviation


def report_temps(city, temp_average, temp_max, temp_min, std_dev):
    """ given all elements to be repoted, print them """

    print('Summary of daily temperature data for {} in year 2016:'.format(city))
    print('Average temp:  {}'.format(temp_average))
    print('Max temp:  {}'.format(temp_max))
    print('Min temp:  {}'.format(temp_min))
    print('Standard deviation:  {}'.format(std_dev))


def main():
    """ the main event """

    city =         validate_input(sys.argv)
    data_lines =   acquire_data(city)
    data =         get_data_from_lines(data_lines)
    temp_average, temp_min, temp_max = calculate_avg_min_max(data)
    temp_std_dev = calculate_std_dev(data, temp_average)

    report_temps(city, temp_average, temp_max, temp_min, temp_std_dev)

    _test_main()




if __name__ == '__main__':

    try:
        main()
    except Exception as e:    # can trap any exception
        if DEBUG:             # if DEBUG flag is True,
            raise             # re-raises caught exception
        else:
            exit(e.args[0])   # otherwise exits with exception message
