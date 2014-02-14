import argparse
import textwrap
from argparse import RawDescriptionHelpFormatter
import help_text
from subparsers.share_image import share_image_subparser
from subparsers.consumer_set_status import consumer_set_status_subparser
from subparsers.list_custom_images import list_custom_images_subparser
from subparsers.list_all_images import list_all_images_subparser
from subparsers.list_members import list_members_subparser
from subparsers.list_single_image import list_single_image_subparser
from subparsers.member_add import member_add_subparser
from subparsers.member_del import member_del_subparser

def create_args():
    parser = argparse.ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            help_text.desc),
        epilog=textwrap.dedent(help_text.epi))
    parser.add_argument('-r',
                        '--region',
                        required=True,
                        choices=['dfw', 'ord', 'syd', 'hkg', 'iad'])
    subparser = parser.add_subparsers(dest="subcommand")

    share_image_subparser(subparser)
    member_add_subparser(subparser)
    member_del_subparser(subparser)
    consumer_set_status_subparser(subparser)
    list_members_subparser(subparser)
    list_single_image_subparser(subparser)
    list_custom_images_subparser(subparser)
    list_all_images_subparser(subparser)
    
    return parser
