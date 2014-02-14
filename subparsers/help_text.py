desc = ('''\
        Image sharing between two seperate accounts
        --------------------------------------------
        Quick help:
        1) Begin with specifying the region with -r {dfw,ord,syd,hkg,iad}
        2) Your subcommand is the action you want to do. For instance,
           to share a image between 2 accounts in ord you would 
           start with:
           ./image_share.py -r ord share-image --help
        3) The --help in the above instance will give you help per
           the subcommand that is before it. 
        4) Remember, the Producer is the account source and 
           the Consumer is the account that will be sharing the image.
        TIP: If you want to share a image in just one step, 'share-image'
             subcommand will do all the work. It will automatically add the 
             consumer as a member and accept membership on it's behalf.
             ''')
epi = ('''\
        Example for sharing a image:
        -------------------------
        ./image-share.py -r iad share-image \\
        -pn source_account_name -pa source_account_apikey\\
        -cn destination_account_name -ca destination_account_apikey\\
        -u the_uuid_of_image
            ''')
