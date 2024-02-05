import mysql.connector
print('Господи, помилуй.')
print('Слава Тебе, Бог наш, Слава Тебе.')
print()
from bs4 import BeautifulSoup as bs
import requests, csv, json, os, sys, time, schedule, random
# from crontab import CronTab
from datetime import datetime
import cooc

# Press F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
print(0)
def connect(a,b,c,d):
    print(0,5)
    cnp = mysql.connector.connect(
        host=a,
        user=b,
        passwd=c,
        database=d
    )
    return cnp
cnx = connect(cooc.host1, cooc.user1, cooc.passwd1,cooc.database1)
print(1)
cursor = cnx.cursor()
# Проверка существования таблицы 'vk'
cursor.execute("SHOW TABLES LIKE 'vk'")
table_exists = cursor.fetchone()
if table_exists:
    cursor.execute("SELECT MAX(id) FROM vk")
    lk = cursor.fetchone()[0]
    if lk is None or int(lk) > 50:
        cursor.execute('DROP TABLE vk')
        # Создание таблицы 'vk'
        cursor.execute(f"""CREATE TABLE vk (
                id int unsigned NOT NULL primary key,
                text text NOT NULL DEFAULT 'r',
                state enum('новое', 'старое') NOT NULL,
                date DATETIME NOT NULL DEFAULT (CURRENT_TIMESTAMP + INTERVAL 7 HOUR),
                links text NOT NULL
                )""")

elif not table_exists:
    # Создание таблицы 'vk'
    cursor.execute(f"""CREATE TABLE vk (
        id int unsigned NOT NULL primary key,
        text text,
        state enum('новое', 'старое') NOT NULL,
        date DATETIME NOT NULL DEFAULT (CURRENT_TIMESTAMP + INTERVAL 7 HOUR),
        links VARCHAR(255) NOT NULL
        )""")
# cursor.execute(f"INSERT INTO users2 (id, first_name, last_name, birthday, age, active) "
#                f"VALUES (1, 'Дмитрий', 'Иванов', '1986-02-18', 31, True)")
cnx.commit()

cnx.close()
cookies = cooc.cookies_bs4

headers = cooc.headers_bs4

params = {'scroll': 'down'}

#  Функция записи html в файл
def write():
    response = requests.get('https://m.vk.com/jobprk?offset=1&own=1', cookies=cookies, headers=headers)
    response.encoding = 'utf-8'
    # print(response.text)
    soup = bs(response.text, 'html.parser')
    print('soup')
    with open('file_vk.html', 'w') as file:
        # Записываем текст в файл
        file.write(str(soup))
    return soup

#  Функция чтения из файла
def read ():
    print(6)
    with open('file_vk.html', encoding='utf-8') as file:
        # Записываем текст в файл
        content = file.read()

    soup = bs(content, 'html.parser')
    return soup
print(7)
def parse():
    print(8)
    response = requests.get('https://m.vk.com/jobprk?offset=1&own=1', cookies=cookies, headers=headers)
    response.encoding = 'utf-8'
    # print(response.text)
    soup = bs(response.text, 'html.parser')
    print('soup')
    return soup


