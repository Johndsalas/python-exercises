def keep_long_words(words):

    '''
    >>> keep_long_words(['ls', 'codeup', 'code', 'pip', 'bayes'])
    ['codeup', 'bayes']
    >>> keep_long_words(['cd', 'ls', 'pwd'])
    []
    >>> keep_long_words(['python', 'algorithm'])
    ['python', 'algorithm']
    '''

    lst = []

    for word in words:

        if len(word) > 4:
        
            lst.append(word)

    return lst

keep_long_words(['ls', 'codeup', 'code', 'pip', 'bayes'])

    
def make_model(cars):
    
    lst = []

    '''
    >>> cars = []
    >>> cars.append({'make': 'Toyota', 'model': 'Camry'})
    >>> cars.append({'make': 'Honda', 'model': 'Accord'})
    >>> cars.append({'make': 'Ford', 'model': 'Fiesta'})
    >>> cars.append({'make': 'Ford', 'model': 'F-150'})
    >>> make_model(cars)
    '''

    for dict in cars:

        car = dict['make'] + ' ' + dict['modle']

        lst.appent(car)

    return lst

def extract_time_components(string):

    '''
    >>> extract_time_components('21:30:00')
    {'hours': 21, 'minutes': 30, 'seconds': 0}
    >>> extract_time_components('09:01:53')
    {'hours': 9, 'minutes': 1, 'seconds': 53}
    '''

    return {'hours': int(string[0:2]), 'minutes': int(string[3:5]), 'seconds': int(string[-2:])}

extract_time_components('21:30:00')