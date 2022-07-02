import json
from bottle import Bottle, run, route, request

@route('/')
def index():
	return 'Hello Someone looking at this'

@route('/crossproduct', method="POST")
def crossproduct():

	#for l in request.body:
	#	print(l)
	#print(request.body)
	data = request.json
	new_vec = []
	
	v = data['v']
	u = data['u']
	
	new_vec.append((u[1]*v[2]) - (u[2]*v[1]))
	new_vec.append((u[2]*v[0]) - (u[0]*v[2]))
	new_vec.append((u[0]*v[1]) - (u[1]*v[0]))
	
	data = json.dumps(new_vec)
	
	return data


run(host='localhost', port=9001)
