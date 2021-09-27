from src.jobs import read
#   from jobs import read


def get_unique_job_types(path):
    job_types = read(path)

    jobs_unique = set()

    for row in job_types:
        jobs_unique.add(row["job_type"])

    return jobs_unique


# print(get_unique_job_types("src/jobs.csv"))


def filter_by_job_type(jobs, job_type):
    filter_job_type = []

    for job in jobs:
        if job["job_type"] == job_type:
            filter_job_type.append(job)

    return filter_job_type


def get_unique_industries(path):
    job_industries = read(path)

    industries_unique = set()

    for row in job_industries:
        if row["industry"] != '':
            industries_unique.add(row["industry"])

    return industries_unique


# print(get_unique_industries('src/jobs.csv'))


def filter_by_industry(jobs, industry):
    filter_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filter_industry.append(job)

    return filter_industry


def get_max_salary(path):
    job_max_salary = read(path)

    salary_max = []

    for row in job_max_salary:
        if row["max_salary"] != '' and row["max_salary"].isdigit():
            # https://www.programiz.com/python-programming/methods/string/isdigit
            salary_max.append(int(row["max_salary"]))
            # try:
            #     if salary_max < int(row["max_salary"]):
            #         salary_max = int(row["max_salary"])
            # except ValueError:
            #     print("Não deu certo. Tente outra vez!")

    return max(salary_max)


# print(get_max_salary("src/jobs.csv"))


def get_min_salary(path):
    job_min_salary = read(path)

    salary_min = []

    for row in job_min_salary:
        if row["min_salary"] != '' and row["min_salary"].isdigit():
            salary_min.append(int(row["min_salary"]))

    return min(salary_min)


# print(get_min_salary("src/jobs.csv"))


def matches_salary_range(job, salary):
    # Raquel e Daniela me auxiliaram no uso do raise.
    # raise usa-se para lançar um erro
    # try except para tratar erros
    if ("min_salary" or "max_salary") not in job:
        raise ValueError("Busca não encontrada")
    elif type(job["min_salary"] or job["max_salary"] or salary) != int:
        # entender sobre salary
        raise ValueError("Busca não encontrada")
    elif (job["min_salary"] > job["max_salary"]):
        raise ValueError("Busca não encontrada")
    # elif isinstance(salary, int):
    #     raise ValueError("Busca não encontrada") preciso entender pq
    # aqui não funciona
    elif (job["min_salary"] <= salary <= job["max_salary"]):
        return True

    return False


def filter_by_salary_range(jobs, salary):
    salary_range = []

    for job in jobs:
        try:
            if isinstance(salary, int) and matches_salary_range(job, salary):
                salary_range.append(job)
        except ValueError:
            print("Ocorreu um erro, tente novamente!")

    return salary_range
