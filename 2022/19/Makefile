CFLAGS += -Wall -Wextra -O3

LDLIBS = $(LIBS)

all: first second

first.o second.o: common.h

clean:
	$(RM) first second *.o
	$(RM) -v *conan*.sh conan*info.txt graph_info.json conan.lock
	$(RM) -r __pycache__
