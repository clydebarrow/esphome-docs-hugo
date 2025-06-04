.PHONY: html clean live-html automations check-links anchors production convert-from-rst

check-links: repo-data anchors
	hugo --environment production

anchors:
	hugo --environment anchors
	python3 tools/md_anchors.py

production: repo-data anchors
	hugo --minify
	npx pagefind
	hugo --minify

repo-data:
	mkdir -p data/automations
	echo "url: `git config --get remote.origin.url`" > data/repo.yaml
	echo "branch: `git branch --show-current`" >> data/repo.yaml
	curl -s -S https://data.esphome.io/release/automations.json | tools/collate_automations.sh > data/automations/current.json
	curl -s -S https://data.esphome.io/beta/automations.json | tools/collate_automations.sh > data/automations/beta.json
	curl -s -S https://data.esphome.io/dev/automations.json | tools/collate_automations.sh > data/automations/next.json

live-html:	repo-data anchors
	npx pagefind
	hugo server --bind 0.0.0.0

clean:
	rm -rf "public/*"
	rm -rf "pagefind/*"
	rm -rf data/automations/
	rm -rf data/repo.yaml
	hugo mod clean

convert-from-rst: 
	python3 tools/convert_rst_to_md.py ./esphome-docs .
