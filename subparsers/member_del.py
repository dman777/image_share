# member del
def member_del_subparser(subparser):
    member_del = subparser.add_parser('remove-member',
                                      description=('***Remove member'
                                                   ' from image'),
                                      help="Remove member from image")
    member_del.add_argument('-pn',
                            '--producer-username',
                            required=True,
                            help="Producer\'s(source account) username")
    member_del.add_argument('-pa',
                            '--producer-apikey',
                            required=True,
                            help="Producer\'s(source account) apikey")
    member_del.add_argument('-u',
                            '--uuid',
                            required=True,
                            help="Image ID number")
    member_del.add_argument('-t',
                            '--consumer-tenantid',
                            required=True,
                            help="Consumer Tenant Id")
