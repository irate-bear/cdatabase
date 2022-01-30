main: main.c 
	$(CC) *.c -o cdb -Wall -Wextra -pedantic -std=c99
run:
	./cdb mydb.db