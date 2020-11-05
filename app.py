import re
from collections import namedtuple

from selenium.webdriver import Firefox


def chose_new_page_number(current_page_number: str) -> str:
    """
    Chose the new page number given the current one
    @param current_page_number: the current page number
    @returns the new page number
    """
    if not current_page_number:
        return 'page2'

    integer_page_number = int(current_page_number[-1])

    return f'page{integer_page_number + 1}'


if __name__ == '__main__':
    driver = Firefox(executable_path='./drivers/geckodriver', service_log_path='/dev/null')
    hardmob_base_url = 'https://www.hardmob.com.br'

    page_number = ''

    threads_info = []
    ThreadInfo = namedtuple('ThreadInfo', ['title', 'link'])

    keyword = 'cadeira'

    while page_number != 'page4':
        driver.get(f'{hardmob_base_url}/forums/407-Promocoes/{page_number}')

        threads = driver.find_element_by_class_name('threads').find_elements_by_class_name('threadbit')

        for thread in threads:
            title_tag = thread.find_element_by_class_name('title')
            title = title_tag.text

            if re.search(keyword, title, re.IGNORECASE) is not None:
                link = title_tag.get_attribute("href")

                threads_info.append(ThreadInfo(title=title, link=link))

        page_number = chose_new_page_number(current_page_number=page_number)

    driver.close()

    for title, link in threads_info:
        print(f'{title} - {link}')
