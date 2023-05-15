import validators
import re 

blank_line = re.compile(r'^\s*\n?$')
domain_regex = re.compile('[a-zA-Z0-9\-\.]+')

def has_domain_name_string(line):
    return re.match(domain_regex, line)

def has_url_string(line):
    return validators.url(line)

def is_url(line):
    if re.match(blank_line, line):
        return False
    
    if (line[0] == '#'):
        return False
    
    return has_url_string(line) or has_domain_name_string(line)


with open('sites.txt', 'r') as f:
    stripped_lines = [ line.strip(' \t\n') for line in f.readlines() ]

    sites = [ line for line in stripped_lines if is_url(line) ]

    for site in sites:
        print(site)