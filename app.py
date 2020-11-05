import re
from collections import namedtuple

from selenium.webdriver import Firefox

if __name__ == '__main__':
    driver = Firefox(executable_path='./drivers/geckodriver', service_log_path='/dev/null')

    hardmob_base_url = 'https://www.hardmob.com.br'

    driver.get(f'{hardmob_base_url}/forums/407-Promocoes/page2')

    threads = driver.find_element_by_class_name('threads').find_elements_by_class_name('threadbit')

    threads_info = []
    ThreadInfo = namedtuple('ThreadInfo', ['title', 'link'])

    keyword = 'cadeira'

    for thread in threads:
        title = thread.find_element_by_class_name('title').text

        if re.search(keyword, title, re.IGNORECASE) is not None:
            link = f'{hardmob_base_url}/{thread.find_element_by_class_name("thread_gotonew").get_attribute("href")}'

            threads_info.append(ThreadInfo(title=title, link=link))

    driver.close()

    for title, link in threads_info:
        print(f'{title} - {link}')
