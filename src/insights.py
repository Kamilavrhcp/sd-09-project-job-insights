from src.jobs import read

def get_unique_job_types(path):
    jobs_list = read(path)
    job_types = set()
    for job in jobs_list:
        job_types.add(job["job_type"])
    return job_types



def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs_list = read(path)
    job_industries = set()
    for job in jobs_list:
        job_industries.add(job["industry"])
    return job_industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]



def get_max_salary(path):
    jobs_list = read(path)
    jobs_salary_list = []
    for job in jobs_list:
        if job["max_salary"].isnumeric():
            jobs_salary_list.append(int(job["max_salary"]))
    max_salary = max(jobs_salary_list)
    return max_salary


def get_min_salary(path):
    jobs_list = read(path)
    jobs_salary_list = []
    for job in jobs_list:
        if job["min_salary"].isnumeric():
            jobs_salary_list.append(int(job["min_salary"]))
    min_salary = min(jobs_salary_list)
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
