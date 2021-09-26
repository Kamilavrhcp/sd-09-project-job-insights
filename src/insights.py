import csv


def read(path):
    with open(path, mode="r") as file:
        jobs_dictionary = list(csv.DictReader(file))
        return jobs_dictionary


def get_unique_job_types(path):
    jobs_dictionary = read(path)
    job_types = set()
    for job in jobs_dictionary:
        job_types.add(job["job_type"])
    return [*job_types]


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    jobs_dictionary = read(path)
    industry_types = set()
    for row in jobs_dictionary:
        if row["industry"] != "":
            industry_types.add(row["industry"])
    return [*industry_types]


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    jobs_dictionary = read(path)
    max_salary = 0
    for row in jobs_dictionary:
        if row["max_salary"] != "":
            if int(row["max_salary"]) > max_salary:
                max_salary = int(row["max_salary"])

    return max_salary


def get_min_salary(path):
    jobs_dictionary = read(path)
    min_salary = 100000000
    for row in jobs_dictionary:
        if row["min_salary"] != "":
            if 0 < int(row["min_salary"]) < min_salary:
                min_salary = int(row["min_salary"])

    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
