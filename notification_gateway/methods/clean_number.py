import re

remove_non_numeric = lambda full_number: re.sub(r'\D', '', full_number) # lamdba function that returns  regular expressions numbers as '967770871484' 