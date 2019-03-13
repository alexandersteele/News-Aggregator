import requests
import sys

s = requests.Session()
def login(login_url, username, password):

    

    response = s.post(login_url, data={'username': username, 'password': password})
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
    response = s.post(post_url, data={'headline': headline, 'category': category,
    'region': region, 'details': details})

    print(response.content)

def deletestory(delete_url, id):
    response = s.post(delete_url, data={'id': id})

    print(response.content)

def getstory (get_url, category, region, date):
    response = s.get(get_url, params={'category': category, 'region': region, 'date': date})

    print(response.content)

def register (register_url, agency_name, agency_url, agency_code):
    response = s.post(register_url, data={'agency_name': agency_name, 'url': agency_url,
    'agency_code': agency_code})

    print(response.content)

if (len(sys.argv) == 3):
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
               logout(url + "/api/logout/")

            if(command == "post"):
                headline =input("Headline: ")
                category =input("Category: ")
                region =input("Region: ")
                details =input("Details: ")
                poststory(url + "/api/poststory/", headline, category, region, details)

            if (command == "register"):
                agency_name = input("Agency name: ")
                agency_url = input("Agency URL: ")
                agency_code = input("Agency code: ")
                register(url+ "/api/register", agency_name, agency_url, agency_code)

            if (command == "list"):
                 getstory(url + "/api/getstories/", "*", "*", "*")

            x = command.split()
            
            if (x[0] == "delete"):
                deletestory(url + "/api/deletestory/", x[1])

            if (command == "news"):
                category =input("Category: ")
                region =input("Region: ")
                date =input("Date: ")
                getstory(url + "/api/getstories/", category, region, date)
