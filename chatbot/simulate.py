#!/usr/bin/env python3

# This script is meant to test commands without having to connect to matrix.

import sys

from commandcenter.commander import Commander
from commandcenter.eventpackage import EventPackage

import botconfig
import atexit

print("Loading commander...")
g_commander = Commander()

def test_message(message, room_id):
    global g_commander

    sender = '@testcommand-py:cclub.cs.wmich.edu'
    body = message.split(" ")

    event_package = EventPackage(body=body, room_id=room_id, sender=sender, event={})

    command_string = body[0]

    if body[0][0] == botconfig.command_prefix:
        print("Bot output: " + g_commander.run_command(command_string, event_package))

def cleanup():
    print("Shutting down.")

if __name__ == '__main__':
    atexit.register(cleanup)

    room_id = ""
    if len(sys.argv) >= 2:
        room_id = sys.argv[1]
    else:
        room_id = "#bottest:cclub.cs.wmich.edu"

    print("Simulating room: {}".format(room_id))

    print("Enter chat commands via stdin:")

    try:
        last = ''
        while True:
            message = input()

            if message != '':
                test_message(message, room_id)
                last = message
            else:
                if last != '':
                    test_message(last, room_id)
    except (EOFError, KeyboardInterrupt):
        sys.exit()

