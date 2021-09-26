from src.jobs import read


def get_unique_job_types(path):

    readed_jobs = read(path)

    unique_jobs = set()
    for jobs in readed_jobs:
        unique_jobs.add(jobs['job_type'])
    return unique_jobs


# get_unique_job_types("jobs.csv")


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

    readed_jobs = read(path)

    unique_industries = set()
    for jobs in readed_jobs:
        if jobs['industry'] != '':
            unique_industries.add(jobs['industry'])
    return unique_industries


# get_unique_industries("jobs.csv")


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

    readed_jobs = read(path)

    salary = 0
    for jobs in readed_jobs:
        if jobs['max_salary'].isdigit() and int(jobs['max_salary']) > salary:
            salary = int(jobs['max_salary'])
    return salary


def get_min_salary(path):

    readed_jobs = read(path)

    salary = 1000000
    for jobs in readed_jobs:
        if jobs['min_salary'].isdigit() and int(jobs['min_salary']) < salary:
            salary = int(jobs['min_salary'])
    return salary


# get_min_salary('jobs.csv')


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
