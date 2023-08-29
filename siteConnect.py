import urllib.request as urllib
def siteConnectivityChecker(url):
    print('This is a site connectivity checker program')
    response = urllib.urlopen(url)
    print("Checking connectivity...")
    print(response)
    print('Connected to ',url,'successfully')
    print('The resoonse code was ',response.getcode())

input_url = input('Input the url of the site you want to check: ')
siteConnectivityChecker(input_url)

