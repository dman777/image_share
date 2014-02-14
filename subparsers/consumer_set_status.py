# consumer set status
def consumer_set_status_subparser(subparser):
    consumer_status = subparser.add_parser('set-status',
                                           description=('***Consumer '
                                                        'sets membership'))
    consumer_status.add_argument('-cn',
                                 '--consumer-username',
                                 required=True,
                                 help="Consumer username")
    consumer_status.add_argument('-ca',
                                 '--consumer-apikey',
                                 required=True,
                                 help="Consumer\'s(source account) apikey")
    consumer_status.add_argument('-u',
                                 '--uuid',
                                 required=True,
                                 help="Image ID number")
    group_status_set = consumer_status.add_mutually_exclusive_group(
        required=True)
    group_status_set.add_argument('--accepted',
                                  action="store_true",
                                  help="Set status of image to accepted")
    group_status_set.add_argument('--pending',
                                  action="store_true",
                                  help=("Set status of image to pending"
                                        " The image is not visible in the"
                                        " member's image-list, but the "
                                        "member can still boot instances"
                                        " from the image."))
    group_status_set.add_argument('--rejected',
                                  action="store_true",
                                  help="Set status of image to rejected")
