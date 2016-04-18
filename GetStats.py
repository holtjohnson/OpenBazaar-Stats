ob_log = '/Users/g-host/Library/Application Support/OpenBazaar/debug.log.1'
commands = {'GET_USER_METADATA', 'GET_PROFILE', 'GET_IMAGE', 'GET_LISTINGS', 'GET_CONTRACT', 'GET_RATINGS', 'GET_FOLLOWING', 'GET_FOLLOWERS'}
stats_db = {}

import re
re_string = r''
for command in commands:
	if re_string:
		re_string += '|' + command
	else:
		re_string = command
p = re.compile(re_string)


with open(ob_log) as f:
	for line in f:
		match = re.search(p, line)
		if match:
			if match.group(0) in stats_db:
				stats_db[match.group(0)].append(line)
			else:
				stats_db[match.group(0)] = [line]

for command in stats_db:
	print(command + ': ' + str(len(stats_db[command])))
# print(stats_db)
