import sys
import json
import requests


def authenticate(username, apikey, region):
    """Authenticates user using apikey"""
    region = region.upper()
    user_data = []
    url = 'https://identity.api.rackspacecloud.com/v2.0/tokens'
    print 'Initializing token for {}....'.format(username),
    try:
        jsonreq = {
            'auth': {'RAX-KSKEY:apiKeyCredentials': {'username': username,
                                                     'apiKey': apikey}}}
        auth_headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(jsonreq), headers=auth_headers)
        if r.status_code == 401:
            print "Apikey did not work for {}!".format(username)
            sys.exit()
        print "Done!"
        jsonresp = json.loads(r.text)
        tenant = str(jsonresp['access']['token']['tenant']['id'])
        token = str(jsonresp['access']['token']['id'])
        endpoint = get_link(jsonresp, username, region) + "/images"
        user_data.append(tenant)
        user_data.append(token)
        user_data.append(endpoint)
        return user_data
    except requests.exceptions.ConnectionError:
        print "Connection Error! Http status Code {}".format(r.status_code)
        sys.exit()
    except requests.exceptions.RequestException:
        print "Ambiguous Error! Http status Code {}".format(r.status_code)
        sys.exit()


def get_link(jsonresp, username, region):
    """Gets the endpoints for Cloud files depending on region"""
    foo = jsonresp["access"]["serviceCatalog"]
    index_save = None
    for i in foo:
        if i["name"] == "cloudImages":
            for index, value in enumerate(i["endpoints"]): 
                if str(value["region"]) == region:
                    bar = i
                    index_save = index
    try:
        region = str(bar["endpoints"][index_save]["publicURL"])
    except:
        print "\nThere's no image endpoint for {}!".format(username)
        sys.exit()
    return region
