## Overview
A small collection of quick python exercises.

## Pre-requisites:
- Python3

## Usage: 

### scan_file.py
scan_file.py [-h] [-q QUERY] [-s STATE] [-w] file_name

## Running Help:
```
python3 scan_file.py -h

positional arguments:
  file_name             Name of the file to parse.

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        Specify the query to run. The available query strings
                        are: happy_sre, happy_dancer
  -s STATE, --state STATE
                        Specify the query to run. The available query strings
                        are: happy_sre, happy_dancer
  -w, --swap            For when you want to swap the attributes and state in
                        the data file.

EXAMPLE SCRIPT RUNS AND  OUTPUT:
» ./scan_file.py -q 'happy dancer'  data.txt
Searching: happy dancer
Result: ['Sara', 'Parker']

» ./scan_file.py -q 'sre female'  data.txt
Searching: sre female
Result: ['Zoe']

» ./scan_file.py -q 'likes_pizza'  data.txt
Searching: likes_pizza
Result: ['Sam', 'Parker']

» ./scan_file.py -q 'happy sre' --swap data.txt
Searching: happy sre
Result: ['Joe']
Swapping attributes and states columns in data.txt

>> ls |grep data
-rw-r--r--  1 yleon  staff   312 Aug 14 01:38 data.txt
-rw-r--r--  1 yleon  staff   312 Aug 14 01:38 data.txt.bkup

(python-world3) yleon@khalessi ~/Dev/qzfun/python (master ✗ ◼) » cat data.txt
Sara:lawyer,dancer,loves_sushi,female,not sleepy,happy:california
Zoe:dancer,sre,,female, likes_burritos:colorado
Sam:not dancer,happy,male,likes_pizza:california
Bill:running, bored:utah
Mary:mac_user, dancer,loves_math:arizona
Parker:dancer , likes_pizza, happy:colorado
Joe:sre,happy ,enjoys_music:california

» cat data.txt.bkup
Sara:california:lawyer,dancer,loves_sushi,female,not sleepy,happy
Zoe:colorado:dancer,sre,,female, likes_burritos
Sam:california:not dancer,happy,male,likes_pizza
Bill:utah:running, bored
Mary:arizona:mac_user, dancer,loves_math
Parker:colorado:dancer , likes_pizza, happy
```

### triple_fibonacci.py 
```
python3 triple_fibonacci.py
```

