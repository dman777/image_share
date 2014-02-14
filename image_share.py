#!/usr/bin/env python
# Version 2.0
# 2014 Tron Team.
# Maintained by Darin Hensley
from subparsers.parser_setup import create_args
from modules.auth import authenticate
from modules.actions import status_set, member_list
from modules.actions import member_add, image_share
from modules.actions import image_list_detail, images_custom_list
from modules.actions import list_all_images


def start():
    parser = create_args()
    args = vars(parser.parse_args())
    return args


if __name__ == "__main__":
    args = start()
    if args.get('producer_apikey', None):
        producer_data = authenticate(
            args['producer_username'], args['producer_apikey'], args['region'])
    if args.get('consumer_apikey', None):
        consumer_data = authenticate(
            args['consumer_username'], args['consumer_apikey'], args['region'])

    if args['subcommand'] == "list-custom-images":
        images_custom_list(args, producer_data)
    elif args['subcommand'] == "list-all-images":
        list_all_images(args, producer_data)
    elif args['subcommand'] == "list-single-image":
        image_list_detail(args, producer_data)
    elif args['subcommand'] == "add":
        member_add(args, producer_data)
    elif args['subcommand'] == "list-members":
        member_list(args, producer_data)
    elif args['subcommand'] == "share-image":
        image_share(args, producer_data, consumer_data)
    elif args['subcommand'] == "set-status":
        status_set(args, consumer_data)
    elif args['subcommand'] == "add-member":
        member_add(args, producer_data)
    elif args['subcommand'] == "remove-member":
        member_add(args, producer_data, remove=True)
