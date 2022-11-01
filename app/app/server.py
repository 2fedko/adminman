import argparse
import threading
from flask import Flask, jsonify, render_template, send_from_directory

from app.utils import config_parser

class Server:

    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.app = Flask(__name__, static_folder='static')
        self.app.register_error_handler(404, self.page_not_found)
        self.app.add_url_rule('/', view_func=self.get_home)
        
    def run_server(self):
        self.server = threading.Thread(target=self.app.run, kwargs={'host' : self.host, 'port': self.port})
        self.server.start()
        return self.server

    def page_not_found(self, err):
        jsonify(error=str(err))
        return render_template('error.html'), 404

    def get_home(self):
        return render_template('index.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, dest='config')

    args = parser.parse_args()

    config = config_parser(args.config)

    server_host = config["SERVER_HOST"]
    server_port = config["SERVER_PORT"]

    server = Server(
        host=server_host,
        port=server_port
    )

    server.run_server()
