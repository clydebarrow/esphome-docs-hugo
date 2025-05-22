.PHONY: html clean live-html

html:
	hugo
	npx pagefind

live-html:	html
	hugo server

clean:
	rm -rf "public/*"
	rm -rf _pagefind/
	hugo mod clean
