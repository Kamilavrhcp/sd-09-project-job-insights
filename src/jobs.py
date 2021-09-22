from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        jobs_list = list(jobs_reader)
    return jobs_list


if __name__ == "__main__":

    read("src/jobs.csv")
