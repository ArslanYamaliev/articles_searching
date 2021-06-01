import requests
from collections import Counter
import re

base_url = 'https://www.osti.gov/api/v1/'


def clean_string(s):
    return re.sub(r'[^\w\s]+|[\d]+', r'', s).strip().lower()


def get_articles(number_of_articles_to_get, publication_date_start=None, publication_date_end=None, page=None):
    payload = {'rows': number_of_articles_to_get}

    if page:
        payload['page'] = page
    if publication_date_start:
        payload['publication_date_start'] = publication_date_start
    if publication_date_end:
        payload['publication_date_end'] = publication_date_end

    res = requests.get(base_url + 'records', params=payload)
    return res.json()


def subject_from_articles(articles):
    subjects = []
    for article in articles:
        for subject in article['subjects']:
            subjects.append(clean_string(subject))
    return subjects


def get_years_of_articles(articles):
    years = []
    for article in articles:
        years.append(article['publication_date'][:4])
    return years


def found_most_tags(tags):
    c = Counter(tags)
    return c.most_common(5)


def get_years_counter(years):
    c = Counter(years)
    return c
