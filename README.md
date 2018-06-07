# OSTpy
Python wrapper around OST api

This version was built with the intention of testing endpoints and writing scripts to automate these processes. Each API call from dev.ost.com is included here and this will be updated as new API features are released. 

To test API calls, uncomment the actions you want to perform in CLIsamples.py

+ API KEY MANAGEMENT(BEFORE YOU COMMIT YOUR BUILD TO GITHUB)
1) In project directory, create a file called "config.py" and put two variables in there: api_secret, api_key. Get these from developer portal in kit.ost.com
2) In same directory, create a file called ".gitignore" and all you need in here is to list the files that you want github to ignore. In mine, I included config.py and config.pyc (although you may not actually need to hide the .pyc file, better safe than sorry)
3) If you have already pushed commits with sensitive data, follow this guide to remove the sensitive info while 
retaining your commits: https://help.github.com/articles/remove-sensitive-data/

