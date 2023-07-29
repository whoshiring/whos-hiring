BOT_NAME = "aggregator"

SPIDER_MODULES = ["aggregator.spiders"]
NEWSPIDER_MODULE = "aggregator.spiders"


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# ScrapeOps API Key
SCRAPEOPS_API_KEY = "8eea4c8b-8c9b-45dc-82e9-60b5bda55d14"

# ScrapeOps API Endpoint
SCRAPEOPS_API_ENDPOINT = "https://proxy.scrapeops.io/v1/?"

# Enable ScrapeOps Proxy
SCRAPEOPS_PROXY_ENABLED = True

# Add In The ScrapeOps Monitoring Extension
EXTENSIONS = {
    "scrapeops_scrapy.extension.ScrapeOpsMonitor": 500,
}


DOWNLOADER_MIDDLEWARES = {
    # ScrapeOps Monitor
    "scrapeops_scrapy.middleware.retry.RetryMiddleware": 550,
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
    # Proxy Middleware
    "aggregator.middlewares.ScrapeOpsProxyMiddleware": 725,
}

# Max Concurrency On ScrapeOps Proxy Free Plan is 1 thread
CONCURRENT_REQUESTS = 1
