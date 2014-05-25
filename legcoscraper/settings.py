# Scrapy settings for legcoscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os


BOT_NAME = 'legcoscraper'

SPIDER_MODULES = ['legcoscraper.spiders']
NEWSPIDER_MODULE = 'legcoscraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'legcoscraper (+http://odhk.github.io/)'

# Added as per 
# https://groups.google.com/forum/print/msg/scrapy-users/kzGHFjXywuY/O6PIhoT3thsJ
ITEM_PIPELINES = [
    'scrapy.contrib.pipeline.files.FilesPipeline',
]

# Needs to be absolute for deployment to scrapyd
FILES_STORE = '/var/legco-watch/scrapyd/files'

DOWNLOADER_MIDDLEWARES = {
    # 100 is for the ordering of the middleware pipeline, not for timeout
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 100,
    'scrapy.contrib.downloadermiddleware.stats.DownloaderStats': 101,
}

# load local dev settings
try:
    from scrapy_local import *
except ImportError:
    pass

