import os
import time

source = ['/Users/luqi/GitHub/Byte-of-Python/C12-Problem-Solving']

target_dir = '/Users/luqi/GitHub/Byte-of-Python/backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -r {} {}".format(target, ' '.join(source))
print(zip_command)

if os.system(zip_command) == 0:
  print('Successful backup to', target)
else:
  print('Backup FAILED')
