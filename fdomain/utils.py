#!/usr/bin/env python
# coding=utf-8

"""
一些通用模块
"""


def _decode(value, code="gbk"):
        try:
            value = value.decode(code, "ignore")
        except:
            pass
        return value

def _encode(value, code="utf-8"):
    if isinstance(value, unicode):
        try:
            value = value.encode(code)
        except UnicodeEncodeError:
            value = value.encode("utf-8", "replace")
    return value
