# time_utils

Basic python package to time processes similar to a stopwatch.  This package also includes various pre-formated timestamps for sql, s3 key prefixes, and s3 glues prefixes.

### basic usage
```python
>>> from time_utils.time_utils import stopWatch
>>> sw = stopWatch()
>>> sw.lap()
Lap 1:
15 second(s)
datetime.timedelta(seconds=15, microseconds=693657)
>>> sw.lap()
Lap 2:
4 second(s)
datetime.timedelta(seconds=4, microseconds=751870)
```
