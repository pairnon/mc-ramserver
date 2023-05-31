from dotenv import load_dotenv
import os
from server import *
from time import sleep
import subprocess

ALLOC_RAM = os.getenv("ALLOC_RAM")
JAR_FILE = os.getenv("JAR_FILE")
SERVER_FOLDER_PATH = os.getenv("SERVER_FOLDER_PATH")

subprocess.Popen("cd {path}".format(path = SERVER_FOLDER_PATH), shell=True)

start = "java -Xmx{alloc_ram} -Xms{alloc_ram} -jar {jar_file} nogui".format(alloc_ram=ALLOC_RAM, jar_file=JAR_FILE)

print(start)

subprocess.Popen(start, shell=True)