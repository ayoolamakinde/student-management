from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data t serve with our API
STUDENT = {
    "Alabi": {
        "fname": "Oluwasanmi",
        "lname": "Alabi",
        "timestamp": get_timestamp()
    },
    "Onifade": {
        "fname": "Tolu",
        "lname": "Onifade",
        "timestamp": get_timestamp()
    },
    "Owolabi": {
        "fname": "Tomisin",
        "lname": "Owolabi",
        "timestamp": get_timestamp()
    }
}
# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [STUDENT[key] for key in sorted(STUDENT.keys())]
