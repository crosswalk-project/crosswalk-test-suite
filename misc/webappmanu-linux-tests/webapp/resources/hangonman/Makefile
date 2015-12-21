PROJECT = hangonman
INSTALL_FILES = audio css data fonts icon.png images index.html js LICENSE _locales manifest.json 

# Boiler-plate code below here

VERSION := $(shell sed -nr 's/.*"version"\s*:\s*"([^"]+)".*/\1/p' manifest.json)
PROJVER = $(PROJECT)-$(VERSION)
ARCHIVE = $(PROJVER).tar.bz2

INSTALL_DIR = ${DESTDIR}/usr/share/$(PROJECT)
DESKTOP_DIR = ${DESTDIR}/usr/share/applications
ICON_DIR    = ${DESTDIR}/usr/share/pixmaps

all:
	@echo "Nothing to build"

.PHONEY: tag dist install

install:
	mkdir -p $(INSTALL_DIR)/
	cp -a $(INSTALL_FILES) $(INSTALL_DIR)/
	mkdir -p $(DESKTOP_DIR)/
	cp $(PROJECT).desktop $(DESKTOP_DIR)/
	mkdir -p $(ICON_DIR)/
	cp icon.png $(ICON_DIR)/$(PROJECT).png

tag:
	@if ! git tag -l $(VERSION)|grep -q $(VERSION); then \
	  echo; echo '>>> Creating new tag "$(VERSION)".  Do not forget to push this new tag with "git push --tags".'; echo; \
	  git tag $(VERSION); \
	fi

dist: tag
	@if [ -f $(ARCHIVE) ]; then rm $(ARCHIVE); fi
	git archive --format=tar --prefix=$(PROJVER)/ $(VERSION) | gzip > $(ARCHIVE)


