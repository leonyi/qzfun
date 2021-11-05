#!/usr/bin/env python3
# encoding: utf-8

from argparse import ArgumentParser
import os
import shutil
import sys
import tempfile 

script_name = os.path.basename(sys.argv[0])


def fetch_query(user_db, search_string, state=None):
    '''Retrieves user information from provided user db.
       :param user_db: Dictionary containing the contents of the user provided data file.
       :param search_string: query string to user to search user attributes from user_db.
       :param state: string
       :return: list of users found in user_db data.
    '''
    happy_names = []

    for entry in user_db:
        # Removes spaces in strings within the attributes list.
        entry['attributes'] = [e.strip(' ') for e in entry['attributes']]
        if all(a in entry['attributes'] for a in search_string.split()):
            happy_names.append(entry['name'])

    return happy_names


def parse_file(file_name, search_query, state=None, swap=False):
    ''' Populates the user db dictionary with contents from the user provided data file.
    :param file_name: User provided colon delimited data file.
    :param search_query: The string user to retrieve user attributes from file.
    :param state: The string holding the state name as a value.
    :return: None
    '''
    people = []

    with open(file_name,'r') as fh:
        for line in fh:
            (name, state, attributes) = line.split(':')
            people.append({'name': name,
                           'state': state,
                          'attributes': attributes.rstrip().split(',')})

    if state in {"california", "CA", "ca"}:
       state = "california"
    else:
        # Sets search_string to the user defined search query.
        search_string = search_query

    print("Searching: {}".format(search_query))
    print(f'Result: {fetch_query(people, search_query, state)}')
    if swap is True:
      print("Swapping attributes and states columns in {}".format(file_name))
      swap_file_entries(file_name)


def swap_file_entries(file_name):
    ''' Backs up and edits provided file by swapping attributes colunm with state.
    :param file_name: File to edit.
    :return: None
    '''
    shutil.copy(file_name, "{}.bkup".format(file_name))

    temp_file = tempfile.NamedTemporaryFile(mode="r+")
    with open(file_name, 'r') as fh:
        for line in fh:
            (name, state, attributes) = line.split(':')
            temp_file.write("{}:{}:{}\n".format(name, attributes.rstrip(), state))
    temp_file.seek(0) 
    with open(file_name, "w") as nfh:
        for l in temp_file:
            nfh.write(l)


def main_args():
    parser = ArgumentParser()

    parser.add_argument(
        'file_name',
        help='Name of the file to parse.', action="store")

    parser.add_argument(
        '-q', '--query', default="happy",
        help='Specify the query to run.'
             'Please quote your search strings, for example: "sre female"', action="store")

    parser.add_argument(
        '-s', '--state', 
        help='Adds state to the search query.', action="store")

    parser.add_argument(
        '-w', '--swap', 
        help='For when you want to swap the attributes and state in the data file.', action="store_true")

    return parser.parse_args()


def main(args):
    if len(sys.argv) == 1:
        sys.exit("ERROR: You must provide a file name to run.  Please run {} -h for more details".format(script_name))

    if not os.path.isfile(args.file_name):
        sys.exit("ERROR: Can't find file, {}. Please check for its existence and run me again.".format(args.file_name))

    if os.path.isfile(args.file_name):
        parse_file(args.file_name,args.query,args.state,args.swap)


if __name__ == "__main__":
    args = main_args()
    main(args)
