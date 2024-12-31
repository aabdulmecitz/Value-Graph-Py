push:
	git add .
	git commit -m "commit"
	git push

run:
	sudo python3 ./graph/graph.py

test_communicate:
	sudo python3 ./communicate/communicate.py