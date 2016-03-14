import biggles, config
import string

def plot( a, b=None, **kw ):
	if b is None:
		x = range(1,len(a)+1)
		y = a
	else:
		x = a
		y = b
	p = apply( biggles.FramedPlot, (), kw )
	p.add( biggles.Curve(x, y) )
	p.show()

def read_column( num, filename, atox=float, \
		comment_char=None, return_numpy=None ):
	import string
	if comment_char is None:
		comment_char = config.value('read_column','comment_char')
	if return_numpy is None:
		return_numpy = config.value('read_column','return_numpy')
	x = []
	f = open( filename )
	lines = map( string.strip, f.readlines() )
	f.close()
	lines = filter( None, lines )	# get rid of ''
	for line in lines:
		if line[0] == comment_char[0]:
			continue
		column = string.split( line )
		x.append( column[num] )
	x = map( atox, x )
	if return_numpy:
		import numpy
		return numpy.array( x )
	return x

def read_rows( filename, atox=float, comment_char=None, return_numpy=None ):
	import string
	if comment_char is None:
		comment_char = config.value('read_rows','comment_char')
	if return_numpy is None:
		return_numpy = config.value('read_rows','return_numpy')
	if return_numpy:
		import numpy
	x = []
	f = open( filename )
	lines = map( string.strip, f.readlines() )
	f.close()
	lines = filter( None, lines )	# get rid of blank lines
	for line in lines:
		if line[0] == comment_char[0]:
			continue
		row = map( atox, string.split(line) )
		if return_numpy:
			row = numpy.array( row )
		x.append( row )
	return x

def read_matrix( filename, atox=float, comment_char=None, return_numpy=None ):
	if comment_char is None:
		comment_char = config.value('read_matrix','comment_char')
	if return_numpy is None:
		return_numpy = config.value('read_matrix','return_numpy')
	m = read_rows( filename, atox=atox, comment_char=comment_char, \
		return_numpy=0 )
	if return_numpy:
		import numpy
		return numpy.array( m )
	return m

