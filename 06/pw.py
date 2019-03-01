#！ python3
# This is an insecure password locker program
PASSWORDS = {'email':'111111',
             'blog':'ABCD',
             'luggage':'12345'
}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for {} copied to clipboard.".format(account))
else:
    print('There is no account named ' + account)