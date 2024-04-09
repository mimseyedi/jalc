"""
•  ┓
┓┏┓┃┏
┃┗┻┗┗ is a package to work with Jalali date and time.
┛

This file is related to the functions that perform conversions
that are necessary for this project.
Including converting dates, numbers, days of the week, months and...


Github repo: https://github.com/mimseyedi/jalc
"""


from datetime import datetime as dt


def g2j(gy: int, gm: int, gd: int) -> tuple:
    """
    Convert Gregorian date to Jalali.
    https://jdf.scr.ir/jdf/python

    :param gy: Gregorian year
    :param gm: Gregorian month
    :param gd: Gregorian day
    :return: tuple(jy, jm,, jd)
    """

    ...


def j2g(jy: int, jm: int, jd: int) -> tuple:
    """
    Convert Jalali date to Gregorian.
    https://jdf.scr.ir/jdf/python

    :param jy: Jalali year
    :param jm: Jalali month
    :param jd: Jalali day
    :return: tuple(gy, gm, gd)
    """

    ...


def fa_number(digit: str) -> str:
    """
    Convert English number to Farsi number.

    :param digit: A single digit number in Gregorian.
    :return: Farsi number in string format.
    """

    ...


def fa_weekday(day: str) -> str:
    """
    Convert Gregorian weekday to Jalali weekday.

    :param day: The name of a weekday in English.
    :return: Jalali weekday in Farsi.
    """

    ...


def fa_month(month: str) -> str:
    """
    Convert Gregorian month to Jalali month.

    :param month: The name of a month in English.
    :return: Jalali month in Farsi.
    """

    ...


def fi_weekday(day: str) -> str:
    """
    Convert Gregorian weekday to Jalali weekday in fingilish format.

    :param day: The name of a weekday in English.
    :return: Jalali weekday in Fingilish.
    """

    ...


def fi_month(month: str) -> str:
    """
    Convert Gregorian month to Jalali month in fingilish format.

    :param month: The name of a month in English.
    :return: Jalali month in Fingilish.
    """

    ...