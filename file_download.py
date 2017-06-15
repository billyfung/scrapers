from bs4 import BeautifulSoup as bs
import csv
import os

import requests
import click


def download_files(savepath,indexURL):
    s = requests.Session()
    d = s.get(indexURL, verify=False)
    soup = bs(d.text)
    for link in soup.findAll("a"):
        modified_on = link.string
        current_link = link.get("href")
        if current_link.endswith('csv'):
            print('Found CSV: ' + current_link)
            print('Downloading %s' % current_link)
            d = s.get('indexURL'+current_link, verify=False)

            content = d.content.decode('utf-8')

            reader = csv.reader(content.splitlines())
            with open(os.path.join(savepath, current_link), 'w') as f:
                writer = csv.writer(f)
                for i, row in enumerate(reader):
                    writer.writerow(row)

@click.command()
@click.option('--savepath', required=True)
@click.option('--indexURL', required=True)
def main(savepath,indexURL):
    download_files(savepath,indexURL)

if __name__ == '__main__':
    main()
