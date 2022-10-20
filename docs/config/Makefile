all: preview

build:
	mkdocs build --config-file ../generated/mkdocs.yml

deploy-origin:
	mkdocs gh-deploy --force --remote-name origin --config-file ../generated/mkdocs.yml

deploy-upstream:
	mkdocs gh-deploy --force --remote-name upstream --config-file ../generated/mkdocs.yml

check test:
	mkdocs build --strict --config-file ../generated/mkdocs.yml

serve preview:
	mkdocs serve --config-file ../generated/mkdocs.yml
