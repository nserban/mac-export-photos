# Mac Export Photos
##### Mac Export Photos preserving creation date and time.


### Description
Exporting original photos from Mac Photos in a separate folder **preserving creation date and time** for files.
Export can be done by year and month.


### Installation
1. Copy file mac-export-photos.py in your home folder. 
2. Make file mac-export-photos.py executable. In Mac Terminal  ``chmod a+x ~/mac-export-photos.py``

#### Usage
Run in Mac Terminal
```bash
cd ~
./mac-export-photos.py
``` 

### Examples
##### Export photos and videos for a specific month 
i.e. May 2017
```bash
./mac-export-photos.py --year 2017 --month 05 --destination <destination_folder> 
```

##### Export photos and videos with the CORRECT HOUR
Mac Photos is storing photos time in UTC (Coordinated Universal Time). For the correct hour use parameter ``--hours-offset`` 

i.e. If your photos are taken in Berlin use:
```bash
./mac-export-photos.py --year 2017 --month 05 --destination <destination_folder> --hours-offset 2
```

i.e. If your photos are taken in Bucharest use:
```bash
./mac-export-photos.py --year 2017 --month 05 --destination <destination_folder> --hours-offset 3
```

##### Export files filtered by extension
```bash
./mac-export-photos.py --year 2016 --month 04 --destination <destination_folder> --filter MOV
```

#### Help
```bash
Mac Export Photos preserving creation date and time.

optional arguments:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR  Year
  -m MONTH, --month MONTH
                        Month
  -d DESTINATION, --destination DESTINATION
                        Destination folder
  -ho HOURS_OFFSET, --hours-offset HOURS_OFFSET
                        Hours offset in hours
  -f FILTER, --filter FILTER
                        Filter files by extension. i.e. JPG, MOV
```
