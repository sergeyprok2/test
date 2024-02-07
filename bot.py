# from playwright.async_api import async_playwright
# from webdriver_manager.chrome import ChromeDriverManager
import cooc

print('Господи, помилуй.')
print('Слава Тебе, Бог наш, Слава Тебе.')
print()
from bs4 import BeautifulSoup as bs
import requests, csv, json, os, sys, time, schedule, random
# from crontab import CronTab
from datetime import datetime
# import pandas as pd
import pprint
import mysql.connector
import textwrap
# import vk_parser
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, Text, BaseFilter,CommandStart
from aiogram.types import Message, ContentType, BotCommand,CallbackQuery
# import os, dotenv
from environs import Env
# from selenium import webdriver
# from selenium.webdriver.common.by import By
from aiogram import Bot, Dispatcher, types,Router
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import Config, load_config
# from aiogram.utils.markdown import text, link,quote_html



from cooc import *
# from playwright.async_api import Playwright, async_playwright
# from playwright_stealth import stealth_async

config1= load_config()
BOT_TOKEN: str = config1.tg_bot.token
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
# API_TOKEN: str = '5959145787:AAHKfsD3UgNhcXuY78EoV0tqE8ZNAn7lK6w'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Стартовать'),
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
        BotCommand(command='/payments',
                   description='Платежи')]

    await bot.set_my_commands(main_menu_commands)


# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Новости')
button_2: KeyboardButton = KeyboardButton(text='Объявления bs4')
button_3: KeyboardButton = KeyboardButton(text='Новости ММА')
button_4: KeyboardButton = KeyboardButton(text='Долгота')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1,button_2,button_3,button_4]],resize_keyboard=True,
                                    one_time_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
# @dp.message(Text(text=['k','K','л','Л']))
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Что хотите посмотреть?',
                         reply_markup=keyboard)



# Список с ID администраторов бота. !!!Замените на ваш!!!
# admin_ids: list[int] = [1942504567]


# Собственный фильтр, проверяющий юзера на админа
# class IsAdmin(BaseFilter):
#     def __init__(self, admin_ids: list[int]) -> None:
#         # В качестве параметра фильтр принимает список с целыми числами
#         self.admin_ids = admin_ids
#
#     async def __call__(self, message: Message) -> bool:
#         return message.from_user.id in self.admin_ids
#
#
# # Этот хэндлер будет срабатывать, если апдейт от админа
# @dp.message(IsAdmin(admin_ids))
# async def answer_if_admins_update(message: Message):
#     print(message.from_user.id)
#     await message.answer(text='Вы админ')



# Этот хэндлер будет срабатывать, при нажатии кнопки Долгота
@dp.message(Text(text='Долгота'))
async def dolgota(message: Message):
    await message.answer(text='Долгота')
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36', }
    with open('dolgota.csv', 'w', encoding='utf-8') as file:
        # m = csv.writer(file)  # ,delimiter=';')
        # m.writerow(['Город', 'Восход', 'Заход', 'Долгота', 'Изменение', 'Сайт', ''])
        d = ['Прокопьевск', 'Удачный    ', 'Норильск   ', 'Воркута    ', '', '', '', '', '', '', '', '', '', '', '', '',
             '',
             '']
        kl='https://voshod-solnca.ru/sun/прокопьевск'
        sait = ['прокопьевск',
                'мурманск',
                'оленегорск',
                'удачный',
                'норильск',
                'воркута',
                'москва',
                'сочи',
                'певек',
                'пхукет',
                'дровяной',
                'мирный_(республика_саха_(якутия))']
        b = []
        n = []
        veter = []
        data = []
        p = 0
        await message.answer(text='1')
        for y in sait:
            response = requests.get(url=f'https://voshod-solnca.ru/sun/{y}', headers=headers)
            response.encoding = 'utf=8'
            soup = bs(response.text, 'html.parser')
            # h=[i.text for i in soup.find('span', class_='unit unit_temperature_c').find_all('div', class_='maxt')]
            gorod = soup.find('div', id='map-content-search').find('option').text
            vochod = soup.find('div', {'data-name': 'sunrise'}).text
            zahod = soup.find('div', {'data-name': 'sunset'}).text
            dolgota = soup.find('div', {'data-name': 'daytime'}).find('span').text
            ismen = soup.find('div', class_='table-scroll').find_all('td')[5].text
            # m.writerow([gorod, vochod, zahod, dolgota, ismen, sait[p]])
            p+=1
            hg=[vochod,zahod,dolgota,ismen,gorod]
            await message.answer(text='   '.join(hg))
        # читаем файл.csv и создаем таблицу
        # chat_id = message.chat.id
        #
        # df = pd.read_csv('dolgota.csv')
        # await message.answer(text=df)
        # # создаем сообщение с таблицей
        # table_message = ''
        # for row in df.itertuples():
        #     table_message += ' | '.join(str(val) for val in row[1:]) + '\n'
        # # отправляем сообщение с таблицей
        #     await message.answer(text=table_message)
        # await bot.send_message(chat_id, table_message)

