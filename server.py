from dotenv import load_dotenv
import os
import mcrcon

class Server:

    load_dotenv()

    IP = os.getenv("IP")
    RCON_PASS = os.getenv("RCON_PASS")
    RCON_PORT = os.getenv("RCON_PORT")

    server_ip = IP
    rcon_password = RCON_PASS
    rcon_port = int(RCON_PORT)

    tls_mode = 0
    timeout = 20

    rcon = mcrcon.MCRcon(server_ip, rcon_password, rcon_port, tls_mode, timeout)

    def __init__(self):
        pass

    def exec(self, command):
        if(command[0:1:] != "/"):
            print("ERROR: command must start with '/'")
            return
        self.rcon.connect()
        response = self.rcon.command(command[1::])
        print(response) # Print the server's response

    def exit(self):
        self.rcon.disconnect()