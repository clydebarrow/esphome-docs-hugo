.PHONY: html clean live-html automations

html: repo-data
	hugo
	npx pagefind

repo-data:
	echo "url: `git config --get remote.origin.url`" > data/repo.yaml
	echo "branch: `git branch --show-current`" >> data/repo.yaml

automations: repo-data
	mkdir -p data/automations
	curl https://data.esphome.io/release/automations.json | ./collate_automations.sh > data/automations/current.json
	curl https://data.esphome.io/beta/automations.json | ./collate_automations.sh > data/automations/beta.json
	curl https://data.esphome.io/dev/automations.json | ./collate_automations.sh > data/automations/next.json

live-html:	html
	hugo server --baseURL "" --bind 0.0.0.0

clean:
	rm -rf "public/*"
	rm -rf "pagefind/*"
	rm -rf data/automations/
	rm -rf data/repo.yaml
	hugo mod clean
