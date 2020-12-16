"""Main module."""
from typing import Union, List, Tuple

list_or_tuple = Union[List,Tuple]


def ltwh_to_ltrb(ltwh: list_or_tuple) -> list_or_tuple:
    return type(ltbw)((ltwh[0], ltwh[1], ltwh[0]+ltwh[2], ltwh[1] + ltwh[3]))


def ltrb_to_ltwh(ltrb: list_or_tuple) -> list_or_tuple:
    return type(ltrb)((ltrb[0], ltrb[1], ltrb[2]-ltrb[0], ltrb[3] - ltrb[0]))