# Функция для подключения к базе данных
def connect(a,b,c,d):
    cnp = mysql.connector.connect(
        host=a,
        user=b,
        passwd=c,
        database=d,
    )
    return cnp
# cnx = connect(cooc.host1, cooc.user1, cooc.passwd1,cooc.database1)
r=[]

# @dp.message(Text(text=['з', 'З', 'p','P']))
# async def zakrep(message: Message):
#     await message.answer(text=r)

# Этот хэндлер будет срабатывать, при нажатии кнопки bs4
@dp.message(Text(text='Объявления bs4'))
async def vk_bs4(message: Message):
    await message.answer(text='Объявления')
    # Получение текущей даты и времени и вывод на экран
    k = datetime.now().strftime('%d.%m.%y  %H:%M:%S')
    print(k)
    await message.answer(text=k)
    # Подключение к базе данных
    cnx = connect(cooc.host1, cooc.user1, cooc.passwd1, cooc.database1)
    cursor = cnx.cursor()
    # Выполнение запроса и получение результатов
    cursor.execute("SELECT text, date, links FROM vk where state='новое' order by id DESC")
    gf = cursor.fetchall()
    ok=len(gf)
    # Если нет новых объявлений, выводится сообщение об этом
    if len(gf) == 0:
        await message.answer(text='Пока новых объявлений нет')
    # Вывод всех новых объявлений
    for i in gf:
        await message.answer(text=i[0] + '\n' + '<a href="{}">ссылка</a>'.format(i[2]) + '\n' + i[1].strftime("%H:%M"),parse_mode='HTML')
    # Обновление состояния объявлений на "старое"
    cursor.execute("UPDATE vk SET state ='старое' where state LIKE 'новое'")
    cnx.commit()

    # Закрытие соединения с базой данных
    cursor.close()
    cnx.close()


# @router.message()
# async def send_answer(message: Message):
#     await message.answer(text=f"Я все о тебе знаю \n"
#                               f"Твой user_id = {message.from_user.id}")

# Этот хэндлер будет срабатывать, если апдейт придет кнопки  'Объявления sel' для парсера вк на селениуме

@dp.message(Text(text='Новости ММА'))
async def mma(message: Message):
    await message.answer(text='Новости ММА')
    # Получение текущей даты и времени и вывод на экран
    k = datetime.now().strftime('%d.%m.%y  %H:%M:%S')
    print(k)
    await message.answer(text=k)
    # Подключение к базе данных
    cnx = connect(cooc.host1, cooc.user1, cooc.passwd1, cooc.database1)
    cursor = cnx.cursor()
    # Выполнение запроса и получение результатов
    cursor.execute("SELECT text, date, links FROM mma where state='новое' order by id DESC")
    gf = cursor.fetchall()
    ok = len(gf)
    # Если нет новых объявлений, выводится сообщение об этом
    if len(gf) == 0:
        await message.answer(text='Пока новых объявлений нет')
    # Вывод всех новых новостей
    for i in gf:
        dft=len(i[2])
        if 'н' not in i[2]:
            # ht=i[0]
            # dr=i[1].strftime("%H:%M")
            # bg=f'<a href={i[2]}>ссылка</a>'
            await message.answer(text=f"{i[0]}\n<a href='{i[2]}'>ссылка</a>\n{i[1].strftime('%H:%M')}", parse_mode='HTML')
        else:
            links2 = i[2].split("н")  # Разделение строки на ссылки
            formatted_links = ''  # Переменная для хранения объединенных ссылок

            for link3 in links2:
                formatted_links += f'<a href="{link3}">ссылка</a>\n'  # Объединение ссылок, добавление тега <a> и перевода строки

            await message.answer(text=i[0] + '\n' + formatted_links + i[1].strftime("%H:%M"), parse_mode='HTML')
            # links = i[2].split("\n")  # Разделение строки на ссылки
            #
            # for link in links:
            #     await message.answer_photo(link)
            #
            # text = f'{i[0]}\n{i[1].strftime("%H:%M")}\n{i[2]}'  # Получение полного текста сообщения
            # await message.answer(text=text, parse_mode='HTML')

            # await message.answer(text=i[0] + '\n' + f'<a href=https://vk.com/photo-30684458_459458805?list=wall-30684458_18669371>ссылка</a>' + '\n' + f'<a href=https://vk.com/photo-30684458_459458804?list=wall-30684458_18669371>ссылка</a>' + '\n' + i[1].strftime("%H:%M"),
            #                      parse_mode='HTML')
    # Обновление состояния новостей на "старое"
    cursor.execute("UPDATE mma SET state ='старое' where state LIKE 'новое'")
    cnx.commit()

    # Закрытие соединения с базой данных
    cursor.close()
    cnx.close()

