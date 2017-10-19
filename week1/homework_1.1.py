import sys

CITIES = { 'Los Angeles': 'losangeles',
 'Chicago': 'chicago',
 'Honolulu': 'honolulu',
 'New York': 'newyork' }


def main():
    city = validate_city()
    city_data = open_file(city)
    calculate_stats(city_data)


def validate_city():
    city = sys.argv[1]
    if city in CITIES:
        print "Summary of 2016 weather data (in degrees F) for ", city
        return city
    else:
        print "I'm sorry but I don't recognize the city you entered."


def open_file(city):
    # city weather data file locations
    filename_template = 'weather_%s.csv' % CITIES[city]

    fh = open(filename_template)
    # skip the first line (csv header)
    lines = fh.readlines()[1:]
    fh.close()

    return lines


def calculate_stats(city_data):
    # temp variables to be used while looping
    sum_of_means = 0
    count_of_means = 0
    means = []

    # loop over each line in city_data
    for line in city_data:
        items = line.split(',')
        # the mean is the third item a string
        mean = items[2]
        means.append(mean)
        sum_of_means += int(mean)
        count_of_means += 1

    minimum_temp = min(means)
    maximum_temp = max(means)
    average_temp = sum_of_means / count_of_means

    # find standard_deviation
    sd = _calculate_standard_deviation(means, average_temp)

    print "average_temp: ", average_temp
    print "minimum_temp: ", minimum_temp
    print "maximum_temp: ", maximum_temp
    print "standard_deviation: ", sd


def _calculate_standard_deviation(data, mean_of_list):
    sum_of_differences_squared = 0
    count = 0

    for item in data:
        difference = abs(int(item) - mean_of_list)
        sum_of_differences_squared += difference ** 2
        count += 1

    # calculate the variance
    variance = sum_of_differences_squared / count
    sd = variance ** 0.5

    return sd


main()