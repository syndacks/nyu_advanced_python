import sys

CITIES = {'Los Angeles': 'losangeles',
            'Chicago': 'chicago',
            'Honolulu': 'honolulu',
            'New York': 'newyork'}


def main():
    city = validate_city()
    city_data = open_file(city)
    report = calculate_stats(city_data)
    print_report(report)


def validate_city():
    city = sys.argv[1]
    try:
        if city in CITIES:
            return city
    except KeyError:
        print "I'm sorry but I don't recognize the city you entered. \
        The options are: Los Angeles, New York, Chicago, or Honolulu."


def open_file(city):
    csv_file = 'weather_%s.csv' % CITIES[city]
    fh = open(csv_file)
    lines = fh.readlines()[1:]
    fh.close()
    return lines


def calculate_stats(city_data):
    # temp variables to be used while looping
    sum_of_means = 0
    count_of_means = 0
    means = []

    for line in city_data:
        items = line.split(',')
        mean = items[2]
        means.append(mean)
        sum_of_means += int(mean)
        count_of_means += 1

    minimum_temp = min(means)
    maximum_temp = max(means)
    average_temp = sum_of_means / count_of_means
    standard_deviation = _calculate_standard_deviation(means, average_temp)

    return {"average_temp": average_temp,
            "minimum_temp": minimum_temp,
            "maximum_temp": maximum_temp,
            "standard_deviation": standard_deviation}

def _calculate_standard_deviation(city_mean_data, mean_of_means):
    sum_of_differences_squared = 0
    count = 0

    for item in city_mean_data:
        difference = abs(int(item) - mean_of_means)
        sum_of_differences_squared += difference ** 2
        count += 1

    variance = sum_of_differences_squared / count
    sd = variance ** 0.5
    return sd


def print_report(report_to_print):
    city = sys.argv[1]

    for stat in report_to_print:
        statement = "The {} of {} was {}: ".format(stat, city, report_to_print[stat])
        print statement


main()
