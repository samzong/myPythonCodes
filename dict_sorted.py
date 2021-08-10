# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""


def dict_sorted(dict=None):
    key_val = {}
    if dict is None:
        return "dict is None"
    else:
        for i in sorted(dict):
            key_val[i] = dict[i]

    return key_val
