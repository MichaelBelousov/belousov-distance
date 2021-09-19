
# terrible practice but it's been a while since I hand wrote a makefile...
all: src/main.cpp src/dist_struct.h
	c++ -g src/main.cpp -o out -Isrc

src/dist_struct.h: make_dist_struct.py
	python3 make_dist_struct.py > src/dist_struct.h
