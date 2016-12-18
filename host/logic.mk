logic: logic.run.pre logic.run logic.run.post

logic.travis: logic.run.pre logic.run.travis logic.run.post

logic.build: logic.clean $(OBJECTS)
	@$(PRINT) yellow $@ start
	$(CC) -std=c89 -Wall -g -pthread -I$(LIB) $(SRC)/main.c $(OBJECTS) -o $(BIN)/logic
	chmod +x $(BIN)/logic
	@$(PRINT) yellow $@ stop

$(OBJ)/%.o:
	@$(PRINT) cyan $*.o start
	$(CC) -std=c89 -Wall -g -I$(LIB) -c $(SRC)/$*.c -o $(OBJ)/$*.o
	@$(PRINT) cyan $*.o stop

logic.run.new: logic.build
	@$(PRINT) red logic start

logic.run.pre: logic.run.new
	@$(PRINT) purple $@ start
	@
	@$(PRINT) purple $@ stop
	@$(PRINT) blue logic.run start

logic.run:
	$(BIN)/logic

logic.run.travis:
	@(echo "hello, world!")

logic.run.post:
	@$(PRINT) blue logic.run stop
	@$(PRINT) purple $@ start
	@
	@$(PRINT) purple $@ stop
	@$(MAKE) logic.run.free

logic.run.free:
	@(echo && $(PRINT) red logic stop)

logic.clean:
	@$(PRINT) cyan $@ start
	-rm -rf $(BIN)/logic*
	-rm -rf $(OBJ)/*.o
	@$(PRINT) cyan $@ stop
