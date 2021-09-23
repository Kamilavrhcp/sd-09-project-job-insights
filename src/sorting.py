import math
from datetime import date


# from src.jobs import read


def max_salary_key(job):
    """
    Gets max_salary as a sorting key.

    Missing information is treated as the lowest possible value.

    Parameters
    ----------
    job : dict
        Dict represeting a job from the dataset.

    Returns
    -------
    Job's max salary as an int, or -infinite.
    """
    try:
        return int(job["max_salary"])
    except (KeyError, TypeError, ValueError):
        return -math.inf


def min_salary_key(job):
    """
    Gets min_salary as a sorting key.

    Missing information is treated as the highest possible value.

    Parameters
    ----------
    job : dict
        Dict represeting a job from the dataset.

    Returns
    -------
    Job's min salary as an int, or infinite.
    """
    try:
        return int(job["min_salary"])
    except (KeyError, TypeError, ValueError):
        return math.inf


def date_posted_key(job):
    """
    Gets date_posted as a sorting key.

    Missing information is treated as the lowest possible value.

    Parameters
    ----------
    job : dict
        Dict represeting a job from the dataset.

    Returns
    -------
    Job's date_posted as a date object.
    """
    try:
        return date.fromisoformat(job["date_posted"])
    except (KeyError, TypeError, ValueError):
        return date.min


def sort_by(jobs, criteria):
    criteria_keys = {
        "date_posted": date_posted_key,
        "max_salary": max_salary_key,
        "min_salary": min_salary_key,
    }

    try:
        key = criteria_keys[criteria]
    except KeyError:
        raise ValueError(f"invalid sorting criteria: {criteria}")

    reverse = criteria in ["max_salary", "date_posted"]

    jobs.sort(key=key, reverse=reverse)
