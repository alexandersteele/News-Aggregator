import requests
import sys
import json


s = requests.Session()
def login(login_url, username, password):

    response = s.post(login_url, headers={'content-Type': 'application/x-www-form-urlencoded'}, data={'username': username, 'password': password})
    print(response.content)

    if (str(response.content, 'utf-8') == "Welcome " + username):
        return True
    else:
        return False


def logout(logout_url):
    response = s.post(logout_url, {})
    print(response.content)
    sys.exit(0)


def poststory(post_url, headline, category, region, details):
    response = s.post(post_url, json={'headline': headline, 'category': category,
    'region': region, 'details': details})

    print(response.content)


def deletestory(delete_url, id):
    response = s.post(delete_url, data={'id': id})

    print(response.content)


def get_agent_story (agent_url, category, region, date):

    response = s.get(agent_url, json={'category': category, 'region': region, 'date': date})
    if (response.status_code == 200):
        print(response.content)


def get_agency_stories (get_url, id, category, region, date):

    agencies = agency_list(get_url)
    resp = json.loads(agencies)

    if id is None:
        for agent in resp["agency_list"]:
            agent_url = agent["url"]
            agent_url = agent_url.rstrip('\\')
            get_agent_story(agent_url + "/api/getstories", category, region, date)
    else:
        for agent in resp["agency_list"]:
            if (agent["agency_code"] == id):
                agent_url = agent["url"]
                agent_url = agent_url.rstrip('\\')
                get_agent_story(agent_url + "/api/getstories", category, region, date)


def register (register_url, agency_name, url, agency_code):

    response = s.post(register_url, json={'agency_name': agency_name, 'url': url,
    'agency_code': agency_code})

    print(response.content)


def agency_list (list_url):
    response = s.get(list_url)

    return (response.text)


if (sys.argv[1] == "news"):

    agency_code = None
    category = "*"
    region = "*"
    date = "*"
    
    for arg in sys.argv:

        if ("-id" in arg):
            splt = arg.split("id=")
            agency_code = splt[1]
        if ("-cat" in arg):
            splt = arg.split("cat=")
            category = splt[1]
        if ("-reg" in arg):
            splt = arg.split("reg=")
            region = splt[1]
        if ("-date" in arg):
            splt = arg.split("date=")
            date = splt[1]
        
    get_agency_stories("http://directory.pythonanywhere.com/api/list/", agency_code, category, region, date)


if (sys.argv[1] == "register"):
        url = sys.argv[2]
        agency_name = input("Agency name: ")
        register_url = input("Agency URL: ")
        agency_code = input("Agency code: ")
        register(url + "/api/register/", agency_name, register_url, agency_code)


if (sys.argv[1] == "list"):
    url = sys.argv[2]
    print(agency_list(url + "/api/list/"))

    
if (sys.argv[1] == "login"):
    while (True):
        url = sys.argv[2]
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        l = login(url + "/api/login/", username, password)
        if (l):
            break


    while (True):
        command = input("$ ")
        if (command == "logout"):
            url = sys.argv[2]
            logout(url + "/api/logout/")

        if(command == "post"):
            url = sys.argv[2]
            headline =input("Headline: ")
            category =input("Category: ")
            region =input("Region: ")
            details =input("Details: ")
            poststory(url + "/api/poststory/", headline, category, region, details)

        x = command.split()
        
        if (x[0] == "delete"):
            url = sys.argv[2]
            deletestory(url + "/api/deletestory/", x[1])

    
