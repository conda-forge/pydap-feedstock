from pydap.client import open_url

# OPeNDAP.
# TODO: charset issue with webop.
#url = 'http://geoport-dev.whoi.edu/thredds/dodsC/estofs/atlantic'
# works for now
# gunicorn
url = 'http://tds.marine.rutgers.edu/thredds/dodsC/roms/espresso/2013_da/his/ESPRESSO_Real-Time_v2_History_Best'
ds = open_url(url)
