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

import flask
from flask import request


app = flask.Flask(__name__)

@app.route('/')
def index():
	return flask.render_template('index.html', text="Hello little world!")

@app.route('/test')
	ip = request.args.get('ip')
	port = request.args.get('port')
	if ip == None or port == None:
		return "You must pass both params"
	return "Ip: " + ip + ", port: " + port
