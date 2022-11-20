import sys
import time
from flask import Flask, render_template, redirect, url_for
from threading import Thread
import signal

from matrix.Matrix import Matrix

from apps import apps

PIX_SIZE = 20
WIDTH = 28
HEIGHT = 22

matrix = Matrix(WIDTH, HEIGHT, PIX_SIZE)

current_app = None


def switch_app(app):
    global current_app
    if app and isinstance(current_app, app):
        return
    if current_app:
        current_app.exit()
        del current_app
    if app:
        current_app = app(matrix)
    else:
        current_app = None


web = Flask(__name__)


@web.route('/')
def index():
    return render_template('index.html', apps=apps)


@web.route('/off')
def off():
    switch_app(None)
    return redirect(url_for('index'))


@web.route('/switch/<int:app_id>')
def switch_route(app_id):
    switch_app(apps[app_id])
    return redirect(url_for('index'))


web_thread = Thread(target=lambda: web.run(host='0.0.0.0', port=80))
web_thread.daemon = True
web_thread.start()


def terminate():
    if current_app:
        current_app.exit()
    global matrix
    del matrix
    sys.exit(0)


signal.signal(signal.SIGTERM, terminate)

while True:
    if current_app:
        current_app.update(0)
    else:
        matrix.fill((1, 1, 1))
    matrix.run()
