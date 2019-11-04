from datetime import datetime
import time


class timer(object):
    '''
    Helper class to time processes

    Basic Usage:
    
    >>> from timer_utils.timer import timer
    >>>
    >>> t = timer()
    >>> t.print_lap('s')
    5.469961
    '''
    def __init__(self):
        self.start = datetime.now()
        self.end = None


    def lap(self, units):
        self.end = datetime.now()
        delta = self.end - self.start
        self.start = self.end

        if units == 's':
            return delta.total_seconds()

        elif units == 'm':
            return delta.total_seconds()/60

        elif units == 'h':
            return delta.total_seconds()/3600


    def print_lap(self, units='s'):
        time = round(self.lap(units),2)

        if units == 's':
            print('{0} seconds \n\n'.format(time))

        elif units == 'm':
            print('{0} minutes \n\n'.format(time))

        elif units == 'h':
            print('{0} hours \n\n'.format(time))

            
def ts_dict(timestamp):
    '''
    timestamp <datetime obj>
              use 'now' to return the current timestamp  
    
    returns a timestamp dict with keys:
        * year YYYY
        * month MM
        * day DD
        * hour HH
        * min MM
        * sec SS
    '''
    
    if timestamp == 'now':
        timestamp = datetime.now()

    timestamp_dict = {
            'year': timestamp.strftime('%Y'),
            'month': timestamp.strftime('%m'),
            'day': timestamp.strftime('%d'),
            'hour': timestamp.strftime('%H'),
            'min': timestamp.strftime('%M'),
            'sec': timestamp.strftime('%S')   
    }
    
    return timestamp_dict


def sql_ts(timestamp, sysout=False):
    '''
    timestamp <datetime obj>
              use 'now' to return the current timestamp 

    returns sql like timestamp
    
    YYYY-MM-DD HH:MM:SS
    '''
    if timestamp == 'now':
        timestamp = datetime.now()
    
    ts = timestamp.strftime('%Y-%m-%d %H:%M:%S')

    if sysout == True:
        print(ts)

    return ts


def s3_ts(timestamp):
    '''
    timestamp <datetime obj>
              use 'now' to return the current timestamp 

    returns s3 ts format /<year>/<month>/DD_HH:MM:SS
    '''

    if timestamp == 'now':
        timestamp = datetime.now()

    return timestamp.strftime('/%Y/%m/%d_%H:%M:%S')


def s3_glue_ts(timestamp):
    '''
    timestamp <datetime obj>
              use 'now' to return the current timestamp 
              
    returns s3 AWS glue friendly key parition
    '''
    if timestamp == 'now':
        timestamp = datetime.now()
    
    return timestamp.strftime('''/year=%Y/month=%m/day=%d/%Y-%m-%d_%H:%M:%S''')
    

