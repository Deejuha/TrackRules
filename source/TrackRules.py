from pathlib import Path
from time import sleep
from urllib.parse import unquote
from urllib.request import urlretrieve
from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By


def download_file(link: str) -> None:
    """
    Requests a file from website, stores to memory.

    """
    out_dir = Path("./out")
    general_dir_name = Path(out_dir, "CONTENTS, RULES OF INTERPRETATION, DEFINITIONS")
    book_a_dir_name = Path(out_dir, "BOOK A: THE CONSTITUTION")
    book_b_dir_name = Path(out_dir, "BOOK B: ORGANISATION")
    book_c_dir_name = Path(out_dir, "BOOK C: COMPETITION")
    book_d_dir_name = Path(out_dir, "BOOK D: INTEGRITY & DISCIPLINARY")
    filename = unquote(link.split("=")[-1]) + ".pdf"
    if search(r"^A[0-9]{1} - +", filename):
        book_dir = book_a_dir_name
    elif search(r"^B[0-9]{1}.[0-9]{1}.+", filename):
        book_dir = book_b_dir_name
    elif search(r"^C[0-9]{1}.[0-9]{1}.+", filename):
        book_dir = book_c_dir_name
    elif search(r"^D[0-9]{1}.[0-9]{1}.+", filename):
        book_dir = book_d_dir_name
    else:
        book_dir = general_dir_name
    book_dir.mkdir(parents=True, exist_ok=True)
    urlretrieve(link, Path(book_dir, filename))


driver = webdriver.Chrome()
driver.get(r"https://www.worldathletics.org/about-iaaf/documents/book-of-rules")

sleep(3)  # website has to load TODO make it wait for some element
xpath = "//a[@href]"
all_links_in_website = driver.find_elements(by=By.XPATH, value=xpath)
for link in set(all_links_in_website):
    if (ahref := link.get_attribute("href")).startswith(
        "https://www.worldathletics.org/download/download"
    ):
        download_file(ahref)
