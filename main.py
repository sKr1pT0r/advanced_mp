import requests
import sys
import pyfiglet
from bs4 import BeautifulSoup
from colorama import Fore, init

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print('py main.py (Start page)-(End page) (Minecraft version)')
    print('(Example: py main.py 5-10 1.12.2)')
    exit()

not_split_page_range = sys.argv[1].split('-')
start_page = int(not_split_page_range[0])
end_page = int(not_split_page_range[1])

minecraft_version = str(sys.argv[2])

out_file = open('out' + ' ' + str(start_page) + '-' + str(end_page) + '.txt', 'w')

pyfiglet.print_figlet('Advanced-MP', font='big')

for now_page in range(start_page,end_page + 1):
    page = requests.get('http://minecraftrating.ru/servera-' + minecraft_version + '/page/' + str(now_page))
    soup = BeautifulSoup(page.content, 'html.parser')
    
    print('-' * 30)
    print('Page:', now_page)
    print('Find ips:', len(soup.select('kbd')))
    print('-' * 30)
    
    for i in range(0,len(soup.select('kbd'))):
        print(soup.select('kbd')[i].text)
        out_file.write(soup.select('kbd')[i].text + '\n')

out_file.close