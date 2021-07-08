# Regex Groups and the Pipe Character

import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNumRegex.search('My number is 415-555-4242')

mo = phoneNumRegex.search('My number is 415-555-4242')

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

# Groups are created in regex strings with ()
# first set of par is group 1 and so on
# calling group() or group(0) returns full matching string
# calling group(1) returns group 1's matching string etc
# us \(and \) to match literal parentheses in regex string
# the | pipe can match one of many possible groups
