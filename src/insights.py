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
    if not (isinstance(salary, int)):
        raise ValueError("invalid salary")
    if (
        "min_salary" not in job.keys()
        or not isinstance(job["min_salary"], int)
    ):
        raise ValueError("invalid min_salary")
    if (
        "max_salary" not in job.keys()
        or not isinstance(job["max_salary"], int)
    ):
        raise ValueError("invalid max_salary")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greatter than max_salary")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    return [
        job
        for job in jobs
        if (
            ("min_salary" in job.keys() and "max_salary" in job.keys())
            and (
                isinstance(job["min_salary"], int)
                and isinstance(job["max_salary"], int)
            )
            and job["min_salary"] <= job["max_salary"]
            and (isinstance(salary, int))
            and matches_salary_range(job, salary)
        )
    ]
