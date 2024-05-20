# pmm_v2_release_notes_search
Web crawler to search for keywords in PMM v2 release notes pages.

## Installing dependencies

```
pip3 install bs4
pip3 install requests
```

## Running the crawler

There are two ways to run it:

1- Include search words in the command itself:

```
shell> python3 crawl_pmmv2_releases.py "prometheus query builder"
Crawling page: https://docs.percona.com/percona-monitoring-and-management/release-notes/2.41.2.html
```

2- Run without parameters, and reply to the prompt:
```
shell> python3 crawl_pmmv2_releases.py
Enter the keyword(s) to search for: prometheus query builder
Crawling page: https://docs.percona.com/percona-monitoring-and-management/release-notes/2.41.2.html
[...]
```
