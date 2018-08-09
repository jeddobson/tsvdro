# Makefile for tsvdro

all:
	python setup.py install

clean:
	@rm -rf build dist tsvdro.egg-info
