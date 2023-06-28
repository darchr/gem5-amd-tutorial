This directory is used by GitHub Codespaces to setup a container to host this repostory.

* **devcontainer.json**: The JSON file defining the container.
* **Dockerfile**: The Dockerfile referenced by "devcontainer.json", and used to create the container.
* **docker**: A directory containing sources for prebuilding the Docker image used by "Dockerfile".
* **on-create.sh**: A script referenced by "devcontainer.json", to be run on the dev container startup.
