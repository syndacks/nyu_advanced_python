import argparse
import os
import time

from pprint import pprint

def main():
    args = setup_argparse()
    directory_to_print = ensure_args(args)


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

def next_stuff():
    outerdict = {}
    for item in os.listdir(directory_to_print):
        print "----------------"
        item_path = os.path.join(directory_to_print, item)
        item_base_name = os.path.basename(item)
        item_size = os.path.getsize(item_path)
        item_time = os.path.getmtime(item_path)

        if os.path.isdir(item_path):
            print "{}: {}".format(item, 'directory')
        elif os.path.isfile(item_path):
            print "{}: {}".format(item, 'file')
        print ""

        # for root, dirs, files in os.walk(directory_to_print):
        #     for dir in dirs:
        #         print os.path.join(root, dir)
        #     for file in files:
        #         print os.path.join(root, file)

        if item_path not in outerdict:
            outerdict[item_path] = { 'name': item_base_name,
                                    'size': item_size,
                                    'mtime': item_time }
        # print "item_path:", item_path
        # print "item_base_name:", item_base_name
        # print "{}: modified {}".format(item_path, time.ctime(item_time))
        # print "{} size: {} bytes".format(item_path, item_size)


# pprint(outerdict)
main()
