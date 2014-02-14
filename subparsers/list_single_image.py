# List single image detail
def list_single_image_subparser(subparser):
    list_image = subparser.add_parser('list-single-image',
                                      description=('***List details'
                                                   ' of a single image'),
                                      help=('List details of a single image'
                                            ' of producers/consumers account'))
    group_key = list_image.add_mutually_exclusive_group(required=True)
    group_key.add_argument('-pn',
                           '--producer-username',
                           help="Producer\'s(source account) username")
    group_key.add_argument('-cn',
                           '--consumer-username',
                           dest='producer_username',
                           metavar='CONSUMER_USERNAME',
                           help="Consumer\'s(destination account) username")
    group_apikey = list_image.add_mutually_exclusive_group(required=True)
    group_apikey.add_argument('-pa',
                              '--producer-apikey',
                              help="Producer\'s(source account) apikey")
    group_apikey.add_argument('-ca',
                              '--consumer-apikey',
                              dest='producer_apikey',
                              metavar='CONSUMER_APIKEY',
                              help="Consumer\'s(destination account) apikey")
    list_image.add_argument('-u',
                            '--uuid',
                            required=True,
                            help="Image ID number")
