import sys
from functools import wraps
import json
from modules.do_request import do_request, do_raw_request


def mutate_url_servers_endpoint(producer_data):
    return (producer_data[0], producer_data[1],
            producer_data[2].replace(".images", ".servers"))


def images_custom_list(args, producer_data):
    tenant, token, url = mutate_url_servers_endpoint(producer_data)

    url = url + '/' + 'detail'
    r = do_raw_request(url, token)
    output = r.json()["images"]
    custom_images_list = [custom_images for custom_images in output
                          if custom_images["metadata"].get('user_id', None)]
    temp_image_list = []
    for image in custom_images_list:
        image_temp = ({"status": image["status"],
                       "links": image["links"][0]["href"],
                       "id": image["id"], "name": image["name"]})
        temp_image_list.append(image_temp)
    if len(temp_image_list):
        print json.dumps(
                { "custom-images": temp_image_list }, indent=2)


def image_list_detail(args, producer_data):
    tenant, token, url = mutate_url_servers_endpoint(producer_data)

    uuid = args['uuid']
    url = url + "/" + uuid
    body, status_code = do_request(url, token)
    print body


def member_add(args, producer_data,
               remove=False, consumer_tenant=None):
    # if called from command line instead of image_share()
    if args.get('consumer_tenantid', None):
        consumer_tenant = args['consumer_tenantid']

    producer_tenant, producer_token, producer_url = producer_data

    uuid = args['uuid']
    url = producer_url + "/" + uuid + "/members"
    json_data = {"member": consumer_tenant}


    if remove:
        print("\nAttempting to remove consumer {}"
              " as member to image {}...".format(consumer_tenant, uuid))
        url = url + "/" + consumer_tenant
        # remove/delete API does not return body
        # so do raw request
        r = do_raw_request(url, producer_token, mode="delete")
        if r.status_code == 204:
            # Delete API does not return anything
            print "Success"
        elif r.status_code == 404:
            print("User {} doesn't exist"
                  " as a member").format(consumer_tenant)
    else:
        print("\nAttempting to add consumer {}"
              " as member to image {}...".format(consumer_tenant, uuid))
        body, status_code = do_request(
            url, producer_token, json_data, mode="post")
        if status_code == 409:
            print "Member already exists!...don't worry...continuing..."
        elif status_code == 404:
            print ("No image found with ID {}." 
                   "\nAre you sure the Producer's image"
                   " resides in region {}?".format(
                       uuid, args["region"]))
            sys.exit()
        else:
            print status_code
            print body
            sys.exit();


def image_share(args, producer_data, consumer_data):
    producer_tenant, producer_token, producer_url = producer_data
    consumer_tenant, consumer_token, consumer_url = consumer_data

    member_add(args, producer_data,
               consumer_tenant=consumer_tenant)
    args['accepted'] = True
    status_code = status_set(args, consumer_data)
    if status_code == 200:
        print "Success!"

def raw_list(function):
    @wraps(function)
    def wrapper(args, producer_data):
        original_function = function(args, producer_data)
        tenant, token, url = producer_data
        body, status_code = do_request(url, token)
        print body
        return original_function
    return wrapper

@raw_list
def member_list(args, producer_data):
    # in argparse, consumer or producer data can be used because
    # consumer is aliased to producer.
    uuid = args['uuid']
    producer_data[2] = producer_data[2] + "/" + uuid + "/members"

@raw_list
def list_all_images(args, producer_data):
    url = producer_data[2]
    url_query = {}
    for key, value in args.iteritems():
        if key == 'visibility' or key == 'owner'\
                or key == 'member_status':
                    if value is not None:
                        url_query[key] = value
    if len(url_query) > 0:
        url = url + "?"
        for key, value in url_query.iteritems():
            url = url + key + '=' + value[0] + "&"
    producer_data[2] = url.rstrip("&")
 
def status_set(args, consumer_data):
    consumer_tenant, consumer_token, consumer_url = consumer_data
    uuid = args['uuid']

    url = consumer_url + "/" + uuid + "/members/" + consumer_tenant
    if args['accepted']:
        status = 'accepted'
    elif args['rejected']:
        status = 'rejected'
    elif args['pending']:
        status = 'pending'

    json_data = {"status": status}

    print ("\nAttempting to set status to "
           "{} for member {}...".format(status, consumer_tenant))
    body, status_code = do_request(url, consumer_token, json_data, mode="put")

    if status_code == 404:
        print("Error....Http Code 404 returned. Are you sure {}"
              " is the Consumer? Only the Consumer can set"
              " status.").format(consumer_tenant)
    else:
        print body
        return status_code
