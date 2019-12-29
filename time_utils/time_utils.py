from datetime import datetime


class stopWatch(object):
    """
    Helper class to time python processes

    Basic usage:

    >>> sw = stopWatch()
    >>> sw.lap()
    Lap 1:
    15 second(s)
    datetime.timedelta(seconds=15, microseconds=693657)
    >>> sw.lap()
    Lap 2:
    4 second(s)
    datetime.timedelta(seconds=4, microseconds=751870)
    """

    def __init__(self):
        self.start = datetime.now()
        self.end = None
        self.lap_num = 0

    def lap(self, sysout=True):
        """
        sysout <boolean> defaults to True
                prints elapsed time
        returns timedelta instance
        """
        self.end = datetime.now()
        delta = self.end - self.start
        self.start = self.end
        self.lap_num += 1

        ts = int(delta.total_seconds())
        hours, remainder = divmod(ts, 3600)
        minutes, seconds = divmod(remainder, 60)

        if sysout is True:
            print(f"Lap {self.lap_num}:")

            if hours > 0:
                print(f"{hours} hour(s), {minutes} minute(s), {seconds} second(s)")
            elif minutes > 0:
                print(f"{minutes} minute(s), {seconds} second(s)")
            else:
                print(f"{seconds} second(s)")

        return delta


def ts_dict(timestamp=None):
    """
    timestamp <datetime obj> defaults to utc now

    returns a timestamp dict with keys:
        * year YYYY
        * month MM
        * day DD
        * hour HH
        * min MM
        * sec SS
    """

    if not timestamp:
        timestamp = datetime.utcnow()

    timestamp_dict = {
        "year": timestamp.strftime("%Y"),
        "month": timestamp.strftime("%m"),
        "day": timestamp.strftime("%d"),
        "hour": timestamp.strftime("%H"),
        "min": timestamp.strftime("%M"),
        "sec": timestamp.strftime("%S"),
    }

    return timestamp_dict


def sql_ts(timestamp=None, sysout=False):
    """
    timestamp <datetime obj>
              use 'now' to return the current timestamp

    returns sql like timestamp

    YYYY-MM-DD HH:MM:SS
    """
    if not timestamp == "now":
        timestamp = datetime.utcnow()

    ts = timestamp.strftime("%Y-%m-%d %H:%M:%S")

    if sysout:
        print(ts)

    return ts


def s3_ts(timestamp=None):
    """
    timestamp <datetime obj> defaults to utc now


    returns s3 ts format /YYYY/MM/DD/
    """

    if not timestamp:
        timestamp = datetime.utcnow()

    return timestamp.strftime("/%Y/%m/%d/")


def s3_glue_ts(timestamp=None):
    """
    timestamp <datetime obj>
              use 'now' to return the current timestamp

    returns s3 AWS glue friendly key parition
    """
    if not timestamp:
        timestamp = datetime.utcnow()

    return timestamp.strftime("/year=%Y/month=%m/day=%d/")