# Этот хэндлер будет срабатывать, если апдейт не от админа
v=[]   #  список ссылок новостей

@dp.message(Text(text='1'))
async def novost_1(message: Message):
    await message.answer(text=v[0])

@dp.message(Text(text='2'))
async def novost_2(message: Message):
    await message.answer(text=v[1])

@dp.message(Text(text='3'))
async def novost_3(message: Message):
    await message.answer(text=v[2])

@dp.message(Text(text='4'))
async def novost_4(message: Message):
    await message.answer(text=v[3])

@dp.message(Text(text='5'))
async def novost_5(message: Message):
    await message.answer(text=v[4])

@dp.message(Text(text='6'))
async def novost_1(message: Message):
    await message.answer(text=v[5])

@dp.message(Text(text='7'))
async def novost_2(message: Message):
    await message.answer(text=v[6])

@dp.message(Text(text='8'))
async def novost_3(message: Message):
    await message.answer(text=v[7])

@dp.message(Text(text='9'))
async def novost_4(message: Message):
    await message.answer(text=v[8])

@dp.message(Text(text='10'))
async def novost_5(message: Message):
    await message.answer(text=v[9])


@dp.message(Text(text='Новости1'))
async def novosti_playwright(message: Message):
    await message.answer(text='Новости')
    k = datetime.now().strftime('%d.%m.%y  %H:%M:%S')
    print(k)
    # print(message.from_user.id)
    await message.answer(text=k)
    # proxy_server = 'http://195.216.135.182:8000'

    # print(message.from_user.id)
    # try:
    # proxy_host = '195.216.135.182'
    # proxy_port = '8000'
    # username = 'XvQx6z'
    # password = '8k8KKM'

    proxy_host = '168.81.59.128'
    proxy_port = '8000'
    username = 'RLdrq9'
    password = 'haRzKV'


    # proxy_server = {
    #     'server': f"http://{proxy_host}:{proxy_port}",
    #     'username': username,
    #     'password': password,
    # }
    # async with async_playwright() as pw:
    #     rt=0
    #     y=cooc
    #     # context = await browser.new_context(cookies=cookie, proxy=proxy_server)
    #
    #     # proxy_server = { "server": f"http://{username}:{password}@{proxy_host}:{proxy_port}" }
    #
    #     proxy_server = {'server': f"http://{proxy_host}:{proxy_port}", 'username': username, 'password': password}
    #     await message.answer(text='выполняет строку browser = await pw.chromium.launch(headless=True)')
    #     # browser = await pw.chromium.launch(headless=False,proxy=proxy_server)
    #     browser = await pw.chromium.launch(headless=True)
    #     await message.answer(text='выполняет строку context = await browser.new_context()')
    #     context = await browser.new_context(proxy=proxy_server)
    #     await message.answer(text='выполняет строку page = await context.new_page()')
    #     page = await context.new_page()
    #     await context.add_cookies(y)
    #
    #
    #     # await stealth_async(page)
    #     await message.answer(text='заходит на страницу сайта')
    #     # await message.answer(text='начался time.sleep')
    #     # time.sleep(100)
    #     # await message.answer(text='закончился time.sleep')
    #     # response = await page.goto("https://dzen.ru/?clid=1946579&win=90&yredirect=true&utm_referer=sso.dzen.ru")
    #     # response = await page.goto("https://dzen.ru/?yredirect=true")
    #     # await page.screenshot(path='/root/tike/botserver/screenshots/screenshot.png')
    #     response = await page.goto("http://dzen.ru")
    #     # await page.screenshot(path='/root/tike/botserver/screenshots/screenshot1.png')
    #     # response = await page.goto("https://stepik.org/lesson/716118/step/4?unit=716910")
    #     # response = await page.goto("https://google.com")
    #     if response.status == 200:
    #         await message.answer(text='200')
    #         # await page.screenshot(path='/root/tike/botserver/screenshots/screenshot2.png')
    #
    #     else:
    #         await message.answer(text='не 200')
    #     await message.answer(text="выполняет строку checkbox = page.locator('.card-news__stories-Bu')")
    #     checkbox = page.locator('.card-news__stories-Bu')
    #     await message.answer(text='выполняет строку checkbox_texts = await checkbox.all_inner_texts()')
    #     checkbox_texts = await checkbox.all_inner_texts()
    #     # checkbox_texts = [await kl.get_attribute('aria-label') for kl in (await checkbox.locator('span').all())]
    #     if checkbox_texts:
    #         await message.answer(text='выполняет строку await message.answer(text=checkbox_texts[0])')
    #         await message.answer(text=checkbox_texts[0])
    #     else:
    #         await message.answer(text='checkbox_texts пустой')
    #     v.clear()  # делает список пустым
    #     print()
    #     # await message.answer(text=checkbox_texts[0])
    #     n = [await k.get_attribute('href') for k in (await checkbox.locator('a').all())]
    #
    #     await message.answer(text="выполняет строку d=checkbox_texts[0].split('\n')")
    #     d=checkbox_texts[0].split('\n')
    #     await message.answer(text='выполняет цикл ')
    #     for i,y in zip(d,n):
    #         await message.answer(text=i)
    #         v.append(y)

