# job_scraper
Python Job Scraper
--------------------------------------------------------
Last debug notes: 

Still getting the below error after fixing the URL syntax error
"Failed to retrieve the page. Status code: 403"
-------------------------------------------------------
Last Fix Notes:

Fixed the below error by placing the url in double quotes.

File "/home/kali/python_scripts/job_scraper.py", line 8
    url = https://www.indeed.com/l-brainerd,+mn-jobs.html?vjk=3c1b76a2fc60c7e9
                                                              ^
SyntaxError: invalid decimal literal
