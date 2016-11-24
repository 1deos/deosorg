dht: dht.build
	@chmod +x $(PATH_BIN)/dht
	$(PATH_BIN)/dht

dht.build: dht.clean $(PATH_OBJ)/dht.o
	$(CC) -std=c89 -Wall -g\
		-I$(PATH_LIB)\
		-c $(PATH_SRC)/dht-example.c\
		$(PATH_OBJ)/dht.o\
		-o $(PATH_BIN)/dht\
		-lcrypt

$(PATH_OBJ)/dht.o:
	$(CC) -std=c89 -Wall -g\
		-I$(PATH_LIB)\
		-c $(PATH_SRC)/dht.c\
		-o $(PATH_OBJ)/dht.o

dht.clean:
	-rm -rf $(PATH_OBJ)/dht.o
	-rm -rf $(PATH_BIN)/dht
