## Description

`octo_prepare.py` is used to generate posts for `Greyshell's Diary`.

### How to use

1. write down notes in `markdown` format.
2. when you paste a image, it gets stored inside the filename.assets folder.
3. If that note needs to be published then set `comments: true` and set a categories like `categories: windows-exploit-dev`.
    - Available categories: windows-exploit-dev, linux-exploit-dev, web-security, network-security, capture-the-flag
4. use markdown preview for `view only` mode.
5. how to include / show the content of a .txt file: create a `.py` file and copy the content inside the multiline comment section.
6. how to use python code: copy the python file into the `octopress/source/artifacts/<filename>.assets` folder directly.
    - refer the code with `../` at the begining of the assets directory. For example,
    `{% include_code ../canary_bypass02.assets/vuln.c %}`
7. run the `octo_prepare.py` script,
    - it checks the source directory and recursively find the all markdown files.
    - it parse the metadata of a markdown file, based on the that it decides that needs to be published or not.
    - it removes the unused images from the artifacts directory.
    - it copies the markdown file into `octopress/source/_posts` directory and associate artifacts into `octopress/source/artifacts` directory.
    - change the image path in the markdown file.
8. after publish the blog, lock the markdown file with `comments: false`.
9. for video walkthough, copy the preview image into the assset folder and manually fix the asset
 directory path in the markdown file.

### Usage
```
usage: octo_prepare.py [-h] -c

create blog posts for octopress

optional arguments:
  -h, --help      show this help message and exit
  -c , --config   provide a .json file
```




