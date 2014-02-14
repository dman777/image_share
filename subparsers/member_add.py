# member add
def member_add_subparser(subparser):
    member_add = subparser.add_parser('add-member',
                                      description='***Add member to image',
                                      help="Add member to image")
    member_add.add_argument('-pn',
                            '--producer-username',
                            required=True,
                            help="Producer\'s(source account) username")
    member_add.add_argument('-pa',
                            '--producer-apikey',
                            required=True,
                            help="Producer\'s(source account) apikey")

    member_add.add_argument('-u',
                            '--uuid',
                            required=True,
                            help="Image ID number")

    member_add.add_argument('-t',
                            '--consumer-tenantid',
                            required=True,
                            help="Consumer Tenant Id")
