################################################################################
#                        Genie Makefile
#
# Author:
#   pyats-support-ext@cisco.com
#
# Support:
#   pyats-support-ext@cisco.com
#
# Version:
#   v1.0
#
# Date:
#   December 2020
#
# About This File:
#   This script will build the documentation of the Genie package which could
#   be served locally via make serve
#
# Requirements:
#	1. Please install dependencies via the make install_build_deps command first
################################################################################

# You can set these variables from the command line.
# Replace later
#	`git status -- .`\n\n\
#	`git log -n 1 --stat -- .`\n\n" | \
#	"mail -s "$(HEADER) Documentation Updated by ${USER}" $(WATCHERS)"
#$(SPHINXAPI) ${VIRTUAL_ENV}/projects/genie_libs -H 'genie_libs apidoc' -F -e -o genie_libs `find ${VIRTUAL_ENV}/projects/genie_libs -maxdepth 1-type d -not -name genie `
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXAPI     = sphinx-apidoc
PAPER         = letter
SOURCEDIR     = .
BUILDDIR      = $(shell pwd)/__build__/documentation
CLEAN_DIR	  = $(shell pwd)/__build__
HOSTNAME      = localhost

# Dependencies for building documentation
DEPENDENCIES = robotframework Sphinx sphinxcontrib-napoleon \
			   sphinxcontrib-mockautodoc sphinx-rtd-theme sphinxcontrib_robotframework

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help install_build_deps docs serve html clean

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "docs:            	Build Sphinx documentation for this package"
	@echo "clean: 			Remove generated documentation"
	@echo "install_build_deps: 	Install build dependencies for docs (will be run in make docs)"
	@echo ""
	@echo "     --- default Sphinx targets ---"
	@echo ""
	@echo "html:       		to make standalone HTML files"
	@echo "serve:      		to start a web server to serve generated html files"

install_build_deps:
	@echo "Installing build dependecies into your environment"
	@pip install $(DEPENDENCIES)
	@echo ""
	@echo "Done"

clean:
	rm -rf $(CLEAN_DIR)

serve:
	@echo "point your browser to http://$(HOSTNAME):8000"
	@cd $(BUILDDIR)/html && python -m http.server || echo Error: run \'make \
	html\' before using \'make serve\'

docs: html
	@echo ""
	@echo "Done."
	@echo ""

html: install_build_deps
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html -devnet
	@echo
	python -m robot.libdoc genie.libs.robot.GenieRobot $(BUILDDIR)/html/userguide/robot.html
	python -m robot.libdoc genie.libs.robot.GenieRobotApis $(BUILDDIR)/html/userguide/robot_api.html
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

serve:
	@echo "point your browser to http://$(HOSTNAME):8000"
	@cd $(BUILDDIR)/html && python -m http.server || echo Error: run \'make \
	docs\' before using \'make serve\'
