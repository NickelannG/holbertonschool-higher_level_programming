#!/usr/bin/python3
""" This module contains the generate_invitations() function """
import logging
import sys


# Define the function
def generate_invitations(template, attendees):
    """
    This function generates personlised invitation files from a
    template with placeholders and a list of objects.

    parameters:
    - template (str): string containing placeholders to be replaced
    (template.txt).
    - attendees (list): list of dictionaries where each dict represents an
    attendee/recipient of invitation.
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
        logging.error("Template is empty, no output files generated.")
        sys.exit()

    if attendees == []:
        logging.error("No data provided, no output files generated.")
        sys.exit()

    # Process each attendee
    # count index of added attendees starting from 1
    i = 1

    for attendee in attendees:
        processed_template = template

        # Replace placeholders in the template
        for key, value in attendee.items():
            if value is None:
                value = "N/A"
            processed_template = processed_template.replace("{" + key + "}", str(value))

        output_file = "output_{}.txt".format(i)
        try:
            with open(output_file, 'w') as f:
                f.write(processed_template)
        except IOError:
            logging.error("Failed to write to {}".format(output_file))

        # Increment index counter
        i += 1
