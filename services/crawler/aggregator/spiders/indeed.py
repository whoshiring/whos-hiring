import json
import re

import scrapy

# FIXME: before deploying remove `services.crawler` prefix
from services.crawler.aggregator.utils.helpers import (
    get_indeed_search_url,
    get_indeed_job_details_url,
)
from services.crawler.aggregator.utils.constants import (
    DEFAULT_KEYWORD_LIST,
    DEFAULT_LOCATION_LIST,
)


def create_job_item(job, location, keyword, offset, jobkey, position):
    job_item = {
        # meta
        "query_keyword": keyword,
        "query_location": location,
        "serp": round(offset / 10) + 1 if offset > 0 else 1,
        "serp_position": position,
        "source": "indeed",
        # data
        "company": job.get("company"),
        "company_rating": job.get("companyRating"),
        "company_review_count": job.get("companyReviewCount"),
        # "highlyRatedEmployer": job.get("highlyRatedEmployer"),
        "jobkey": jobkey,
        "job_title": job.get("title"),
        "job_location_city": job.get("jobLocationCity"),
        "job_location_postal": job.get("jobLocationPostal"),
        "job_location_state": job.get("jobLocationState"),
        "max_salary": job.get("estimatedSalary").get("max")
        if job.get("estimatedSalary") is not None
        else 0,
        "min_salary": job.get("estimatedSalary").get("min")
        if job.get("estimatedSalary") is not None
        else 0,
        "salary_type": job.get("estimatedSalary").get("type")
        if job.get("estimatedSalary") is not None
        else "none",
        "pub_date": job.get("pubDate"),
        "apply_link": job.get("thirdPartyApplyUrl"),
    }
    return job_item


class IndeedSpider(scrapy.Spider):
    name = "indeed"
    custom_settings = {
        "FEEDS": {
            "data/%(name)s_%(time)s.csv": {
                "format": "csv",
            }
        }
    }

    def start_requests(self):
        keyword_list = DEFAULT_KEYWORD_LIST
        location_list = ["Atlanta, GA"]
        for keyword in keyword_list:
            for location in location_list:
                indeed_jobs_url = get_indeed_search_url(keyword, location)
                yield scrapy.Request(
                    url=indeed_jobs_url,
                    callback=self.parse_search_results,
                    meta={"keyword": keyword, "location": location, "offset": 0},
                )

    def parse_search_results(self, response):
        location = response.meta["location"]
        keyword = response.meta["keyword"]
        offset = response.meta["offset"]
        script_tag = re.findall(
            r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});',
            response.text,
        )
        if script_tag is not None:
            json_blob = json.loads(script_tag[0])

            # Extract Jobs From Search Page
            jobs_list = json_blob["metaData"]["mosaicProviderJobCardsModel"]["results"]
            for index, job in enumerate(jobs_list):
                jobkey = job.get("jobkey")
                if jobkey is not None:
                    job_url = get_indeed_job_details_url(jobkey)
                    # FIXME: use an actual Item object
                    indeed_job_item = create_job_item(
                        job, location, keyword, offset, jobkey, index
                    )
                    yield scrapy.Request(
                        url=job_url,
                        callback=self.parse_job,
                        meta={
                            "jobKey": jobkey,
                            "job_item": indeed_job_item,
                        },
                    )

    def parse_job(self, response):
        item = response.meta["job_item"]
        script_tag = re.findall(r"_initialData=(\{.+?\});", response.text)
        if script_tag is not None:
            json_blob = json.loads(script_tag[0])
            job = json_blob["jobInfoWrapperModel"]["jobInfoModel"]
            item["description"] = (
                job.get("sanitizedJobDescription")
                if job.get("sanitizedJobDescription") is not None
                else ""
            )

            yield item
