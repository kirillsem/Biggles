include make.inc

SRCDIR		= ./src
EXAMPLESDIR	= ./examples

.PHONY: all install uninstall clean

all:
	cd $(SRCDIR) && $(MAKE) all
	cd $(SRCDIR)/libplot && $(MAKE) all

install: all
	[ -d $(BIGGLESDIR) ] || mkdir -m755 $(BIGGLESDIR)
	install -m644 $(SRCDIR)/*.ini $(BIGGLESDIR)
	install -m644 $(SRCDIR)/*.py  $(BIGGLESDIR)
	install -m644 $(SRCDIR)/*.pyc $(BIGGLESDIR)
	install -m755 $(SRCDIR)/*.so  $(BIGGLESDIR)
	[ -d $(BIGGLESDIR)/libplot ] || mkdir -m755 $(BIGGLESDIR)/libplot
	install -m644 $(SRCDIR)/libplot/*.py  $(BIGGLESDIR)/libplot
	install -m644 $(SRCDIR)/libplot/*.pyc $(BIGGLESDIR)/libplot
	install -m755 $(SRCDIR)/libplot/*.so  $(BIGGLESDIR)/libplot

uninstall:
	[ -d $(BIGGLESDIR) ] && rm -rf $(BIGGLESDIR)

clean:
	cd $(SRCDIR) && $(MAKE) clean
	cd $(SRCDIR)/libplot && $(MAKE) clean
	-cd $(EXAMPLESDIR) && rm *.png *.eps

