#!/usr/bin/python

import argparse
import datetime
import getpass
import os.path
import time
from shutil import copyfile

parser = argparse.ArgumentParser(
    description="Mac Export Photos preserving creation date and time.",
    formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument('-y', '--year', required=True,
                    help='Year')
parser.add_argument('-m', '--month', required=True,
                    help='Month')
parser.add_argument('-d', '--destination', required=True,
                    help='Destination folder')
parser.add_argument('-ho', '--hours-offset', required=False, default=0,
                    help='Hours offset in hours')
parser.add_argument('-f', '--filter', required=False, default=None,
                    help='Filter files by extension. i.e. JPG, MOV')

args = parser.parse_args()

# Parameters
year = args.year
month = args.month.zfill(2)
destination_folder = args.destination
osx_user = getpass.getuser()
time_offset = int(args.hours_offset) * 3600
file_filter = args.filter
container = []

print("Mac Export Photos preserving creation date and time.")
print("Year={}, Month={}, User={}, TimeOffset={}, Filter={}, Destination={}".format(year, month, osx_user, time_offset,
                                                                                    file_filter, destination_folder))


class File:
    file_name = ''
    source_file_path = ''
    dst_folder = ''
    dst_file_path = ''
    creation_timestamp = 0

    def __init__(self, file_name, source_file_path, dst_folder, dst_file_path, creation_timestamp):
        self.file_name = file_name
        self.source_file_path = source_file_path
        self.dst_folder = destination_folder
        self.dst_folder = dst_folder
        self.dst_file_path = dst_file_path
        self.creation_timestamp = creation_timestamp


FOLDER_SOURCE_MASTER = "/Users/" + osx_user + "/Pictures/Photos Library.photoslibrary/Masters/" + year + "/" + month + "/"

# Check folder source master
if not os.path.isdir(FOLDER_SOURCE_MASTER):
    print("No Photos source was found !")
    exit(1)

# Scan Photo source master
print("Scan Photos ...")
for root, directories, filenames in os.walk(FOLDER_SOURCE_MASTER):
    if len(filenames) > 0:
        for filename in filenames:
            file_path = os.path.join(root, filename)
            file_parts = file_path.replace(FOLDER_SOURCE_MASTER, "").split('/')
            time_parts = str(file_parts[1]).split('-')
            str_date = time_parts[0]
            str_hour = time_parts[1]
            timestamp = time.mktime(
                datetime.datetime.strptime(str_date + ' ' + str_hour, "%Y%m%d %H%M%S").timetuple())
            # Add Time offset
            timestamp += time_offset
            extension = os.path.splitext(file_path)[1][1:]

            if (file_filter is None and extension in ['JPG', 'MOV']) or (
                    file_filter is not None and extension == file_filter):
                dst_folder = destination_folder + "/" + year + "/" + month
                dst_file_path = dst_folder + "/" + filename

                f = File(file_name=filename, source_file_path=file_path, dst_folder=dst_folder,
                         dst_file_path=dst_file_path,
                         creation_timestamp=timestamp)
                container.append(f)

print("Found {}".format(len(container)))

print("Copy files ...")
for f in container:
    dst_folder = f.dst_folder
    if not os.path.isdir(dst_folder):
        os.makedirs(dst_folder)
    copyfile(f.source_file_path, f.dst_file_path)
    os.utime(f.dst_file_path, (f.creation_timestamp, f.creation_timestamp))
print("DONE")
