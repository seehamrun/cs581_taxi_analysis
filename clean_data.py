import csv

with open('data/yellow_tripdata_2019-01.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    valid_trips = []

    for row in csv_reader:
        #     print(str(row["PULocationID"]) + " " + str(row["DOLocationID"]) + " " + str(row["passenger_count"]))
        if (row["PULocationID"] == 138 or row["DOLocationID"] == 138):
        	valid_trips.append(row)

        line_count += 1

    print('Processed ' + str(line_count) + ' lines.')    
    print('Kept ' + str(len(valid_trips)) + ' lines.')