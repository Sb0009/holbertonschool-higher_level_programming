#!/usr/bin/python3
'''Script that takes in a URL, sends a request to the URL
 and displays the body of the response (decoded in utf-8).
 '''

import sys
import urllib
import urllib.error

if __name__=="__main__":
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as resp:
            print(resp.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
