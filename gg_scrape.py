import requests
from bs4 import BeautifulSoup


def recursive_url(root, url, depth):
    if depth == 1:
        return url

    source_code = requests.get(root + url).text
    soup = BeautifulSoup(source_code, 'html.parser')

    new_url = soup.find('a')['href']
    print(new_url)
    if len(new_url) == 0:
        return url
    else:
        return url, recursive_url(root, new_url, depth + 1)


def get_links(root):
    source_code = requests.get(root).text
    soup = BeautifulSoup(source_code, 'html.parser')

    links = []
    for link in soup.findAll('a'):
        links.append(recursive_url(root, link['href'], 0))
        if '#' not in link['href'] and 'https' not in link['href']:
            links.append(link['href'])

    return links


def get_words_language(url, language):
    source_code = requests.get(url + '?locale=' + language).text
    soup = BeautifulSoup(source_code, 'html.parser')

    words_hash = {}

    print('Language: ' + language)

    element_search = ['p', 'a', 'span', 'li'] + ['h' + str(i + 1) for i in range(5)]
    print(element_search)
    print('All DOM elements: ' + str(len(soup.findAll(element_search))))

    for each_text in soup.findAll(element_search):
        content = each_text.text
        words = content.lower().split()

        for each_word in words:
            symbols = '!-©@#$%^&*()_-+={[}]|\;:"<>?/.,"\' '
            word = each_word
            for symbol in symbols:
                word = word.replace(symbol, '')
            if word in words_hash:
                words_hash[word] += 1
            else:
                words_hash[word] = 1

    # c = Counter(words_hash)
    # top = c.most_common()
    # print(top)
    return words_hash


def get_missing_translate(url):
    en_words_hash = get_words_language(url, 'en')
    fr_words_hash = get_words_language(url, 'fr')

    missing_translate = {}

    for key, value in en_words_hash.items():
        if key in fr_words_hash:
            if value != fr_words_hash[key]:
                missing_translate[key] = fr_words_hash[key]
            else:
                missing_translate[key] = value

    print(set(fr_words_hash.items()) - set(en_words_hash.items()))
    percent = 100 - sum(missing_translate.values()) * 100 / sum(en_words_hash.values())
    print("Page: {} is {:.2f}% completed".format(url, percent))


def start(url):
    # print(get_links(url))
    get_missing_translate(url)


if __name__ == '__main__':
    # start("https://www.golfgenius.com/")
    start("http://localhost:3000/")
