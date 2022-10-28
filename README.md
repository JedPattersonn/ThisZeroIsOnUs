# This Zero Is On Us
This Coke is on us code generator. Written in Python


# About 

This is arguably one of my favourite projects I have ever made. The promotion was to promote Coke's "Zero" line of drinks. In participating stores, you would be able to take any of these drinks (e.g. Coke Zero, Dr Pepper Zero) and scan the barcode you are given to get the value of the drink taken off the order. However, the code would work on any product and could be used multiple times per order, effectively getting anthing free.

I was first alerted to this mistake by some friends. They would spend ages getting loads of codes and going into the store to buy lots of food/drink for free. I realised that this process could be automated. I went through the process of getting a code and intercepted all the requests being made.

I noticed that the only unique data being sent to the API was your name, email, date of birth, and the ID of the store you selected. This was all very easy to generate. I would use a random name library to get the name, a special trick to make infinite gmail addresses, and I used the same birthday for every request as that couldn't be used to filter people.

As I was testing the script on my local store, I had hard-coded in the venueID. I did however implement a way for other users to search for their venue using a postcode. Unfortunately, the API to get the locations required co-ordinates so I had to use an API that would convert a postcode into co-ordinates and post that.

This "exploit" lasted just a few days before Coke would patch the part where the same code be used infinitely. A couple days later they fixed the whole exploit and made it 1 code per order which meant you could not get items valued at £1.80 or higher for free.

The people who ran this promotion could have easily prevented this from the start. There are two main ways to prevent this. The first is to communicate better with the retailers and make sure the discount code can only be used on correct products and once per order. The second is to make it harder to generate more than one code per person. You could use anti-bot services like Akamai or PerimterX to validate the requests or add some sort of captcha service that would be harder to solve without the use of external services.








# How to use

Download the `src` folder and run the `menu.py` file. 

To get a venue ID, enter the `Location Finder` section and input your postcode. This will print the nearest stores and their ID.

Once you have your venue ID, select the `Free Coke` option and input your **GMAIL** and the venue ID, as well as how many codes you would like.


After around 20 repetitions, there may be some bugs. Not entirely sure why but open a pull request if you think you have a fix!

Proxies are required in the `proxies.txt` file. I have provided some free one for you but you can add your own if you so wish.
