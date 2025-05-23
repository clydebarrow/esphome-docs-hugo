.PHONY: html clean live-html

html: repo-data
	hugo
	npx pagefind

repo-data:
	echo "url: `git config --get remote.origin.url`" > data/repo.yaml

live-html:	html
	hugo server --baseURL "" --bind 0.0.0.0

clean:
	rm -rf "public/*"
	rm -rf _pagefind/
	hugo mod clean
