pos.png vel.png phase.png : JQ_graph.py tray.txt
	python JQ_graph.py
tray.txt : gravity
	./gravity > tray.txt
gravity:
	c++ JQ_gravity.cpp -o gravity
