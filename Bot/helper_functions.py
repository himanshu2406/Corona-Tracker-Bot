'''
A set of helper functions to be used in the bot.py functions.
'''


def check_na(stat):
    ''' Returns NA if any statistic passed for a country is not available
        Or else it returns the string of that number.
    '''
    return str(stat) if stat is not None else "NA"


def cleaned_diff(new_val, old_val):
    ''' Returns a string with (+/- change) in a statistic.
        Returns empty string if some value is not found or if there is no change
    '''
    if new_val and old_val and new_val - old_val:
        return " ({:+d})".format(new_val-old_val)
    return ""
