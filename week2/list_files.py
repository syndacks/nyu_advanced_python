import argparse
import os
import time

from pprint import pprint


def main():
    args = setup_argparse()
    directory_to_print = ensure_args(args)
    outerdict = build_outerdict(directory_to_print)
    final_list = sort_outerdict(outerdict, args)
    print_final_list(final_list)


def setup_argparse():
    parser = argparse.ArgumentParser(description='Show the files in a directory')
    parser.add_argument('-dir', type=str,
                        help='the directory you want to see files for')
    parser.add_argument('-by', type=str,
                        help='the criteria by which to sort/return data')
    parser.add_argument('-results', type=int,
                        help='the number of results to return')
    parser.add_argument('-order', type=str,
                        help='ascending OR descending order results')
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


def sort_outerdict(outerdict, args):
    def _sort(key):
        # sort by args.by possibilities: 'name', 'size', or 'mtime'
        sorted_by = outerdict[key][args.by]
        return sorted_by

    sorted_dict_keys = sorted(outerdict, key=_sort)

    # reverse the list of sorted_dict_keys if 'descending', no change for 'ascending'
    if args.order == 'descending':
        sorted_dict_keys.reverse()

    # matched the sorted values to the outter dict for final results
    final_list = []
    for sorted_val in sorted_dict_keys[:args.results]:
        final_list.append(outerdict[sorted_val])

    return final_list


def _convert_mtime(mtime):
    date_pattern = '%Y-%m-%d %H:%M:%S'
    return time.strftime(date_pattern, time.localtime(mtime))


def print_final_list(final_list):
    for dictionary in final_list:
        print '-{}: {} bytes. Last formatted: {}'.format(dictionary['name'],
        dictionary['size'], _convert_mtime(dictionary['mtime']))
