import os
import time

source = ['/Users/luqi/GitHub/Byte-of-Python/C12-Problem-Solving']

target_dir = '/Users/luqi/GitHub/Byte-of-Python/backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
  os.mkdir(today)
  print('Successfully created directory', today)

target = today + os.sep + now + '.zip'

zip_command = "zip -r {} {}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
  print('Successful backup to', target)
else:
  print('Backup FAILED')
