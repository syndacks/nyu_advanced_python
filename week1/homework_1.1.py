import sys


def main():
    print sys.argv
    if len(sys.argv) == 2:
        if sys.argv[1] == 'New York':
            city = 'new_york'
        elif sys.argv[1] == 'Los Angeles':
            city = 'los_angeles'
        elif sys.argv[1] == 'Honolulu':
            city = 'honolulu'
        elif sys.argv[1] == 'Chicago':
            city = 'chicago'
        else:
            print "I'm sorry but I don't recognize the city you entered."

        print "city chosen: ", city
        calculate_means(city)


def calculate_means(city):
    # city weather data file locations
    if city == 'new_york':
        weather_data = './weather_newyork.csv',
    elif city == 'chicago':
        weather_data = './weather_chicago.csv',
    elif city == 'honolulu':
        weather_data = './weather_honolulu.csv',
    elif city == 'los_angeles':
        weather_data = './weather_losangeles.csv',

    fh = open(weather_data)
    # skip the first line (csv header)
    lines = fh.readlines()[1:]

    sum_of_means = 0
    count_of_means = 0
    for line in lines:
        # items is a list
        items = line.split(',')
        print items
        # the mean is the third item a string
        mean = items[2]
        sum_of_means += int(mean)
        count_of_means += 1

    print "sum_of_means: ", sum_of_means
    print "count_of_means: ", count_of_means
    print "avg means: ", sum_of_means / count_of_means


main()
