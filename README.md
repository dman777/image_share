#Image Share ![alt text](https://raw2.github.com/dman777/icons/master/team.png)
#####Version 2.0
##Introduction
This is a utility to share a image between 2 Rackspace accounts. 
With this utility you may:
* Complete all steps for sharing a image in one command
* List Members of a image. This is done by Producer or Consumer.
* Add members to a image. This is done by the Producer.
* Delete members from a image. This is done by the Producer.
* Change member status of image to accepted, rejected, or pending. This is done by the Consumer.
* (Ver 2.0)List all images from a account with optional query search parameters. This can be done by Producer or Consumer.
* (Ver 2.0)List custom only images. This can be done by Producer or Consumer.
* List detail of a image. This can be done by Producer or Consumer.

##Synopsis
The Producer is the owner/account of the image. The Consumer will be the account that will be using the image. The Producer marks
it's image by adding the tenant ID of the Consumer to the image. This is known as adding a member. Once the Consumer accepts membership by marking that same 
image url as "accepted", the Consumer can use that image to deploy servers. 

<span class="octicon-stop"></span>
*The consumer never owns the image that it is sharing. Basically, it only has a reference to the Producers image. If the consumer wants to own the
image, the consumer should deploy a server from the shared image and make a image of that server. Then the consumer will own 
a copy of the shared image.*

##Usage
Each action you would to take...rather it be `share-image`, `add-member`, `remove-member`, `set-status`, `list-images`, `list-members`, etc...you will want to treat these as subcommands or positional parameters. 

######Example 1:

     	// After script name, specify region. After region, specify subcommand:
	    ./image_share.py -r iad list-images --help

######Example 2:

    	//Share a image. NOTE: This conveniently adds member to Producer's image and accepts membership of image on behalf of the consumer for you.
    	//So, everything is done in just one subcommand called 'share-image'
    	./image-share -r iad share-image\
    	-pn producers_name -pa producers_apikey\
    	-cn consumers_name -ca consumers_apikey
    	-u uuid_of_image_to_be_shared_that_resides_on_producers_account

######Example 3:

       //After successfull image share, verify image is available on consumers account
       // by looking at the image detail
  	  ./image_share.py -r iad list-single-image -cn consumers_name -ca consumers_apikey -u uuid_of_image
  	  
  	  //On a side note, a user can list their entire image collection with:
  	  ./image_share.py -r iad list-single-image -cn consumers_name -ca consumers_apikey

######Example 4:

        //List all images of a account. Use query search for images that are in "share" status
        // and member status "accepted"
        ./image_share.py -r iad list-all-images -pn -cn consumers_name -ca consumers_apikey --visibility shared --member-status accepted
	    


