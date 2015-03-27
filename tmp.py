import datetime
now = datetime.datetime.now()
date = str(now).split(' ')[0].replace('-', '')
f = open('tmp.txt', 'w')
f.write(date)
f.close()
