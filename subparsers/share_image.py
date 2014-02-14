#share image subprocesser 
def share_image_subparser(subparser):
    share = subparser.add_parser('share-image',
                                 help="Share image from 2 accounts")
    share.add_argument('-pn',
                       '--producer-username',
                       required=True,
                       help="Producer\'s(source account) username")
    share.add_argument('-cn',
                       '--consumer-username',
                       required=True,
                       help="Consumer\'s(destination account) username")
    share.add_argument('-pa',
                       '--producer-apikey',
                       required=True,
                       help="Producer\'s(source account) apikey")
    share.add_argument('-ca',
                       '--consumer-apikey',
                       required=True,
                       help="Consumer\'s(destination account) apikey")
    share.add_argument('-u',
                       '--uuid',
                       required=True,
                       help="Image ID number")
