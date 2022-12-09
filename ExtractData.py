import requests


def download_file_from_url(url: str):
    """Descarga un archivo desde una url en "./datasets/"

    :param url: URL donde el archivo esta
    :return: None
    """
    r = requests.get(url=url, allow_redirects=True)
    path = "./datasets/"
    name_file = url[url.rfind('/') + 1:]
    open(path + name_file, 'wb').write(r.content)


if __name__ == "__main__":
    url_files = ['https://raw.githubusercontent.com/HX-FAshur/PI01_DATA05/main/Datasets/amazon_prime_titles.csv',
                 'https://raw.githubusercontent.com/HX-FAshur/PI01_DATA05/main/Datasets/disney_plus_titles.csv',
                 'https://raw.githubusercontent.com/HX-FAshur/PI01_DATA05/main/Datasets/hulu_titles.csv',
                 'https://raw.githubusercontent.com/HX-FAshur/PI01_DATA05/main/Datasets/netflix_titles.json']

    for url in url_files:
        download_file_from_url(url=url)
