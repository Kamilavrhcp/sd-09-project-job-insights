from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    job_types = set()
    for job in data:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    return [row for row in jobs if row["job_type"] == job_type]


def get_unique_industries(path):
    data = read(path)
    industry_types = set()
    for industry in data:
        if industry["industry"]:
            industry_types.add(industry["industry"])
    return industry_types


def filter_by_industry(jobs, industry):
    return [row for row in jobs if row["job_type"] == industry]
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
    data = read(path)
    salaries = set()
    for salary in data:
        if salary["max_salary"].isnumeric():
            salaries.add(int(salary["max_salary"]))
    max_salary = sorted(salaries)[-1]
    return max_salary


def get_min_salary(path):
    data = read(path)
    salaries = set()
    for salary in data:
        if salary["min_salary"].isnumeric():
            salaries.add(int(salary["min_salary"]))
    min_salary = sorted(salaries)[0]
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
