CFLAGS += -Wall -Wextra -O3

LDLIBS = $(LIBS)

run: first second
	./$<

clean:
	$(RM) first
	$(RM) -v *conan*.sh conan*info.txt graph_info.json conan.lock
	$(RM) -r __pycache__
