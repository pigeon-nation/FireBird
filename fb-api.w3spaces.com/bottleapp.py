#!/usr/bin/env python3

from bottle import (
	route, 
	run, 
	template, 
	response, 
	request
)

import decorator

ops = {
	'plus': '+',
	'minus': '-',
	'multi': '*',
	'div': '/'
}

@decorator.decorator
def retcapture(func, *args, **kwargs):
	out = func(*args, **kwargs)
	print('RETCAPT:', out)
	return out

@route('/<i1>/<oper>/<i2>/')
@retcapture
def hello(i1, oper, i2):
	try:
		int(i1)
	except:
		return
	
	try:
		int(i2)
	except:
		return
	
	xyz = str(eval(i1+ops[oper]+i2))
	return '<h1>' + xyz + '</h1>'

run(host='localhost', port=8888)