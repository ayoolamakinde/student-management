"""
This is the student module and supports all the ReST actions for the
STUDENT collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
STUDENT = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp(),
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp(),
    },
}


def read_all():
    """
    This function responds to a request for /api/student
    with the complete lists of student

    :return:        json string of list of student
    """
    # Create the list of student from our data
    return [STUDENT[key] for key in sorted(STUDENT.keys())]


def read_one(lname):
    """
    This function responds to a request for /api/student/{lname}
    with one matching person from student

    :param lname:   last name of person to find
    :return:        person matching last name
    """
    # Does the person exist in student?
    if lname in STUDENT:
        person = STUDENT.get(lname)

    # otherwise, nope, not found
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )

    return person


def create(person):
    """
    This function creates a new person in the student structure
    based on the passed in person data

    :param person:  person to create in student structure
    :return:        201 on success, 406 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    # Does the person exist already?
    if lname not in STUDENT and lname is not None:
        STUDENT[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{lname} successfully created".format(lname=lname), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=lname),
        )


def update(lname, person):
    """
    This function updates an existing person in the student structure

    :param lname:   last name of person to update in the student structure
    :param person:  person to update
    :return:        updated person structure
    """
    # Does the person exist in student?
    if lname in STUDENT:
        STUDENT[lname]["fname"] = person.get("fname")
        STUDENT[lname]["timestamp"] = get_timestamp()

        return STUDENT[lname]

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )


def delete(lname):
    """
    This function deletes a person from the student structure

    :param lname:   last name of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the person to delete exist?
    if lname in STUDENT:
        del STUDENT[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname), 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )
