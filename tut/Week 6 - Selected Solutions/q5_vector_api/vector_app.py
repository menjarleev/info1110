#from bottle import run, request, post
#import json

#@post('/crossproduct')
#def cproduct():
#    j_obj = json.loads(request.body.read())
#    a = j_obj['u']
#    b = j_obj['b']
#    c = [0]*3
#    c[0] = ((a[1]*b[2]) - (a[2]*b[1]))
#    c[1] = ((a[2]*b[0]) - (a[0]*b[2]))
#    c[2] = ((a[0]*b[1]) - (a[1]*b[0]))
#    response.content_type = 'application/json'
#    return json.dumps({'result' : c })


#@post('/dotproduct')
#def dproduct():
#    j_obj = json.loads(request.body.read())
#    a = j_obj['u']
#    b = j_obj['b']
#    d = json.dumps({ 'result' : (a[0]*b[0]) + (a[1]*b[1]) + (a[2]*b[2]) })
#    response.content_type = 'application/json'
#    return d

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
