#[DeOS]
deos: deos.run.pre deos.run deos.run.post

#[Build]
deos.build: deos.clean $(OBJECTS)
	@$(PRINT) yellow $@ start
	$(CC) -std=c89 -Wall -g\
		-pthread\
		-I$(PATH_LIB)/atdlib\
		$(PATH_DOJO)/main.c\
		$(OBJECTS)\
		-o $(PATH_BIN)/deos
	chmod +x $(PATH_BIN)/deos
	@$(PRINT) yellow $@ stop

#[Build ATD Library]
$(PATH_OBJ)/%.o:
	@$(PRINT) cyan $*.o start
	$(CC) -std=c89 -Wall -g\
		-I$(PATH_LIB)/atdlib\
		-c $(PATH_SRC)/atdlib/$*.c\
		-o $(PATH_OBJ)/$*.o
	@$(PRINT) cyan $*.o stop

#[New]
deos.run.new: deos.build
	@$(PRINT) red deos start

#[Pre-Hook]
deos.run.pre: deos.run.new
	@$(PRINT) purple $@ start
	@
	@$(PRINT) purple $@ stop
	@$(PRINT) blue deos.run start

#[Run]
deos.run:
	$(PATH_BIN)/deos

#[Post-Hook]
deos.run.post:
	@$(PRINT) blue deos.run stop
	@$(PRINT) purple $@ start
	@
	@$(PRINT) purple $@ stop
	@$(MAKE) deos.run.free

#[Free]
deos.run.free:
	@echo
	@$(PRINT) red deos stop

#[Clean]
deos.clean:
	@$(PRINT) cyan $@ start
	-rm -rf $(PATH_BIN)/deos*
	-rm -rf $(PATH_OBJ)/*.o
	@$(PRINT) cyan $@ stop
