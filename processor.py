import re
import random
import string

# Read in the Syslog Messages
syslog_messages = []
with open("asa_syslog_messages.txt", encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        syslog_messages.append(line.rstrip("\n"))


# Read in the Syslog Variables listed by Cisco
variables = []
with open("variables_used_in_asa_syslog_messages.txt", encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        variables.append(line.rstrip("\n"))

# Sort the variables to process the longer ones first to prevent overlap
sorted_variables = sorted(variables, key=len)
sorted_variables.reverse()
variables = sorted_variables


# Create a unique id for each variable
mapped_variables = {}
for v in variables:
    value = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    mapped_variables[v] = value

from pprint import pprint
pprint(mapped_variables)


'''
for line in syslog_messages:
    result = re.findall(r"(?=(\b" + '|'.join(variables) + r"\b))", line)
    if result:
        print(line, result, "\n")
'''

