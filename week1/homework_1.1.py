import sys

CITIES = { 'Los Angeles': 'losangeles',
 'Chicago': 'chicago',
 'Honolulu': 'honolulu',
 'New York': 'newyork' }

def main():
    city = _validate_city()
    means = _calculate_means(city)


def _validate_city():
    city = sys.argv[1]
    if city in CITIES:
        print "Input city: ", city
        return city
    else:
        print "I'm sorry but I don't recognize the city you entered."


def _calculate_means(city):
    # city weather data file locations
    FILENAME_TEMPLATE = 'weather_%s.csv' % CITIES[city]

    fh = open(FILENAME_TEMPLATE)
    # skip the first line (csv header)
    lines = fh.readlines()[1:]

    # temp variables to be used while looipng
    sum_of_means = 0
    count_of_means = 0
    means = []

    # loop over each line
    for line in lines:
        items = line.split(',')
        # the mean is the third item a string
        mean = items[2]
        # add each mean to the array
        means.append(mean)
        sum_of_means += int(mean)
        count_of_means += 1

    # close the file
    fh.close()

    # variable calculations
    minimum_temp = min(means)
    maximum_temp = max(means)
    average_temp = sum_of_means / count_of_means

    # find standard_deviation
    sd = _calculate_standard_deviation(means, average_temp)

    print "minimum_temp: ", minimum_temp
    print "maximum_temp: ", maximum_temp
    print "average_temp: ", average_temp
    print "standard_deviation: ", sd


def _calculate_standard_deviation(data, mean_of_list):
    print "data: ", data
    print "mean_of_list: ", mean_of_list

    for item in data:
        print item

    sum_of_differences_squared = 0
    count = 0

    for item in data:
        difference = abs(int(item) - mean_of_list)
        sum_of_differences_squared += difference ** 2
        count += 1

    # calcualte the variance
    variance = sum_of_differences_squared / count
    sd = variance ** 0.5

    return sd


main()
