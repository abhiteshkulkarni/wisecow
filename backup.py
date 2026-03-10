import shutil
import datetime

source = "/home/user/data"
backup = "/home/user/backup"

date = datetime.datetime.now().strftime("%Y-%m-%d")

backup_file = backup + "/backup_" + date

try:
    shutil.make_archive(backup_file, 'zip', source)
    print("Backup completed successfully")
except Exception as e:
    print("Backup failed:", e)

#Example: 0 2 * * * python backup.py
