import csv

valid_trips = []

with open('rawdata/yellow_tripdata_2019-01.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if (int(row["PULocationID"]) == 138 or int(row["DOLocationID"]) == 138):
        	valid_trips.append(row)
        line_count += 1

    print('Processed ' + str(line_count) + ' lines.')    
    print('Kept ' + str(len(valid_trips)) + ' lines.')


keys = valid_trips[0].keys()
with open('data/yellow_tripdata_2019-01_LGA.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(valid_trips)
