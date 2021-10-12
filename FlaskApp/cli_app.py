import argparse
import csv

parser = argparse.ArgumentParser(description='Add new films and ratings')
parser.add_argument('--film_name', type=str, required=True)
parser.add_argument('--stars', type=str, required=True)
args = parser.parse_args()

with open('films.txt', 'a', newline='') as filmsFile:
    csv_writer = csv.writer(filmsFile)
    print([args.film_name, args.stars])
    csv_writer.writerow([args.film_name, args.stars])
