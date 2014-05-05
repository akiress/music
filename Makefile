CXX = gcc
CFLAGS = -fPIC

button.pd_linux: button.o
	ld $(CFLAGS) -export-dynamic -shared -o button.pd_linux button.o -lc -lm -lwiringPi

button.o: button.c
	$(CXX) -c button.c -o button.o

clean:
	rm *.pd_linux
	rm *.o
