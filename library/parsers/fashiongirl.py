from tabulate import tabulate
from bs4 import BeautifulSoup
import requests
import base64
import json
import library.files


class Data:
    def __init__(self, url, category) -> None:
        self.url = url
        self.category = category

    def __repr__(self):
        return f"Data(url='{self.url}', category='{self.category}')"


class PostData:
    def __init__(self, photos, title, description, category, subcategory, sizes, colors, amount, price) -> None:
        self.photos = photos
        self.title = title
        self.description = description
        self.category = category
        self.subcategory = subcategory
        self.sizes = sizes
        self.colors = colors
        self.amount = amount
        self.price = price

    def __repr__(self):
        return (f"PostData(photos={self.photos}, title='{self.title}', description='{self.description}', category='{self.category}', subcategory='{self.subcategory}', sizes={self.sizes}, colors={self.colors}, amount={self.amount}, price={self.price})")

    def __str__(self) -> str:
        return (f"PostData(photos={self.photos}, title='{self.title}', description='{self.description}', category='{self.category}', subcategory='{self.subcategory}', sizes={self.sizes}, colors={self.colors}, amount={self.amount}, price={self.price})")


class DataCollection:
    def __init__(self):
        self.data = []

    def put(self, data: Data):
        self.data.append(data)

    def __repr__(self):
        return f"DataCollection(data={self.data})"


class PostDataCollection:
    def __init__(self):
        self.data = []

    def put(self, data: PostData):
        if len(self.data) < 10:
            self.data.append(data)
        else:
            self.save()

    def save(self):
        save_txt = ''
        for data in self.data:
            save_txt += str(data)+'\n'
        library.files.write_txt('data/fashiongirl.data',
                                save_txt)
        self.data = []
        print('save!')

    def __repr__(self):
        return f"PostDataCollection(data={self.data})"


def prepare_data() -> DataCollection:
    with open('library/config/fashiongirl.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    collection = DataCollection()

    for url_cfg in config:
        collection.put(Data(url_cfg, config[url_cfg]))

    return collection


def parsing() -> DataCollection:
    col = prepare_data()
    parsing_col = DataCollection()
    for data in col.data:
        response = requests.get('https://fashion-girl.ua/ua/'+data.url)
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')
        pages = soup.find_all(
            'a', class_='b-goods-title b-product-gallery__title')

        for page in pages:
            href = 'https://fashion-girl.ua'+page.get('href')
            parsing_col.put(Data(href, data.category))

    return parsing_col


def loader(datas: DataCollection) -> PostDataCollection:
    post_col = PostDataCollection()
    for data in datas.data:
        response = requests.get(data.url)
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        photos = []
        for url in soup.find_all('img', class_='b-images__img'):
            photo = requests.get(url.get('src').replace(
                'w100', 'w640').replace('h100', 'h640'))
            photos.append(base64.b64encode(photo.content).decode('utf-8'))

        title = soup.find(
            'span', attrs={'data-qaid': 'product_name'}).text.replace('оптом', '')
        description = []

        table = soup.find_all(id='sizing_table')
        table = table[len(table)-1]

        for tr in table.find_all('tr'):
            line = []
            for td in tr.find_all('td'):
                if td.text != '':
                    line.append(td.text)
            description.append(line)

        description = tabulate(
            description, headers="firstrow", tablefmt="plain").replace('\n', '||')

        def unpack():
            return data.category.split('+')
        category, subcategory = unpack()

        sizes_colors = soup.find(id='sizing_table').find_all('strong')
        sizes = []
        colors = []
        for size_color in sizes_colors:
            temp = size_color.text.split('-')
            try:
                if int(temp[0]):
                    sizes += temp
            except:
                if temp[0] != 'Колір':
                    colors += temp

        amount = 5
        price = int(soup.find(
            class_='b-product-cost__price').text.replace(' ₴', ''))

        post_col.put(PostData(
            photos, title, description, category, subcategory, sizes, colors, amount, price))
    return post_col
