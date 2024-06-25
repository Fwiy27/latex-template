input = test
output = output

build:
	pandoc --from markdown \
		--to latex $(input).md \
		--output $(output).tex \
		--filter=dependencies/filter.py \
		--template=dependencies/template.tex
	pdflatex $(output).tex
	pdflatex $(output).tex
	pdflatex $(output).tex
	find . -name "$(output).*" |\
		grep -v "$(output).pdf" |\
		xargs rm -rf