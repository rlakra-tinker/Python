#
# Author: Rohtash Lakra
#
from datetime import datetime
from pytz import timezone
import pytz


class TimeUtils:
    __DATE_FORMAT = '%Y-%m-%d %H:%M:%S %Z'
    __PST_TIMEZONE = 'US/Pacific'

    def utc_to_pst(self, utc_time):
        """Converts a UTC datetime to PST datetime."""
        pst_timezone = pytz.timezone(self.__PST_TIMEZONE)
        pst_time = utc_time.astimezone(pst_timezone)
        return pst_time

    def now_utc(self):
        """Returns the current datetime in UTC timezone"""
        return datetime.now(pytz.utc)

    def iso_datetime(self, date_time_str: str):
        return datetime.fromisoformat(date_time_str)

    def utc_datetime(self, date_time_str: str):
        """Converts a UTC datetime to PST datetime."""
        utc_timezone = timezone('UTC')
        utc_datetime = datetime.fromisoformat(date_time_str).astimezone(utc_timezone)
        return utc_datetime

    def to_str(self, date: datetime, date_format: str) -> str:
        return date.strftime(date_format)


print()
time_utils = TimeUtils()
# Print the result
utc_now = time_utils.now_utc()
pst_now = time_utils.utc_to_pst(utc_now)
print("UTC time:", utc_now)
print("PST time:", pst_now)
print()

# 2024-10-02 20:28:32
print('iso_date:', time_utils.iso_datetime('2024-10-02 20:28:32'))
print('utc_datetime:', time_utils.utc_datetime('2024-10-02 12:21:00'))
print()

date_format = '%Y-%m-%d %H:%M:%S %Z'
date = datetime.now(tz=pytz.utc)
# print('Current date & time is:', date.strftime(date_format))
print('Current date & time is:', time_utils.to_str(date, date_format))
date = date.astimezone(timezone('US/Pacific'))
# print('Local date & time is:', date.strftime(date_format))
print('Local date & time is:', time_utils.to_str(date, date_format))
print()
