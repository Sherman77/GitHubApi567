"""SSW567_HomeWork_Week4
    Xiaomeng Xu"""

import requests


def get_id():
    """Get user's Github id"""
    g_id = input("Please enter your Github user ID:")
    return g_id

def get_repository(g_id):
    """Based on user's ID, retrive names of his/her repositories, return as a list"""
    url = f"https://api.github.com/users/{g_id}/repos"
    github = requests.get(url).json()   #Request data through URL
    name = []
    if not isinstance(github, list):
        raise ValueError(f"{github['message']}")
    for i in github:
        name.append(i['name'])
    return name


def get_commit(g_id, repo_name):
    """Get number of commits based on name of repository"""
    url = f"https://api.github.com/repos/{g_id}/{repo_name}/commits"
    commit = requests.get(url).json()
    return len(commit)

'''def main():
    """Main function"""
    switch = True
    while switch:
        g_id = get_id()
        try:
            name = get_repository(g_id)
        except ValueError as err:
            print(err)
        else:
            switch = False

    for i in name:
        print(f"Repo: {i}   Number of commits: {get_commit(g_id, i)}")

if __name__ == '__main__':
    main()'''
