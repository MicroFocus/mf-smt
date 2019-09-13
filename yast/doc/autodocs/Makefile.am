#Mkefile.am for common/doc/autodocs

htmldir = $(docdir)/autodocs

index.html:
	cd ../../ && yardoc && cd -

html_DATA = $(wildcard *.html)

CLEANFILES = $(html_DATA)

EXTRA_DIST = ../../.yardopts

