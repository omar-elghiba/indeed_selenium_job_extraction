import csv

header = ['reference', 'name', 'sections', 'skills', 'tags']

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)