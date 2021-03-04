from HTMLCreator import createHTML,deleteHTML,createDir,isExisting
from time import sleep
import WebScrapper
import os

title, html = WebScrapper.getTitleAndHTML("https://mikhail-cct.github.io/ooapp2/wk4/#/")
createHTML(1, html)