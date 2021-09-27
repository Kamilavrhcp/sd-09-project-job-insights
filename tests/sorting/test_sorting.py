from src.sorting import sort_by


def test_sort_by_criteria():
    list_jobs = [
      {
        "job_name": "Programador Fullstack",
        "min_salary": "3500",
        "max_salary": "12000",
        "date_posted": "27-09-2021"
      },
      {
        "job_name": "Programador Front-End",
        "min_salary": "4500",
        "max_salary": "13000",
        "date_posted": "28-09-2000"
      },
      {
        "job_name": "Programador Back-end",
        "min_salary": "5000",
        "max_salary": "14000",
        "date_posted": "30-09-2019"
      },
    ]

    # date_posted = [
    #   list_jobs[0],
    #   list_jobs[2],
    #   list_jobs[1],
    # ]

    min_salary = [
      list_jobs[0],
      list_jobs[1],
      list_jobs[2],
    ]

    max_salary = [
      list_jobs[2],
      list_jobs[1],
      list_jobs[0],
    ]

    sort_by(list_jobs, "min_salary")
    assert list_jobs == min_salary

    sort_by(list_jobs, "max_salary")
    assert list_jobs == max_salary

    # sort_by(list_jobs, "date_posted")
    # assert list_jobs == date_posted
