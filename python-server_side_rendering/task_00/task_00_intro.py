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
    
    # iterate through each dictionary in the attendees list
    for attendee in attendees:
        i += 1
        for key, value in attendee.items():
            if value is not None:
                # using the ** operator to unpack dictionary
                processed_template = template.format(**attendee)
            else:
                # if any value in the dctionary is None - replace with N/A
                attendee[key] = "N/A"

        output_file = "output_{}.txt".format(i)
        # Write to output file
        try: 
            with open(output_file, 'w') as f:
                    f.write(processed_template)
        except IOError:
            logging.error("Failed to write to file")
