import argparse
import os

from pprint import pprint


def main():
    args = setup_argparse()
    directory_to_print = ensure_args(args)
    outerdict = build_outerdict(directory_to_print)
    sort_outerdict(outerdict, args)


def setup_argparse():
    parser = argparse.ArgumentParser(description='Show the files in a directory')
    parser.add_argument('-dir', type=str,
                        help='the directory you want to see files for')
    parser.add_argument('-by', type=str,
                        help='the criteria by which to sort/return data')
    parser.add_argument('-results', type=int,
                        help='the number of results to return')
    parser.add_argument('-order', type=str,
                        help='ascending/desending order results')
    args = parser.parse_args()
    return args


def ensure_args(args):
    directory_to_print = args.dir
    print "directory_to_print from ensure_args", directory_to_print
    if not os.path.exists(os.path.dirname(directory_to_print)):
        print "Path of directory to print is not recognized, please use another one"
    else:
        return directory_to_print


def build_outerdict(directory_to_print):
    outerdict = {}
    for item in os.listdir(directory_to_print):
        item_path = os.path.join(directory_to_print, item)
        item_base_name = os.path.basename(item)
        item_size = os.path.getsize(item_path)
        item_time = os.path.getmtime(item_path)

        try:
            outerdict[item_path] += {'name': item_base_name,
                                     'size': item_size,
                                     'mtime': item_time}
        except KeyError:
            outerdict[item_path] = {'name': item_base_name,
                                    'size': item_size,
                                    'mtime': item_time}

    return outerdict


def _getlen(arg):
    return len(arg)


def sort_outerdict(outerdict, args):
    by = args.by
    order = args.order
    results = args.results
    # print by, results, order
    # name, size, and key should be able to be used to sort by
    for key in outerdict:
        name = outerdict[key]['name']
        print "name", name
        size = outerdict[key]['size']
        print "size", size
        mtime = outerdict[key]['mtime']
        print "mtime", mtime

    def _by_size(key):
        size = outerdict[key]['size']
        return size

    sorted_by_size = sorted(outerdict, key=_by_size)
    print sorted_by_size

    # matched the sorted values to the outter dict
    for sorted_val in sorted_by_size:
        print outerdict[sorted_val]



    # sorted_dict = sorted(outerdict, key=_getlen)
    # pprint(sorted_dict)

# first look at the "by" and get the data for that parameter
# then sort that data by asending order or descending order (large to small)
# then return only the first x amount of results



main()