@dp.message(Text(text='Новости'))
async def novosti_requests(message: Message):
    await message.answer(text='Новости')
    k = datetime.now().strftime('%d.%m.%y  %H:%M:%S')
    print(k)
    # print(message.from_user.id)
    await message.answer(text=k)
    # proxy_server = 'http://195.216.135.182:8000'

    # print(message.from_user.id)
    # try:
    # proxy_host = '195.216.135.182'
    # proxy_port = '8000'
    # username = 'XvQx6z'
    # password = '8k8KKM'

    proxy_host = '168.81.59.128'
    proxy_port = '8000'
    username = 'RLdrq9'
    password = 'haRzKV'


    # proxy_server = {
    #     'server': f"http://{proxy_host}:{proxy_port}",
    #     'username': username,
    #     'password': password,
    # }

    rt=0
    # y=cookies
    # context = await browser.new_context(cookies=cookie, proxy=proxy_server)

    # proxy_server = { "server": f"http://{username}:{password}@{proxy_host}:{proxy_port}" }

    proxy_server = {'server': f"http://{proxy_host}:{proxy_port}", 'username': username, 'password': password}
    cookies = cooc.cookies_ya

    headers = cooc.headers_ya

    response = requests.get('https://m.dzen.ru/', cookies=cookies, headers=headers)
    # response = requests.get(url="https://dzen.ru", headers=headers,cookies=y)
    # print(response.text)
    if response.status_code == 200:
        await message.answer(text='200')
        response.encoding = 'utf-8'
        soup = bs(response.text, 'html.parser')
        g=soup.find_all('ul', class_="card-news__stories-Bu")
        t=soup.find('ul', class_="card-news__stories-Bu")
        v.clear()
        # print(g)


        for i in g:
            # v.append([k['href'] for k in i.find_all('a')])
            for n in i.find_all('li'):
                v.append(n.find('a')['href'])
                await message.answer(text=n.text)
        print()
        print()

        # await page.screenshot(path='/root/tike/botserver/screenshots/screenshot2.png')

    else:
        await message.answer(text='не 200')

# @dp.message(Text(text='Новости sel'))
# async def novosti_selenium(message: Message):
#     await message.answer(text='Новости')
#     k = datetime.now().strftime('%d.%m.%y  %H:%M:%S')
#     print(k)
#     print(message.from_user.id)
#     await message.answer(text=k)
#     print(message.from_user.id)
#     # try:
#     options_chrome = webdriver.ChromeOptions()
#     # options_chrome.add_extension('coordinates.crx')
#     # zzz=options=options_chrome
#
#     options_chrome.add_argument('--headless=chrome')
#     with webdriver.Chrome(options=options_chrome) as browser:
#         await message.answer(text='1')
#         browser.get('https://dzen.ru/?clid=1946579&win=90&yredirect=true&utm_referer=sso.dzen.ru')
#         await message.answer(text='2')
#         checkbox = browser.find_element(By.CLASS_NAME, 'card-news__stories-Bu')   #
#
#         v.clear()   #  делает список пустым
#         g = [i.strip() for i in checkbox.text.split('\n')]   #  список заголовков новостей
#         n = [k.get_attribute('href') for k in checkbox.find_elements(By.TAG_NAME, 'a')]   #  список ссылок новостей
#         for y, u in zip(g, n):
#             # print(y, u)
#             v.append(u)   #  добавляет ссылки в список
#             # await message.answer(text=u)
#             await message.answer(text=y)
    # except:
    #     await message.answer(text='Что то пошло не так')
    #     print('Что то пошло не так')





if __name__ == '__main__':
    dp.startup.register(set_main_menu)
    dp.run_polling(bot)