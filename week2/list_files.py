import argparse
import os
import time

from pprint import pprint


def main():
    args = setup_argparse()
    directory_to_print = ensure_args(args)
    outerdict = build_outerdict(directory_to_print)
    sort_outerdict(outerdict)


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
    if not os.path.exists(os.path.dirname(directory_to_print)):
        print "Path of directory to print is not recognized, please use another one"
    else:
        print "directory_to_print: ", directory_to_print
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

def _get_args_data_for_sorting():
    args = setup_argparse()
    args.results


def _getlen(arg):
    # get the argparse args data from user

    print "args from _getlen", args.results;
    return len(arg)


def sort_outerdict(outerdict):
    sorted_dict = sorted(outerdict, key=_getlen)
    pprint(sorted_dict)



main()
