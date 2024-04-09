"""
•  ┓
┓┏┓┃┏
┃┗┻┗┗ is a package to work with Jalali date and time.
┛

This file is related to the occasions and events of Jalali months.
Comprehensive information from the Jalali calendar related to the
important occasions of Iranian and Persian speakers is stored and accessible here.


Github repo: https://github.com/mimseyedi/jalc
"""


import json
from pathlib import Path


def get_events(month: int, day: int=0) -> dict|str:
    """
    Receive occasions and events of the months and days of the Jalali calendar.

    :param month: Month number (1-12).
    :param day: Day number (day 0 means the current day and -1 means all days of the month).
    :return: Dictionary for all days of the month | string for a day.
    """

    ...


def _read_events(json_file: Path) -> dict:
    """
    Reading events from Jalali Months json file.

    :param json_file: The path of the json file containing the information about the occasion of the months.
    json file of Jalali months events information.
    It already exists in the /events path.
    In case of any problem and file corruption,
    download them again from this link: https://github.com/mimseyedi/jalc/blob/master/src/jalc/events/

    :return: A dictionary containing file information.
    """

    ...