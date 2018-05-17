
#!/usr/bin/env python

"""whatsapp_stats.py: Simple whatsapp word counting tool."""

import re

data = {}
timeframe = 'before'

with open('input.txt') as inputfile:
	for line in inputfile:
		# if there is text
		if len(line) > 0:
			# if date, time, and author present then update key info and strip that data
			if (re.match('[0-9]+/[0-9]+/[0-9]+, [0-9]+:[0-9]+ - [A-Za-z ]+:', line)):
				date = line.split(',')[0]
				day = date.split('/')[1]
				year = date.split('/')[2]
				author = line.split('-')[1].split(':')[0].strip()
				line = line.split(':',2)[2]
				if int(year) > 16:
					timeframe = 'after'
			if author not in data:
				data[author] = {'before':{}, 'after':{}}
			if date not in data[author][timeframe]:
				data[author][timeframe][date] = {'msg_cnt':0,'word_cnt':0}
			data[author][timeframe][date]['msg_cnt'] += 1
			data[author][timeframe][date]['word_cnt'] += len(line.split())


	for author, tfs in data.items():
		day_cnt = 0.0
		msg_cnt = 0.0
		word_cnt = 0.0
		for tf, dates in tfs.items():
			for date, counts in dates.items():
				day_cnt += 1
				msg_cnt += counts['msg_cnt']
				word_cnt += counts['word_cnt']
			print (author + ' wrote ' + str(msg_cnt / day_cnt) + ' messages per day with an average of ' + str(word_cnt / msg_cnt) + ' words per message ' + tf)

