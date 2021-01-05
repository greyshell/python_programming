#!/usr/bin/env python3

# author: asinha
# description: update the csv file with branch name

import sys
import argparse
import pandas as pd


class UserInput:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="csv update")
        self.parser.add_argument("-m", "--master_csv", metavar="", help="previous csv",
                                 required=True)
        self.parser.add_argument("-t", "--month_csv", metavar="", help="latest csv", required=True)
        self.parser.add_argument("-o", "--output_csv", metavar="", help="output csv", required=True)


def auto_triage(master_csv, month_csv, output_csv):
    # load the csv
    month = pd.read_csv(month_csv, dtype=str)
    master = pd.read_csv(master_csv, dtype=str)

    lookup = {}

    for row in master.iterrows():
        # pick up the first column
        client_code = row[1][0]
        branch = row[1][2]
        lookup[client_code] = branch

    for i, row in month.iterrows():
        # pick up the first column
        new_client_code = str(row[0])
        if new_client_code == "" or new_client_code is None:
            continue
        # get the branch from lookup
        new_branch = lookup.get(new_client_code, False)
        if new_branch:
            month.loc[i, 'Branch'] = new_branch

    month.to_csv(output_csv, index=False)


if __name__ == "__main__":
    my_input = UserInput()
    args = my_input.parser.parse_args()

    if len(sys.argv) == 1:
        my_input.parser.print_help(sys.stderr)
        sys.exit(0)

    if args.master_csv and args.month_csv and args.output_csv:
        auto_triage(args.master_csv, args.month_csv, args.output_csv)
    else:
        my_input.parser.print_help(sys.stderr)
