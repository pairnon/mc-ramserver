from dotenv import load_dotenv
import os
from server import *
from time import sleep
import subprocess

ALLOC_RAM = os.getenv("ALLOC_RAM")
JAR_FILE = os.getenv("JAR_FILE")
RAM_SERVER_PATH = os.getenv("RAM_SERVER_PATH")

start = "cd {ram_path} && java -Xmx{alloc_ram} -Xms{alloc_ram} -jar {jar_file} nogui".format(alloc_ram=ALLOC_RAM, jar_file=JAR_FILE, ram_path=RAM_SERVER_PATH)

subprocess.Popen(start, shell=True)

sleep(30)

server = Server()

server.exec("/stop")