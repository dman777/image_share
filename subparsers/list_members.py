# List Members
def list_members_subparser(subparser):
    list_members = subparser.add_parser('list-members',
                                        description=('***List members of a'
                                                     ' image. These are'
                                                     ' known as the consumers.'
                                                     ' However, for ease of'
                                                     ' use you can specify'
                                                     ' the account as producer'
                                                     ' or consumer since ether'
                                                     ' account can list'
                                                     ' them.'),
                                        help=('List members(consumers)'
                                              ' of a image'))
    group_list_members_name = list_members.add_mutually_exclusive_group(
        required=True)
    group_list_members_name.add_argument('-pn',
                                         '--producer-username',
                                         help=("Producer\'s(source"
                                               " account) username"))
    group_list_members_name.add_argument('-cn',
                                         '--consumer-username',
                                         dest='producer_username',
                                         metavar='CONSUMER_USERNAME',
                                         help=("Consumer\'s(destination"
                                               " account) username"))
    group_list_members_key = list_members.add_mutually_exclusive_group(
        required=True)
    group_list_members_key.add_argument('-pa',
                                        '--producer-apikey',
                                        help=("Producer\'s(source"
                                              " account) apikey"))
    group_list_members_key.add_argument('-ca',
                                        '--consumer-apikey',
                                        metavar='CONSUMER_APIKEY',
                                        dest='producer_apikey',
                                        help=("Consumer\'s(destination"
                                              " account) apikey"))
    list_members.add_argument('-u',
                              '--uuid',
                              required=True,
                              help="Image ID number")
    list_members.add_argument('--visibility',
                              nargs='?',
                              default='None',
                              metavar='',
                              help='[shared][private][public]')
    list_members.add_argument('--member-status',
                              nargs='?',
                              default='None',
                              metavar='',
                              help='[pending][accepted][rejected][all]')
    list_members.add_argument('--owner',
                              nargs='?',
                              default='None',
                              metavar='ownerId',
                              help='[pending][accepted][rejected][all]')
