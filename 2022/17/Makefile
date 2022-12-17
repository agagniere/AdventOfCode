CFLAGS += -Wno-gnu-designator -Wall -Wextra -O3

run: first second
	./first
	./second

clean:
	$(RM) first second *.o

re: clean
	$(MAKE) run

.PHONY: run clean
