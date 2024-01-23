# 拼接任意列表
# 实现类似于R语言中的paste函数功能


# %% paste() function for Python
# join lists pairwise, using recycling rules
# default behavior is equivalent to R's paste() function
def paste(*args: list, sep="", recycle=True):
    """
    join lists together pairwise
    allowing for unequal length, using recycling rules
    if recycle is True:
        it's equivalent to R's paste() function
        recyle shorter lists elements
    if recycle is False: paste together without recycling
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


# %% test
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c"]
c = ["x"]
d = []

print(paste(a, b, sep="-", recycle=False))
print(paste(a, b, sep="-"))
print(paste(a, b, c, sep="-", recycle=False))
print(paste(a, b, c, sep="-", recycle=True))
print(paste(a, c, sep="-"))
print(paste(a, sep="-"))
print(paste(sep="-"))
# with empty list
print(paste(a, b, d, sep="-", recycle=False))
print(paste(a, b, d, sep="-", recycle=True))


# %%
