.PHONY: html clean live-html

html:
	hugo
	npx pagefind

live-html:	html
	hugo server --baseURL "" --bind 0.0.0.0

clean:
	rm -rf "public/*"
	rm -rf _pagefind/
	hugo mod clean
