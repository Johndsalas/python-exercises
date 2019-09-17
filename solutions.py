
def extract_time_components(time):

    '''
    >>> extract_time_components('21:30:00')
    {'hours': 21, 'minutes': 30, 'seconds': 0}
    >>> extract_time_components('09:01:53')
    {'hours': 9, 'minutes': 1, 'seconds': 53}
    '''

    return {'hours': int(time[0:2]), 'minutes': int(time[3:5]), 'seconds': int(time[-2:])}

