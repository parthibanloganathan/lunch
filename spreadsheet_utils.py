def clean(col):
    ''' Remove title and strip newlines from column '''
    col = col[1:]
    print col
    col = [x.rstrip('\n') for x in col if x is not None]
    return col

def filter_attending(emails, first_names, last_names, attending):
    ''' Filter out the columns where user is not attending '''
    
    emails = [x for x,y in zip(emails, attending) if y != "No"]
    first_names = [x for x,y in zip(first_names, attending) if y != "No"]
    last_names = [x for x,y in zip(last_names, attending) if y != "No"]
    availability = [x for x,y in zip(availability, attending) if y != "No"]

    return emails, first_names, last_names, availability

def get_availability_set(availability):
    ''' Create set of days on which user is available '''
    availability = availability.split(', ')
    availability = set(availability)
    return availability
