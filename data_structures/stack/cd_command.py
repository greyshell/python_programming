def solution(cwd: str, arg: str) -> str:

    stack = []

    if cwd != "/" and arg[0] != "/":
        # remove leading and trailing /
        temp = cwd.strip("/")
        # arg does not start with / and present home directory is not /
        stack = temp.split("/")

    # remove leading and trailing /
    temp = arg.strip("/")
    # get directories by splitting by /
    dirs = temp.split("/")  # a = "/bar", len(a.split("/") -> 2 , due to this we need to strip out

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
