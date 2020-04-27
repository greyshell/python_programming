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

    def _parse_metadata(self):
        pass

    def process_markdown(self):
        for root, curr_dir, files in os.walk(self._src_dir):
            # print(f"root: {root}, curr_dir: {curr_dir}, files: {files}")
            for file in files:
                absolute_file_path = root + file
                for filetype in self._whitelisted_filetypes:
                    if filetype in absolute_file_path:
                        print(absolute_file_path)


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
