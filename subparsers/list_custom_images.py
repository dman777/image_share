# List custom images
def list_custom_images_subparser(subparser):
    list_images = subparser.add_parser(
                                       'list-custom-images',
                                       description=('***List custom'
                                                    ' saved images of'
                                                    ' producers/consumers'
                                                    ' account'),
                                       help=('List custom'
                                             ' saved images of'
                                             ' producers/consumers'
                                             ' account'))
    group_key = list_images.add_mutually_exclusive_group(required=True)
    group_key.add_argument('-pn',
                           '--producer-username',
                           help="Producer\'s(source account) username")
    group_key.add_argument('-cn',
                           '--consumer-username',
                           dest='producer_username',
                           metavar='CONSUMER_USERNAME',
                           help="Consumer\'s(destination account) username")
    group_apikey = list_images.add_mutually_exclusive_group(required=True)
    group_apikey.add_argument('-pa',
                              '--producer-apikey',
                              help="Producer\'s(source account) apikey")
    group_apikey.add_argument('-ca',
                              '--consumer-apikey',
                              dest='producer_apikey',
                              metavar='CONSUMER_APIKEY',
                              help="Consumer\'s(destination account) apikey")
    list_images.add_argument('-u',
                             '--uuid',
                             help="Image ID number")
