from HTMLCreator import createHTML,deleteHTML
from time import sleep
import WebScrapper
import os
import MoodleCRUD

x = MoodleCRUD.LocalGetSections("8")
print(x.getsections)