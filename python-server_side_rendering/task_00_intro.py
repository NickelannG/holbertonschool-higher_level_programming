#!/usr/bin/python3
""" This module contains the generate_invitations() function """
import logging
import sys


# Define the function
def generate_invitations(template, attendees):
    """
    This function generates personlised invitation files from a
    template with placeholders and a list of objects
    """
    if not isinstance(template, str):
        logging.error("Invalid input type: template must be a string.")
        sys.exit()

    if not isinstance(attendees, list) \
            and not all(isinstance(elem, dict) for elem in attendees):
        logging.error("Invalid input type: attendees must be a list of"
                      "dicionaries")
        sys.exit()

    if template == "":
        logging.error("template must not be an empty string")
        sys.exit()

    if attendees == []:
        logging.error("attendees must not be an empty list")
        sys.exit()

    # Process each attendee
    # if a value is missing, replace with default value "N/A"
    # count index of added attendees starting from 1
    i = 1
    for attendee in attendees:
        processed_template = template.format(
            name=attendee.get('name', 'N/A'),
            event_title=attendee.get('event_title', 'N/A'),
            event_date=attendee.get('event_date', 'N/A'),
            event_location=attendee.get('event_location', 'N/A')
        )
        i += 1

        output_file = "output_{}.txt".format(i)
        # Write to output file
        with open(output_file, 'w') as f:
            f.write(processed_template)
