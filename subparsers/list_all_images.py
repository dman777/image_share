# List aa images with query stringa available
def list_all_images_subparser(subparser):
    list_all_images = subparser.add_parser(
                                           'list-all-images',
                                           description=('***List all'
                                                        ' images of'
                                                        ' producers/consumers'
                                                        ' account'),
                                           help=('List all'
                                                 ' images of'
                                                 ' producers/consumers'
                                             ' account'))
    group_key = list_all_images.add_mutually_exclusive_group(required=True)
    group_key.add_argument('-pn',
                           '--producer-username',
                           help="Producer\'s(source account) username")
    group_key.add_argument('-cn',
                           '--consumer-username',
                           dest='producer_username',
                           metavar='CONSUMER_USERNAME',
                           help="Consumer\'s(destination account) username")
    group_apikey = list_all_images.add_mutually_exclusive_group(required=True)
    group_apikey.add_argument('-pa',
                              '--producer-apikey',
                              help="Producer\'s(source account) apikey")
    group_apikey.add_argument('-ca',
                              '--consumer-apikey',
                              dest='producer_apikey',
                              metavar='CONSUMER_APIKEY',
                              help="Consumer\'s(destination account) apikey")
    list_all_images.add_argument('--visibility',
                              nargs=1,
                              help='[shared][private][public]')
    list_all_images.add_argument('--member-status',
                              nargs=1,
                              help='[pending][accepted][rejected][all]')
    list_all_images.add_argument('--owner',
                              nargs=1,
                              help='Owner Id')
