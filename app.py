import re
from argparse import ArgumentParser
from collections import namedtuple
from datetime import datetime

from selenium.webdriver import Firefox


def parse_arguments():
    parser = ArgumentParser()

    parser.add_argument('-w', '--word', help='the specific keyword to search up to', required=True)

    return parser.parse_args()


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


def is_thread_date_more_than_five_days_old(thread_date: str) -> bool:
    """
    Compare the current date with the thread date to check if the thread date is more than five days old
    @param thread_date: the date when the thread was posted
    @returns if the thread more than five days older
    """
    today = datetime.now()

    try:
        day, month, year, *_ = thread_date.split('-')

    except ValueError:
        return False

    else:
        year = year.split(',')[0]

    thread_date = datetime(year=int(year), month=int(month), day=int(day))

    difference_in_days = (today - thread_date).days

    return difference_in_days > 5


if __name__ == '__main__':
    args = parse_arguments()
    keyword = args.word

    driver = Firefox(executable_path='./drivers/geckodriver', service_log_path='/dev/null')
    hardmob_base_url = 'https://www.hardmob.com.br'

    page_number = ''
    should_continue_searching = True

    threads_info = []
    ThreadInfo = namedtuple('ThreadInfo', ['title', 'link'])

    while should_continue_searching:
        driver.get(f'{hardmob_base_url}/forums/407-Promocoes/{page_number}')

        threads = driver.find_element_by_class_name('threads').find_elements_by_class_name('threadbit')

        for thread in threads:
            post_info = thread.find_element_by_class_name('threadlastpost')
            post_date = post_info.find_elements_by_tag_name('dd')[1]

            if is_thread_date_more_than_five_days_old(post_date.text):
                should_continue_searching = False
                break

            title_tag = thread.find_element_by_class_name('title')
            title = title_tag.text

            if re.search(keyword, title, re.IGNORECASE) is not None:
                link = title_tag.get_attribute("href")

                threads_info.append(ThreadInfo(title=title, link=link))

        page_number = chose_new_page_number(current_page_number=page_number)

    driver.close()

    for title, link in threads_info:
        print(f'{title} - {link}')
