__version__ = '1.6.6'

from biggles import		 \
	Circle			,\
	Circles			,\
	ColoredPoint		,\
	ColoredPoints		,\
	Curve			,\
	DataArc			,\
	DataBox			,\
	DataInset		,\
	DataLabel		,\
	DataLine		,\
	Density			,\
	Ellipse			,\
	Ellipses		,\
	ErrorBarsX		,\
	ErrorBarsY		,\
	FillAbove		,\
	FillBelow		,\
	FillBetween		,\
	FramedArray		,\
	FramedPlot		,\
	Geodesic		,\
	Histogram		,\
        Labels                  ,\
	LineX			,\
	LineY			,\
	LowerLimits		,\
	OldCustomFramedPlot	,\
	OldKey			,\
	Plot			,\
	PlotArc			,\
	PlotBox			,\
	PlotInset		,\
	PlotKey			,\
	PlotLabel		,\
	PlotLine		,\
	Point			,\
	Points			,\
	Slope			,\
	SymmetricErrorBarsX	,\
	SymmetricErrorBarsY	,\
	Table			,\
	Text			,\
	UpperLimits		,\
	multipage

from config import		 \
	configure

from contour import		 \
	Contour			,\
	Contours

from func import		 \
	plot			,\
	read_column		,\
	read_matrix		,\
	read_rows

from hammer import		 \
	HammerAitoffPlot

# aliases
Arc = DataArc
Box = DataBox
Inset = PlotInset
Label = DataLabel
Line = DataLine
SymmetricXErrorBars = SymmetricErrorBarsX
SymmetricYErrorBars = SymmetricErrorBarsY
XErrorBars = ErrorBarsX
YErrorBars = ErrorBarsY

class _deprecated:

	def __init__( self, obj, old, new, harrass=1 ):
		self.obj = obj
		self.old = old
		self.new = new
		self.harrass = harrass

	def __call__( self, *args, **kw ):
		import sys
		if self.harrass == 1:
			sys.stderr.write( \
				"biggles: %s is deprecated - use %s instead\n" \
				% (self.old, self.new) )
		return apply( self.obj, args, kw )

# XXX:deprecated 1.0
Plot2D = _deprecated( FramedPlot, "Plot2D", "FramedPlot" )

# XXX:deprecated 1.3
ErrorEllipses = _deprecated( Ellipses, "ErrorEllipses", "Ellipses"  )
LabelData = _deprecated( DataLabel, "LabelData", "DataLabel" )
LabelPlot = _deprecated( PlotLabel, "LabelPlot", "PlotLabel" )
LineKey = _deprecated( OldKey, "LineKey", "PlotKey" )
LineSlope = _deprecated( Slope, "LineSlope", "Slope" )
SymbolKey = _deprecated( OldKey, "SymbolKey", "PlotKey" )

# XXX:deprecated 1.5
CustomFramedPlot = _deprecated( \
	OldCustomFramedPlot, "CustomFramedPlot", "FramedPlot", 0 )
readcolumn = _deprecated( read_column, "readcolumn", "read_column", 0 )

try:
	del _biggles
	del biggles
	del config
	del contour
	del func
	del geometry
	del hammer
except NameError:
	pass

