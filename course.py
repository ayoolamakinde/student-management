"""
This is the course module and supports all the ReST actions for the
course collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
course = {
    "Cloud": {
        "coursename": "Cloud",
        "lecturername": "Ayoola",
        "timestamp": get_timestamp(),
    },
    "Python": {
        "coursename": "Python",
        "lecturername": "Oluwasanmi",
        "timestamp": get_timestamp(),
    },
    "Data": {
        "coursename": "Data",
        "lecturername": "Tolu",
        "timestamp": get_timestamp(),
    },
}


def read_all():
    """
    This function responds to a request for /api/course
    with the complete lists of course
    :return:        json string of list of course
    """
    # Create the list of course from our data
    return [course[key] for key in sorted(course.keys())]


def read_one(lecturername):
    """
    This function responds to a request for /api/course/{lecturername}
    with one matching person from course
    :param lecturername:   last name of person to find
    :return:        person matching last name
    """
    # Does the person exist in course?
    if lecturername in course:
        person = course.get(lecturername)

    # otherwise, nope, not found
    else:
        abort(
            404, "Person with last name {lecturername} not found".format(lecturername=lecturername)
        )

    return person


def create(person):
    """
    This function creates a new person in the course structure
    based on the passed in person data
    :param person:  person to create in course structure
    :return:        201 on success, 406 on person exists
    """
    lecturername = person.get("lecturername", None)
    coursename = person.get("coursename", None)

    # Does the person exist already?
    if lecturername not in course and lecturername is not None:
        course[lecturername] = {
            "lecturername": lecturername,
            "coursename": coursename,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{lecturername} successfully created".format(lecturername=lecturername), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Person with last name {lecturername} already exists".format(lecturername=lecturername),
        )


def update(lecturername, person):
    """
    This function updates an existing person in the course structure
    :param lecturername:   last name of person to update in the course structure
    :param person:  person to update
    :return:        updated person structure
    """
    # Does the person exist in course?
    if lecturername in course:
        course[lecturername]["coursename"] = person.get("coursename")
        course[lecturername]["timestamp"] = get_timestamp()

        return course[lecturername]

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Person with last name {lecturername} not found".format(lecturername=lecturername)
        )


def delete(lecturername):
    """
    This function deletes a person from the course structure
    :param lecturername:   last name of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the person to delete exist?
    if lecturername in course:
        del course[lecturername]
        return make_response(
            "{lecturername} successfully deleted".format(lecturername=lecturername), 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Person with last name {lecturername} not found".format(lecturername=lecturername)
        )
