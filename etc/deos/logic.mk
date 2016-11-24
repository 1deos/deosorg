#[logic]
logic: logic.run.pre logic.run logic.run.post
logic.travis: logic.run.pre logic.run.travis logic.run.post


#[Build]
logic.build: logic.clean $(OBJECTS)
	@$(PRINT) yellow $@ start
	$(CC) -std=c89 -Wall -g\
		-pthread\
		-I$(PATH_LIB)\
		$(PATH_DOJO)/main.c\
		$(OBJECTS)\
		-o $(PATH_BIN)/logic
	chmod +x $(PATH_BIN)/logic
	@$(PRINT) yellow $@ stop

#[Build ATD Library]
$(PATH_OBJ)/%.o:
	@$(PRINT) cyan $*.o start
	$(CC) -std=c89 -Wall -g\
		-I$(PATH_LIB)\
		-c $(PATH_SRC)/$*.c\
		-o $(PATH_OBJ)/$*.o
	@$(PRINT) cyan $*.o stop

#[New]
logic.run.new: logic.build
	@$(PRINT) red logic start

#[Pre-Hook]
logic.run.pre: logic.run.new
	@$(PRINT) purple $@ start
	@
	@$(PRINT) purple $@ stop
	@$(PRINT) blue logic.run start

#[Run]
logic.run:
	$(PATH_BIN)/logic
logic.run.travis:
	@echo "hello, world!"

#[Post-Hook]
logic.run.post:
	@$(PRINT) blue logic.run stop
	@$(PRINT) purple $@ start
	@
	@$(PRINT) purple $@ stop
	@$(MAKE) logic.run.free

#[Free]
logic.run.free:
	@echo
	@$(PRINT) red logic stop

#[Clean]
logic.clean:
	@$(PRINT) cyan $@ start
	-rm -rf $(PATH_BIN)/logic*
	-rm -rf $(PATH_OBJ)/*.o
	@$(PRINT) cyan $@ stop
