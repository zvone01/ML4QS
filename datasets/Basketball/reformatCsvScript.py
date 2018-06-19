import csv
import re
import json

f = open('Export.csv')
csv_f = csv.reader(f, delimiter='|')

rows = list(csv_f)

sensors = ['LSM6DSM Accelerometer','Step Counter','Motion Accel','LSM6DSM Gyroscope','Gravity','Linear Acceleration','AK09915 Magnetometer','BMP280 Pressure','Orientation','Rotation Vector',]

for name in sensors:
   f = open(name + ".csv","w+")
   f.close()

for row in rows[5:]:
    name = row[1]
    if name in sensors:
        f = open(name + ".csv","a+")
        f.write(name)
        f.write(',smartphone')
        f.write("," + row[3]  + "000000")
        fileLine = row[2]
        fileLine = fileLine.translate(None, '][')
        fileLine = fileLine.strip()
        lineElems = fileLine.split(',')
        for row in lineElems:
            f.write("," + str(float(row)))
        #floats = re.findall(r"[-+]?\d*\.\d+|\d+", row[2])
        #for value in floats:
        #    f.write("," + value)
        f.write('\n')
        f.close()
