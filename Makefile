# Setup the project environment by:
# - Run pipenv shell to start the virtual env.
env:
	pipenv --python=${conda run which python} --site-packages
	pipenv shell 

# Install all libraries of package.
install-all:
	pipenv install --system --dev

# Install a package. 
install:
	pipenv install $(pkg)

# Install a package in dev mode.
install-dev:
	pipenv install --dev $(pkg)

# Clone code repositories that will be analyzed.
clone:
	python -m bin.clone

# Ask something to GPT and use the VectorDB information.
ask:
	python -m bin.ask

# Insert data in the VectorDB.
insert:
	python -m bin.insert
