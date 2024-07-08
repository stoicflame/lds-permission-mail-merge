import csv

filename = '/tmp/camp-responses.csv'

with open(filename, 'r') as csvfile, open('field-template.xml', 'r') as t:
    template = t.read()
    datareader = csv.reader(csvfile)
    next(datareader)
    for row in datareader:
        fdf = template.format(*row)
        outfile = row[1].replace(' ', '_')
        with open(f'/tmp/camp-permissions/{outfile}.fdf', 'w') as fdffile:
            fdffile.write(fdf)
