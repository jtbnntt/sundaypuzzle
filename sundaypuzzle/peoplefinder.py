import re
import requests
import sys

import lxml.etree as ET

NUMBER_OF_DAYS_BY_MONTH = {
    'January': 31,
    'February': 29,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

URL_TEMPLATE = 'https://en.wikipedia.org/wiki/{}_{}'

PERSON_PATTERN = r'[^a-zA-Z]*(.+?),.*'


def main():
    with open('people.txt', 'w') as output:
        for month, days in NUMBER_OF_DAYS_BY_MONTH.items():
            for i in range(days):
                url = URL_TEMPLATE.format(month, i + 1)
                sys.stdout.write('Processing <{}>...'.format(url))
                r = requests.get(url)
                tree = ET.fromstring(r.text)
                persons = tree.xpath('//div/h2[span[@id="Births"]]'
                                     '/following-sibling::ul[1]/li')
                for person in persons:
                    text = ''.join(person.xpath('./descendant::text()'))
                    m = re.match(PERSON_PATTERN, text)
                    if m:
                        output.write(m.group(1) + '\n')
                print('done.')
    print('Complete.')


if __name__ == '__main__':
    main()
