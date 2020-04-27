#!/usr/bin/env python3

# author: greyshell
# description: create blog posts for octopress


import argparse
import json
import os
import subprocess
import sys


class UserInput:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
                description="create blog posts for octopress")
        self.parser.add_argument("-c", "--config", metavar="", help="provide a .json file", required=True)


class Octopress:
    def __init__(self):
        self._src_dir = ""
        self._dest_dir = ""
        self._publish_flag = ""
        self._blacklisted_dirs = list()
        self._whitelisted_filetypes = list()

    def get_parameters(self, config_dict):
        """
        retrieve the value from the input
        :param config_dict: dict
        :return: None
        """

        self._src_dir = config_dict["src_dir"]
        self._dest_dir = config_dict["dest_dir"]
        self._publish_flag = config_dict["publish_flag"]
        self._blacklisted_dirs = config_dict["blacklisted_dirs"]
        self._whitelisted_filetypes = config_dict["whitelisted_filetypes"]

        # validate the input
        if not self._src_dir and self._dest_dir and self._publish_flag:
            print(f"[x] please fill the input in the json config file !!")
            sys.exit(0)

    def clean_dest_dir(self):
        # clean the existing dest dir
        command = "cd " + self._dest_dir + " && " + "rm -rf *"
        print(command)
        subprocess.check_output(command, shell=True)

    @staticmethod
    def _parse_metadata(absolute_file_path):
        """
        parse metadata from a markdown file
        :return:
        """
        date = comments = ""
        counter = 0
        with open(absolute_file_path) as file:
            for line in file:
                if line[0] == b'-':
                    return date, comments
                else:
                    # date
                    if counter == 3:
                        date = line.split(" ")[1]
                    # comments
                    elif counter == 4:
                        comments = line.split(" ")[1]
                    elif counter > 4:
                        break
                counter = counter + 1
        return date, comments

    def process_markdown(self):
        """
        process the markdown files
        :return:
        """
        for root, dirs, files in os.walk(self._src_dir):
            for file in files:
                # print(root, curr_dir, files)
                for filetype in self._whitelisted_filetypes:
                    absolute_file_path = root + "/" + file
                    if filetype in absolute_file_path:
                        print(absolute_file_path)
                        # parse metadata from a markdown file
                        date, comments = self._parse_metadata(absolute_file_path)
                        if date != "" and comments != "":
                            print(date, comments)

                        exit(0)


if __name__ == "__main__":
    my_input = UserInput()
    args = my_input.parser.parse_args()

    if len(sys.argv) == 1:
        my_input.parser.print_help(sys.stderr)
        sys.exit(0)

    if args.config:
        with open(args.config) as f:
            json_config = json.load(f)

        octo = Octopress()
        octo.get_parameters(json_config)
        # octo.clean_dest_dir()
        octo.process_markdown()

    else:
        my_input.parser.print_help(sys.stderr)
