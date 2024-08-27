# R's paste() function for Python
# concatenate lists of strings pairwise, using recycling rules
# default behavior is equivalent to R's paste() function
def paste(*args: list, sep="", recycle=True):
    """
    concatenate lists of strings together pairwise, allowing for unequal length
    It accept two additional arguments:
        recycle: wether to recycle the shorter list's elements
            default to True
                equivalent to R's paste() function
                using recycling rules, recyle shorter lists elements
            if False, paste together without recycling
        sep: a string to concatenate list elements, default to empty string "".
    return a string
    """
    # delete empty list first
    args = list(args)
    for arg in args:
        if len(arg) == 0:
            args.remove(arg)

    if len(args) == 0:
        return None

    pasted = args[0]
    if len(args) == 1:
        return pasted
    
    for arg in args[1:]:
        if recycle is True:
            if len(pasted) > len(arg):
                arg = (
                    arg
                    + arg * (len(pasted) // len(arg) - 1)
                    + arg[: (len(pasted) % len(arg))]
                )
                pasted = [f"{a}{sep}{b}" for a, b in zip(pasted, arg)]
            elif len(pasted) <= len(arg):
                pasted = (
                    pasted
                    + pasted * (len(arg) // len(pasted) - 1)
                    + pasted[: (len(arg) % len(pasted))]
                )
                pasted = [f"{a}{sep}{b}" for a, b in zip(pasted, arg)]
        elif recycle is False:
            if len(pasted) > len(arg):
                longer_part = pasted[len(arg) :]
                pasted = [f"{a}{sep}{b}" for a, b in zip(pasted, arg)]
                pasted = pasted + longer_part
            elif len(pasted) <= len(arg):
                longer_part = arg[len(pasted) :]
                pasted = [f"{a}{sep}{b}" for a, b in zip(pasted, arg)]
                pasted = pasted + longer_part
    return pasted
