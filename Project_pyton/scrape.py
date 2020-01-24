from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

search_querries = ['black dress', 'white dress', 'black shoes', 'white shoes', 'black sweatshirt','red sweatshirt',
                   'red t-shirt', 'red dress']


def download_images(query):
    arguments = {
        'keywords': query,
        'format': 'jpg',
        'limit': 60,
        'print_urls': True,
        'size': 'medium',
        'aspect_ratio': 'square',
        'chromedriver': r'‪C:\Users\kkrol\Desktop\chromedriver\chromedriver.exe'
    }

    try:
        response.download(arguments)
    except FileNotFoundError:
        arguments = {
            'keywords': query,
            'format': 'png',
            'limit': 60,
            'print_urls': True,
            'size': 'medium',
            'chromedriver': r'‪C:\Users\kkrol\Desktop\chromedriver\chromedriver.exe'
        }

        try:
            response.download(arguments)
        except:
            pass


for query in search_querries:
    download_images(query)
    print()