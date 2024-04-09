"""
•  ┓
┓┏┓┃┏
┃┗┻┗┗ is a package to work with Jalali date and time.
┛

This file is related to Jalali calendar.
There are functions that draw the monthly/yearly calendar in the terminal environment.


Github repo: https://github.com/mimseyedi/jalc
"""


def calendar(month: int=0, lang: str='fi') -> None:
    """
    Display Jalali calendar in standard output.

    :param month: Month number (0 is current month and -1 is year).
    :param lang: Output language (fa: Farsi, fi: Fingilish).
    :return: None
    """

    ...


def print_header(year: int, month: int, lang: str='fi') -> None:
    """
    Print the Jalali calendar header.

    :param year: Current year.
    :param month: Current month.
    :param lang: Output language (fa: Farsi, fi: Fingilish).
    :return: None
    """

    ...


def print_days(*names, lang: str='fi') -> None:
    """
    Print the Jalali days name.

    :param names: Names in 2 char.
    :param lang: Output language (fa: Farsi, fi: Fingilish).
    :return: None
    """

    ...


def print_dates(*dates, lang: str='fi') -> None:
    """
    Print dates in number format.

    :param dates: dates in int.
    :param lang: Output language (fa: Farsi, fi: Fingilish).
    :return: None
    """

    ...


def get_current_year() -> int:
    """
    Received this year.

    :return: current year -> int.
    """

    ...


def is_leap_year(year: int) -> bool:
    """
    Examining the current year in order to determine the leap year.

    :param year: year in Jalali/Shamsi.
    :return: True/False
    """

    ...


def next_days(day: str):
    """
    Days after the current day in a row.

    :param day: Current day.
    :return: Generator
    """

    ...


def set_start_point(weekday: str) -> None:
    """
    Print space to prepare the start or end point.

    :param weekday: Jalali weekday.
    :return: None
    """

    ...
