import os
import time

source = ['/Users/luqi/GitHub/Byte-of-Python/C12-Problem-Solving']

target_dir = '/Users/luqi/GitHub/Byte-of-Python/backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Enter a comment --> ')
if len(comment) == 0:
  target = today + os.sep + now + '.zip'
else:
  target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
  os.mkdir(today)
  print('Successfully created directory', today)

zip_command = "zip -r {} {}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
  print('Successful backup to', target)
else:
  print('Backup FAILED')
