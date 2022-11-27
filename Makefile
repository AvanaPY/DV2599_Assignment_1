zip:
	@rm -rf assignment
	@mkdir assignment
	@cp README.md classify.py data.py hypothesis.py main.py spambase.csv ./assignment
	@zip assignment.zip assignment/*
	@rm -r assignment

unzip: zip
	@unzip assignment.zip

clean:
	@rm -rf assignment assignment.zip