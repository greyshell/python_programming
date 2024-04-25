"""
Given current directory and change directory path, return final path.

For Example:

Current                 Change            Output
/                    /facebook           /facebook
/facebook/test       ../abc/def          /facebook/abc/def

Leetcode: https://leetcode.com/problems/simplify-path/description/
"""


def cd_command(cwd: str, arg: str) -> str:
    # cwd -> current working directory
    stack = []
    # set up the stack when first arg start with / and cwd is also not /
    if arg[0] != "/" and cwd != "/":
        # remove leading and trailing /
        temp = cwd.strip("/")
        # arg does not start with / and present home directory is not /
        stack = temp.split("/")

    # if we do "/bar".split("/") -> ['', 'bar']
    # due to this, first we need to strip out /

    # remove leading and trailing /
    temp = arg.strip("/")
    # get directories by splitting by /
    dirs = temp.split("/")

    for d in dirs:
        if d == "..":  # need to backtrack if stack is not empty
            if stack:
                stack.pop()
            else:
                continue
        elif d == ".":  # no need to do anything
            continue
        else:
            stack.append(d)

    # after lots of ../../../ when the stack becomes empty then we need to return only /
    result = "/" + "/".join(stack)  # result always start with /
    return result


if __name__ == "__main__":
    print(cd_command("/Desktop/abc", "..p/../xyz"))
