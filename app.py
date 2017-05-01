# -*- coding: utf-8 -*-
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
sys.path.insert(0, '/home/martin/public_html/proxies')

import flask
from flask import request
import checkProxy as cp

app = flask.Flask(__name__)
application = app

@app.route('/')
def index():
	return flask.render_template('index.html')

@app.route('/checkProxy')
def checkProxy():
	ip = request.args.get('ip')
	port = request.args.get('port')
	if ip == None or port == None:
		return flask.render_template('boiler.html', text="You must pass both params")
	proxyTest = cp.check_proxy(ip, port)
	return flask.render_template('boiler.html', text=proxyTest)

if __name__ == "__main__":
	app.run(host="0.0.0.0")
