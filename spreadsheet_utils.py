def clean(col):
    ''' Remove title and strip newlines from column '''
    col = col[1:]
    col = [x.rstrip('\n') for x in col if x is not None]
    return col

def filter_attending_and_compress(emails, first_names, last_names, attending, availability):
    ''' Filter out the columns where user is not attending and compress into single list '''
    
    emails = [x for x,y in zip(emails, attending) if y != "No"]
    first_names = [x for x,y in zip(first_names, attending) if y != "No"]
    last_names = [x for x,y in zip(last_names, attending) if y != "No"]
    availability = [x for x,y in zip(availability, attending) if y != "No"]

    return zip(emails, first_names, last_names, availability)

def _get_set_availability(availability):
    ''' Get set from string '''
    return set(availability.split(', '))
