line = "$(1)[ $(2) ]$(COLOR)"

all: clean venv xcompile $(EXECUTABLE)
	@echo $(call line,\n${GREEN},wikid: exec)
	@-$(SH) -c "source $(VENV_MAC_DIR)/bin/activate && $(BIN_DIR)/$(EXECUTABLE)"
	@echo $(call line,${GREEN},wikid: exit)

docker:
	@-docker-compose up

xcompile:
	@echo $(call line,\n${GREEN},convert: python to xmacro)
	@-cd $(TOOL_DIR) && $(PYTHON) xcompile.py
	@echo $(call line,${GREEN},convert: complete)

$(EXECUTABLE):
	@echo $(call line,\n${PURPLE},wikid: compile)
	@-$(CC) $(WARNINGS) -Wall -I. -I$(MACRO_DIR) -std=$(STD) \
		`$(VENV_MAC_DIR)/bin/python-config --cflags` \
		./$(MAIN_C) $(OUTPUT) \
		`$(VENV_MAC_DIR)/bin/python-config --ldflags`
	@echo $(call line,${PURPLE},wikid: built)

venv:
	@echo $(call line,\n${GREEN},venv: init)
	@-$(VENV) -p /usr/bin/python2.7 $(VENV_MAC_DIR) --no-site-packages
	@echo $(call line,${GREEN},venv: created)
	@echo $(call line,\n${PURPLE},python: install exec)
	@-$(SH) -c "source $(VENV_MAC_DIR)/bin/activate && \
		pip install -r $(CONFIG_DIR)/python/requirements.txt"
	@echo $(call line,${PURPLE},python: install exit)

clean:
	@echo $(call line,\n${BLUE},clean: exec)
	@-$(RM) -r $(BASE_PATH)/__pycache__/ $(BASE_PATH)/*.pyc
	@-$(RM) -r $(VENV_MAC_DIR)/ && mkdir $(VENV_MAC_DIR)/
	@-cp ./templates/special/gitignore.txt $(VENV_MAC_DIR)/.gitignore
	@-$(RM) -r $(VENV_LINUX_DIR)/ && mkdir $(VENV_LINUX_DIR)/
	@-cp ./templates/special/gitignore.txt $(VENV_LINUX_DIR)/.gitignore
	@echo $(call line,${BLUE},clean: exit)

#[endfi]
