.DEFAULT_GOAL := gem5-amd-tutorial-env

gem5-amd-tutorial-env : gem5-amd-tutorial-env-pull
	docker build . -t gcr.io/gem5-test/gem5-amd-tutorial-env:latest

gem5-amd-tutorial-env-pull :
	- docker pull gcr.io/gem5-test/gem5-amd-tutorial-env:latest

clean :
	- docker image rm gcr.io/gem5-test/gem5-amd-tutorial-env:latest

push : gem5-amd-tutorial-env
	docker push gcr.io/gem5-test/gem5-amd-tutorial-env:latest
