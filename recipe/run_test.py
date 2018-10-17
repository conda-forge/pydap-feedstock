from pydap.client import open_url

url = 'http://geoport-dev.whoi.edu/thredds/dodsC/estofs/atlantic'

ds = open_url(url)