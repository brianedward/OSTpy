# OSTpy

OSTpy.py is a python module that wraps the OST Developers API. 

CLIsamples.py demonstrates how to use each command.

GETTING STARTED
1) Sign-up on https://kit.ost.com.
2) Launch a branded token economy with OST KIT⍺ via web-dash board.
3) Obtain an API Key and API Secret from the OST KIT⍺ Developer API Console
5) In project directory, create a file called "config.py" and put the following variables in here: api_secret, api_key, company UUID. Get these from developer portal in kit.ost.com. This will be hidden from github
6) In same directory, create a file called ".gitignore" and type the path to 'config.py'. (If you have already pushed commits with sensitive data, follow this guide to remove the sensitive info while 
7) Move OSTpy.py and authenticate.py into your project directory wherever you keep your modules (Soon, OSTpy will be available via pip. But until then...)
retaining your commits: https://help.github.com/articles/remove-sensitive-data/)
8) Make sure the modules that OSTpy.py and CLIsamples.py import are found by each file.
9) Open CLIsamples.py in a text editor. To choose command to run, switch 'if False:' to 'if True:' before the desired command. 
10) From command line, run 'python CLIsamples.py' to execute command and see the output logged to terminal.


NEXT STEPS
- build as a PyPI module
