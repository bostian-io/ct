import re

records = [
    "Name: Alice Johnson | Email: alice.j@gmail.com | Phone: (555) 123-4567 | Joined: 01/15/2023",
    "Name: Bob Smith | Email: bob_smith@yahoo.com | Phone: 555.987.6543 | Joined: 03-22-2023",
    "Name: Charlie Brown | Email: charlie@outlook.com | Phone: 555 111 2222 | Joined: 2023/07/01",
    "Name: Diana Prince | Email: diana.prince@company.co.uk | Phone: (555)444-3333 | Joined: 11/30/2023",
]

def extract_names(records):
    pattern = r"Name:\s*([^|]+?)\s*\|" # search up to the first pipe character, minding whitespaces
    return [re.search(pattern, record).group(1) for record in records]

def extract_emails(records):
    pattern = r"Email:\s*([\S]+)\s*\|"
    return [re.search(pattern, record).group(1) for record in records]

def normalize_phones(records):
    return ["-".join(re.search(r"\(?(\d{3})\)?[\s.-]*(\d{3})[\s.-]*(\d{4})", record).groups()) for record in records] #we can use .join and a hypen seperator on the string outputs of the 3 regex groups with this list comprehension

def extract_dates(records):
    pattern = r"Joined:\s*([\d/.-]+)"
    return [re.search(pattern, record).group(1) for record in records]

def parse_records(records):
    pattern = (
        r"Name:\s*(?P<name>[^|]+?)\s*\|\s*"
        r"Email:\s*(?P<email>\S+)\s*\|\s*"
        r"Phone:\s*(?P<phone>[^|]+?)\s*\|\s*"
        r"Joined:\s*(?P<joined>\S+)"
    )
    return [re.search(pattern, r).groupdict() for r in records]

# function tests
def summary(records):
    return {
        "names": extract_names(records),
        "emails": extract_emails(records),
        "phones": normalize_phones(records),
        "dates": extract_dates(records),
        "parsed_records": parse_records(records)
    }

from pprint import pprint # import pprint module for more a readable summary of records

pprint(summary(records), sort_dicts=False) # use sort_dicts=False to maintain the order of the keys in the printed output

# printed results:
"""
{'names': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince'],
 'emails': ['alice.j@gmail.com',
            'bob_smith@yahoo.com',
            'charlie@outlook.com',
            'diana.prince@company.co.uk'],
 'phones': ['555-123-4567', '555-987-6543', '555-111-2222', '555-444-3333'],
 'dates': ['01/15/2023', '03-22-2023', '2023/07/01', '11/30/2023'],
 'parsed_records': [{'name': 'Alice Johnson',
                     'email': 'alice.j@gmail.com',
                     'phone': '(555) 123-4567',
                     'joined': '01/15/2023'},
                    {'name': 'Bob Smith',
                     'email': 'bob_smith@yahoo.com',
                     'phone': '555.987.6543',
                     'joined': '03-22-2023'},
                    {'name': 'Charlie Brown',
                     'email': 'charlie@outlook.com',
                     'phone': '555 111 2222',
                     'joined': '2023/07/01'},
                    {'name': 'Diana Prince',
                     'email': 'diana.prince@company.co.uk',
                     'phone': '(555)444-3333',
                     'joined': '11/30/2023'}]}
"""