def print_hi():
    k = datetime.now().strftime('%d.%m.%y  %H:%M:%S')
    print(k)
    # soup = bs(content, 'html.parser')
    # soup = write()  # Сохраняем HTML-контент в файл перед его парсингом
    soup = parse()  # Выполняем программу и парсим его
    # soup = read()  # Читаем HTML-контент из файла и парсим его


    # pretty_soup = soup.prettify()
    # Вывод хорошо читаемого объекта soup
    # print(pretty_soup)
    r34=soup.find_all('div', class_="wall_item")
    fg=soup.find_all('div', class_="wall_item post--withRedesign")
    # print(soup.find('div',id="posts_container"))
    # print(soup.find_all('div', class_="pi_text"))
    # d = [i.text for i in soup.find_all('div', class_="pi_text")]
    d = []
    link = []
    r = []
    hj = 0
    for u in soup.find_all('div', class_="wall_item post--withRedesign"):
        o9=u.find('div', class_="wi_body").text
        o=len(u.find('div', class_="wi_body").text)
        # o8=u.find('div', class_="pi_text").text
        kj=u.find('span', class_="wall_text")
        if u.find('span', class_="PostHeader__contentExplain") != None:
            d.append('объявление закреплено')
            if u.find('div', class_="pi_text") == None:
                if u.find('img', class_='MediaGrid__imageSingle') != None:
                    print('картинка')
                    r.append(u.find('img', class_='MediaGrid__imageSingle')['src'])
                    continue
                elif u.find('div', class_='pi_medias audios_list medias_audios_list'):
                    print('опрос')
                    hy = u.find('div', class_='pi_medias audios_list medias_audios_list').text
                    continue
                print('фото')
                r.append(u.find('img')['src'])
                continue
            r.append(u.find('div', class_="pi_text").text)
            continue
        elif u.find('div', class_="wi_body wi_no_text"):  #  без текста
            if u.find('img', class_='PhotoPrimaryAttachment__imageElement'):   #  только фото
                print('фото')
                link.append(u.find('img', class_='PhotoPrimaryAttachment__imageElement')['src'])
                d.append('gh')
            elif u.find('div', class_="poster__text"):  #  с картинки можно текст взять
                d.append(u.find('div', class_="poster__text").text)
                link.append('')

            elif u.find('a', class_="thumb_link"):  # только видео
                link.append('https://vk.com' + u.find('a', class_="thumb_link")['href'])
                d.append('gh')
                print('видео')
        else:
            if u.find('a', class_="thumb_link"):
                d.append(u.find('div', class_="pi_text").text)
                link.append('https://vk.com' + u.find('a', class_="thumb_link")['href'])
                # d.append(u.find('div', class_="pi_text").text)
                print('видео')
            elif u.find('img', class_="PhotoPrimaryAttachment__imageElement"):
                d.append(u.find('div', class_="pi_text").text)
                link.append(u.find('img', class_="PhotoPrimaryAttachment__imageElement")['src'])
                # d.append(u.find('div', class_="pi_text").text)
                print('фото')
            elif u.find('div', class_="MediaGridContainerMvk--post MediaGridContainerMvk--postFullWidth"):
                d.append(u.find('div', class_="pi_text").text + '\n')  # Добавляем текст из pi_text в список d

                # Итерируемся по всем элементам <a> и получаем значение атрибута href для каждого элемента
                for linkk in u.find('div', class_="MediaGridContainerMvk--post MediaGridContainerMvk--postFullWidth").find_all('a'):
                    link.append('к')
                    link[hj] += '\n' + 'https://vk.com' + linkk['href']  # Добавляем значение href в список d
                    link[hj].replace('к', '')
                print('несколько фото')
            elif not u.find('div', class_="pi_medias thumbs_list thumbs_list1 audios_list medias_audios_list"):
                d.append(u.find('div', class_="pi_text").text)
                link.append('')
                print('только текст')

        # if u.find('div', class_="pi_text") == None:
        #     if u.find('img', class_='PhotoPrimaryAttachment__imageElement'):
        #         if u.find('div', id="image-overlay") != None:
        #             d.append(u.find('div', class_="poster__text").text)
        #             link.append(u.find('img', class_='PhotoPrimaryAttachment__imageElement')['src'])
        #             continue
        #         print('фото')
        #         link.append(u.find('img', class_='PhotoPrimaryAttachment__imageElement')['src'])
        #         d.append('')
        #     elif u.find('div', class_="poster__text") != None:
        #         d.append(u.find('div', class_="poster__text").text)
        #         link.append('')
        #
        #     elif u.find('a', class_="thumb_link"):
        #         link.append('https://vk.com' + u.find('a', class_="thumb_link")['href'])
        #         d.append('')
        #         print('видео')
        # else:
        #     if u.find('a', class_="thumb_link"):
        #         d.append(u.find('div', class_="pi_text").text)
        #         link.append('https://vk.com' + u.find('a', class_="thumb_link")['href'])
        #         # d.append(u.find('div', class_="pi_text").text)
        #         print('видео')
        #     elif u.find('img', class_="PhotoPrimaryAttachment__imageElement"):
        #         d.append(u.find('div', class_="pi_text").text)
        #         link.append(u.find('img', class_="PhotoPrimaryAttachment__imageElement")['src'])
        #         # d.append(u.find('div', class_="pi_text").text)
        #         print('фото')
        #     elif u.find('div', class_="MediaGridContainerMvk--post MediaGridContainerMvk--postFullWidth"):
        #         d.append(u.find('div', class_="pi_text").text + '\n')  # Добавляем текст из pi_text в список d
        #
        #         # Итерируемся по всем элементам <a> и получаем значение атрибута href для каждого элемента
        #         for linkk in u.find('div',
        #                             class_="MediaGridContainerMvk--post MediaGridContainerMvk--postFullWidth").find_all(
        #                 'a'):
        #             link.append('к')
        #             link[hj] += '\n' + 'https://vk.com' + linkk['href']  # Добавляем значение href в список d
        #             link[hj].replace('к', '')
        #         print('несколько фото')
        #     elif not u.find('div', class_="pi_medias thumbs_list thumbs_list1 audios_list medias_audios_list"):
        #         d.append(u.find('div', class_="pi_text").text)
        #         link.append('')
        #         print('только текст')

        hj += 1
    if len(d) == 0:
        print('Вас заблокировали')
    cnx=connect(cooc.host1, cooc.user1, cooc.passwd1,cooc.database1)
    cursor = cnx.cursor()
    # Выполните SQL-запрос для подсчета строк в таблице
    cursor.execute("SELECT COUNT(*) FROM vk")

    # Получите результат запроса
    daf = cursor.fetchone()[0]
    if daf>50:
        # Выполните SQL-запрос для удаления строк из таблицы
        cursor.execute("DELETE FROM vk order by id limit 25")

        # Подтвердите удаление строк
        cnx.commit()

        # Проверьте, сколько строк было удалено
        print(f"Удалено строк: {cursor.rowcount}")

    cursor.execute("SELECT MAX(id) FROM vk")
    lk = cursor.fetchone()[0]
    if lk is not None:
        n = lk + 1
    else:
        n = 1
    print(f'{len(d)} + lplk')
    for j, link1 in zip(d, link):
        try:
            if 'Показать ещё' in j:
                j = j.replace('Показать ещё', ' ')
            # print(len(j),j)
            # cursor = cnx.cursor()
            cursor.execute("SELECT * FROM vk WHERE text LIKE %s", (j,))
            result = cursor.fetchone()

            if result and j != 'gh':
                continue


            cursor.execute(f"INSERT INTO vk (id, text, state, links)"
                           f"VALUES (%s, %s, %s, %s)", (n, j, 'новое', link1))
            cnx.commit()
            n += 1
        except Exception as err:
            print(err)
            continue

    cursor.close()
    cnx.close()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

    # Расписание выполнения задачи каждые 30 минут
    schedule.every(30).minutes.do(print_hi)

    while True:
        schedule.run_pending()
        time.sleep(1)