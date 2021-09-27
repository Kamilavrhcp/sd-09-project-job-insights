import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        jobs_data = []
        for row in jobs_reader:
            jobs_data.append(row)

        return jobs_data

# print(read('src/jobs.csv'))
