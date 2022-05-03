import os


def parse_v1(vstr1):
    """ 
    The first version check
    This was in earlier, beta builds of the product, it is now recommended to use the version.NUMBER.

    This is deprecated behaviour, only left up for archivial purposes.
    """
    return int(vstr1)


def parse_v2(vstr1):
    """
    The second iteration

    This one tends to use the version.NUMBER check, but it is more of a pseudo check,
    it just provides you with the version.NUMBER format, and should NEVER be used.

    Unless you have a reason to. Just use `v3`.
    """
    return vstr1


def parse_v3(vstr1):
    """
    The third iteration

    This is the VSign NJMono uses, it works in the same way the NFy VSign does.
    
    """
    return int(vstr1[vstr1.find(".") + 1:])
