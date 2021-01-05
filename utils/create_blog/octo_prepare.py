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
        self.parser.add_argument(
            "-c", "--config", metavar="", help="provide a .json file", required=True)


class Octopress:
    def __init__(self):
        self._src_dir = ""
        self._dst_dir = ""
        self._publish_flag = ""
        self._platform = ""
        self._blacklisted_dirs = list()
        self._whitelisted_filetypes = list()
        self._skipped_files = list()

    def get_parameters(self, config_dict):
        """
        retrieve all values from json
        :param config_dict: dict
        :return: None
        """

        self._src_dir = config_dict["src_dir"]
        self._dst_dir = config_dict["dst_dir"]
        self._publish_flag = config_dict["publish_flag"]
        self._blacklisted_dirs = config_dict["blacklisted_dirs"]
        self._whitelisted_filetypes = config_dict["whitelisted_filetypes"]
        self._skipped_files = config_dict["skipped_files"]

        self._platform = config_dict["platform"]

        # validate the input
        if not self._src_dir and self._dst_dir and self._publish_flag and self._platform and self._skipped_files:
            print("[x] please fill the input in the json config file !!")
            sys.exit(0)

    @staticmethod
    def _parse_metadata(absolute_file_path):
        """
        parse markdown metadata
        :return:
        """
        date = comments = ""
        counter = 0
        with open(absolute_file_path) as file:
            for line in file:
                # if first line is not started with '-' then the file is not valid
                if counter == 0 and line[:-1] != '---':
                    return date, comments
                # date
                if counter == 3:
                    date = line.split(" ")[1]
                # comments
                elif counter == 4:
                    comments = line.split(" ")[1]
                elif counter > 4:
                    break
                counter = counter + 1
        return date, comments[:-1]

    @staticmethod
    def _remove_unused_image(asset_dir, markdown_file, skipped_file):
        """
        remove unused images from local asset dir
        """
        flag = True
        files_used_in_markdown = []
        # processing the markdown file
        with open(markdown_file) as f:
            for line in f:
                # checking .png file
                if line.startswith("![") and line.find(".png)"):
                    image = line.split('/').pop()[:-2]
                    files_used_in_markdown.append(image)

                # check pattern for the video preview image
                if line.startswith("[![") and line.find(".png)"):
                    tmp = line.split(')](')
                    image = tmp[0].split('/').pop()
                    files_used_in_markdown.append(image)

        for root, dirs, files in os.walk(asset_dir):
            for file_name in files:
                # skipping .py and .txt files
                name, extension = os.path.splitext(file_name)
                if extension in skipped_file:
                    continue

                if file_name not in files_used_in_markdown:
                    flag = False
                    path = asset_dir + '/' + file_name
                    os.remove(path)
                    print(f"[x] removed {file_name}")

        if flag is True:
            print(f"[+] no files are removed from the .assets directory ")

    def process_markdown(self):
        """
        process the markdown files
        :return:
        """
        for root, dirs, files in os.walk(self._src_dir):
            for file in files:
                # resolve the / issue at src directory
                if root != self._src_dir:
                    absolute_file_path = root + "/" + file
                else:
                    absolute_file_path = root + file

                # extract the file type
                name, file_type = os.path.splitext(file)

                # extract the directory
                curr_dir = root.split('/').pop()

                if curr_dir in self._blacklisted_dirs:
                    continue

                # check if the file types are whitelisted
                if file_type in self._whitelisted_filetypes:
                    # parse metadata from a markdown file
                    date, comments = self._parse_metadata(absolute_file_path)

                    if comments == "false":
                        print(f"[x] {file} => comment : false")
                        continue

                    if date != "" and comments == "true":
                        print(f"[x] {file} => comment : true")
                        # remove unused images
                        asset_dir = root + "/" + name + ".assets/"
                        self._remove_unused_image(
                            asset_dir, absolute_file_path, self._skipped_files)

                        # prepare the file name
                        new_file_name = date + "-" + name.replace('_', '-') + ".markdown"

                        # remove the old file
                        cmd = "cd " + self._dst_dir + " " + "&& rm -f " + new_file_name
                        subprocess.check_output(cmd, shell=True)

                        # clean the artifacts dir for that specific file
                        cmd = "cd " + self._dst_dir + "../artifacts/ && " + "rm -rf " + name + \
                              ".assets"
                        subprocess.check_output(cmd, shell=True)

                        # copy the file to the dst dir
                        cmd = "cp " + absolute_file_path + " " + self._dst_dir + new_file_name
                        subprocess.check_output(cmd, shell=True)

                        # mac os specific commands
                        if self._platform == 'mac':
                            # add artifacts on the image link
                            cmd = "sed -i'.bkk' " + "-e 's/" + name + ".assets/\/artifacts\/" + \
                                  name + ".assets/'" + " " + \
                                  self._dst_dir + new_file_name
                            subprocess.check_output(cmd, shell=True)
                            # remove the bkk file
                            # add artifacts on the image link
                            cmd = "rm -f " + self._dst_dir + new_file_name + ".bkk"
                            subprocess.check_output(cmd, shell=True)

                            # copy the images for mac
                            cmd = "cp -R " + root + "/" + name + ".assets" + \
                                  " " + self._dst_dir + "../artifacts/"
                            subprocess.check_output(cmd, shell=True)

                        else:
                            # reset the image path under artifacts dir
                            # linux specific commands
                            cmd = "sed -i " + "'s/" + name + ".assets/\/artifacts\/" + name + \
                                  ".assets/'" + " " + \
                                  self._dst_dir + new_file_name
                            subprocess.check_output(cmd, shell=True)
                            # copy the images for linux
                            cmd = "cp -r " + root + "/" + name + ".assets/" + \
                                  " " + self._dst_dir + "../artifacts/"
                            subprocess.check_output(cmd, shell=True)


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
        octo.process_markdown()

    else:
        my_input.parser.print_help(sys.stderr)
