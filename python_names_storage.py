from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests
import csv

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
 
  
  "type": "service_account",
  "project_id": "optimal-life-382223",
  "private_key_id": "68d56bffa9d19ceff7e20b5e21d68165f8a94a8c",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDWDETzPnbp2VwT\nOCwEkBK+HADAaT1Vwf3mIqyHo6q7FHjcYM/g1C2RP7pSrvSSZQ5R7MOprQTeNxEC\nJCfcJkEKOG193v9AoZEOz6G/p5QP46dc4ONNtzRZvx9STxx/AovvnWR7QCsSVodK\n/5A/gIQyV/to1VATj14ZZ1UH45GSoOd3NBmhe2HYouKSF6d7+NYgQYAWDVxkf/MP\nrexpgrmqUuAgik7v/BHVbFh/UeWmsLNVA8jxRJo8j+z8P097O2nreRgyAu8ZDVe+\nvf7gx1WvPDrSgOfwrvs+nzDcZuqq30EvOw8A+CG/yJQMgC/Vz96ipqu8aaLwgkG7\nO7+VbdGZAgMBAAECggEAGxUKVEx+9y+NOtFMoHcqJ+ubHL00CXm2Cjww4CiRHYKF\nmDyXkLbH3SzXAkcooq0ulqcCSqGdkBAfksnIUU51xDlHgTmJyj+m/ty+dmVZknkX\nX+UEXXzknsZTzDI+RMOpuPONFxsTWAqiq5aSRbaZA1WmdaknrJHjMguk8o6UiJyf\nvDx7TrY1hZ5kuWVNgXbClJRlBd2DHDx5TpVSGhcVESIUaFnfAl2rX3OonPn8PD4s\n1WMmDhREh0WKI3hKBiraw//NdunG77QZttr8ow8gPkFzoAkf7JJzI1EZ+kOOKS0J\n6EheEBMv0Fnnxf/Al4/8s3kITZ1rI2jpS6vfbOKQUQKBgQD+TigGu1ujbXv/fv7E\n90Az9HHQKUM44Ae77AlmbOojsOtjOBNL6JA65iTrOEeOgRGvo6o6x9yXawonq6K4\nrUAQzSVucGueCbnzTGIERTx/8E7JchEgl3LczlwQV+0Ie0Avtd4PQ3wBVUdhTv7U\nKt9phmRr60TthLoVaaeN2LS65wKBgQDXeW8hAIEsFdI46I2egxuMtC29MT/rpRWe\n5u09RI49DY9UFJrYK3XJ7vA9OCQc6ca+68MonOxwH6EkfxfpeAD//gQWt11Xb45g\nxjBm2Ozo2DDvaqnSSXpeOshV4sbuBMtOj+Rl2tZnMQcPbKHhTsvFpOlXch/ehLnT\ngnIjY3//fwKBgBJHvfrV5v11dk9kap3wBA54COJkxO9Gs2efzQEu3RnZsuH7+u8e\n9Zc2SfsanZIx1vqgMjFtgn7j8+PsI5NQ6OUMSh+JN0MyAcrqd7VE4Nd1h8RVTcPg\n/yG+N8H5ABH3AiMr2J2SRUy3O51UF19bAZpNTdSwIdFNFC9L2/6HUF6LAoGBAJ7A\ntFSvR3xQk3MkO3sHA5w1/+D9USfvmC9b2nyibt2iiPAcwjz0QDNIHK4uF8VJpAl0\nMHRSsYymcRYvoVF8/dedsit+a4IJCfBY9L5BosKmzd8HShlJ06NrUcCddY1V8Ohv\n8Yntoruijp4Znmceo9l5eAXaaoqKZVLlL+zM2ThHAoGAWHAdHPTo9/kIMFeg6/W+\nCAJZPWypcn0vgIdoPYIHki1o7AV33I3ToJnUMd5ruJmfyfKR/25l9e/CVlzHKvmL\n6e6/fTWW5md+zHUN6lDsLvbK0m51pnwSFC/aiEkqpF+BEXTHEVJkGhZzXJcNiWxp\nApIWwNwR6iWn5rnmJP9IwIY=\n-----END PRIVATE KEY-----\n",
  "client_email": "untitled@optimal-life-382223.iam.gserviceaccount.com",
  "client_id": "116990924871949476816",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/untitled%40optimal-life-382223.iam.gserviceaccount.com"
} 


try:

  """Uploads a file to the bucket."""
  credentials = service_account.Credentials.from_service_account_info(credentials_dict)
  storage_client = storage.Client(credentials=credentials)
  bucket = storage_client.get_bucket('atividade4dataops') ### Nome do seu bucket
  blob = bucket.blob('artist-names.csv')

  pages = []
  names = "Name \n"

  for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

  for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
      names = names + artist_name.contents[0] + "\n"

    blob.upload_from_string(names, content_type="text/csv")

except Exception as ex:
  print(ex) 
