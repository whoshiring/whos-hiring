from urllib.parse import urlencode


def get_indeed_search_url(keyword, location, offset=0):
    parameters = {"q": keyword, "l": location, "filter": 0, "start": offset}
    return "https://www.indeed.com/jobs?" + urlencode(parameters)


def get_indeed_job_details_url(jobkey):
    return "https://www.indeed.com/m/basecamp/viewjob?viewtype=embedded&jk=" + jobkey
