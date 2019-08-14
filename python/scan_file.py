#!/usr/bin/env python3
# encoding: utf-8
#
#Question 1: Return a list of people who are happy dancer
#
#Question 2: Modify your solution so question 1 still work, return a list of people who are happy SRE
#
#Question 3: Modify your solution so question 1 and 2 still work, return a list of people who are happy dancer from California
#
#Question 4: Modify your solution so question 1, 2 and 3 still work, swap the state and attributes column in the data file

from argparse import ArgumentParser
import os
from pprint import pprint as pp
import sys

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


def parse_file(file_name, search_query, state=None):
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


def main_args():
    parser = ArgumentParser()
    
    parser.add_argument(
        'file_name',
        help='Name of the file to parse.', action="store")

    parser.add_argument(
        '-q', '--query', default="all",
        help='Specify the query to run. The pre-defined query strings are: happy_sre, happy_dancer. '
             'You can provide your own by quoting the strings, for example: "sre female"', action="store")

    parser.add_argument(
        '-s', '--state', 
        help='Specify the query to run. The available query strings are: happy_sre, happy_dancer', action="store")

    parser.add_argument(
        '-w', '--swap', 
        help='For when you want to swap the attributes and state in the data file.', action="store_true")

    return parser.parse_args()


def main(args):
    if len(sys.argv) == 1:
        sys.exit("ERROR: You must provide a file name to run.  Please run {} -h for more details".format(script_name))

    if os.path.isfile(args.file_name):
        parse_file(args.file_name,args.query,args.state)
    else:
        sys.exit("ERROR: Can't find file, {}. Please check for its existence and run me again.")


if __name__ == "__main__":
    args = main_args()
    main(args)
