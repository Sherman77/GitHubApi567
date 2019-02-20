"""SSW567_HomeWork_Week4
    Xiaomeng Xu"""

import urllib.request
import json
from collections import defaultdict


def get_id():
    """Get user's Github id"""
    id = input("Please enter your Github user ID:")
    return id

def get_repository(id):
    """Based on user's ID, retrive names of his/her repositories, return as a list"""
    url = f"https://api.github.com/users/{id}/repos"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}    #Add header to shove HTTP err 403
    req = urllib.request.Request(url = url, headers = headers)
    uh = urllib.request.urlopen(req)   #Request data through URL
    data = uh.read().decode()  
    js = json.loads(data)
    name = []
    for i in js:
        name.append(i["name"])
    return (name)

def get_commit(id, repo_name):
    """Get number of commits based on name of repository, count the commits and return as a number"""
    url = f"https://api.github.com/repos/{id}/{repo_name}/commits"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}    #Add header to shove HTTP err 403
    req = urllib.request.Request(url = url, headers = headers)
    uh = urllib.request.urlopen(req)
    data = uh.read().decode()
    js = json.loads(data)
    return (len(js))






def main():
    
    switch = True
    while switch == True:
        id = get_id()
        try:
            name = get_repository(id)
        except urllib.error.HTTPError as err:
            print(err)
        else:
            switch = False

    for i in name:
        print (f"Repo: {i}   Number of commits: {get_commit(id, i)}")
            



"""    id = 'shermannnnn77'
    print(get_repository(id))"""


if __name__ == '__main__':
    main()

