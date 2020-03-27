.DEFAULT_GOAL := all
MAKEFLAGS += --no-builtin-rules

ifeq ($(shell uname -s), Darwin)
    BLACK         := black
    CHECKTESTDATA := checktestdata
    COVERAGE      := coverage3
    MYPY          := mypy
    PYDOC         := pydoc3
    PYLINT        := pylint
    PYTHON        := python3
else ifeq ($(shell uname -p), unknown)
    BLACK         := black
    CHECKTESTDATA := checktestdata
    COVERAGE      := coverage
    MYPY          := mypy
    PYDOC         := pydoc
    PYLINT        := pylint
    PYTHON        := python
else
    BLACK         := black
    CHECKTESTDATA := checktestdata
    COVERAGE      := coverage3
    MYPY          := mypy
    PYDOC         := pydoc3
    PYLINT        := pylint3
    PYTHON        := python3
endif

FILES :=                                  \
    .gitignore                            \
    .gitlab-ci.yml                        \
    collatz-tests                         \
    Collatz.py                            \
    makefile                              \
    RunCollatz.in                         \
    RunCollatz.out                        \
    RunCollatz.py                         \
    TestCollatz.py						  \
    collatz-tests/jiwonny-RunCollatz.in   \
    collatz-tests/jiwonny-RunCollatz.out  \
    Collatz.html                          \
    Collatz.log                           \

.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@

collatz-tests:
	git clone https://gitlab.com/gpdowning/cs373-collatz-tests.git collatz-tests

Collatz.html: Collatz.py
	-$(PYDOC) -w Collatz

Collatz.log:
	git log > Collatz.log

RunCollatz.pyx: Collatz.py RunCollatz.py .pylintrc
	-$(MYPY)   Collatz.py
	-$(PYLINT) Collatz.py
	-$(MYPY)   RunCollatz.py
	-$(PYLINT) RunCollatz.py
	./RunCollatz.py < cs373-collatz-tests/jiwonny-RunCollatz.in > RunCollatz.tmp
	diff RunCollatz.tmp cs373-collatz-tests/jiwonny-RunCollatz.out

TestCollatz.pyx: Collatz.py TestCollatz.py .pylintrc
	-$(MYPY)   Collatz.py
	-$(PYLINT) Collatz.py
	-$(MYPY)   TestCollatz.py
	-$(PYLINT) TestCollatz.py
	$(COVERAGE) run    --branch TestCollatz.py
	$(COVERAGE) report -m

all:

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -f  *.tmp
	rm -rf __pycache__
	rm -rf .mypy_cache

check: $(FILES)

config:
	git config -l

ctd:
	$(CHECKTESTDATA) RunCollatz.ctd  RunCollatz.in

docker:
	docker run -it -v $(PWD):/usr/python -w /usr/python gpdowning/python

format:
	black Collatz.py
	black RunCollatz.py
	black TestCollatz.py

init:
	touch README
	git init
	git remote add origin git@gitlab.com:gpdowning/cs373-collatz.git
	git add README.md
	git commit -m 'first commit'
	git push -u origin master

pull:
	make clean
	@echo
	git pull
	git status

push:
	make clean
	@echo
	git add .gitignore
	git add .gitlab-ci.yml
	-git add Collatz.html
	-git add Collatz.log
	git add Collatz.py
	git add makefile
	git add README.md
	git add RunCollatz.ctd
	git add RunCollatz.in
	git add RunCollatz.out
	git add RunCollatz.py
	git add TestCollatz.py
	git commit -m "another commit"
	git push
	git status

run: RunCollatz.pyx TestCollatz.pyx

scrub:
	make clean
	rm -f  Collatz.html
	rm -f  Collatz.log
	rm -rf collatz-tests

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

sync:
	@pwd
	@rsync -r -t -u -v --delete			   \
    --include "Collatz.py"                 \
    --include "RunCollatz.ctd"             \
    --include "RunCollatz.in"              \
    --include "RunCollatz.out"             \
    --include "RunCollatz.py"              \
    --include "TestCollatz.py"             \
    --exclude "*"                          \
    ~/projects/python/collatz/ .
	@rsync -r -t -u -v --delete            \
    --include "makefile"                   \
    --include "Collatz.py"                 \
    --include "RunCollatz.ctd"             \
    --include "RunCollatz.in"              \
    --include "RunCollatz.out"             \
    --include "RunCollatz.py"              \
    --include "TestCollatz.py"             \
    --exclude "*"                          \
    . downing@$(CS):cs/git/cs373-collatz/

versions:
	@echo  'shell uname -p'
	@echo $(shell uname -p)
	@echo
	@echo  'shell uname -s'
	@echo $(shell uname -s)
	@echo
	@echo "% which $(BLACK)"
	@which $(BLACK)
	@echo
	@echo "% $(BLACK) --version"
	@$(BLACK) --version
	@echo
	@echo "% which $(COVERAGE)"
	@which $(COVERAGE)
	@echo
	@echo "% $(COVERAGE) --version"
	@$(COVERAGE) --version
	@echo
	@echo "% which $(MYPY)"
	@which $(MYPY)
	@echo
	@echo "% $(MYPY) --version"
	@$(MYPY) --version
	@echo
	@echo "% which $(PYDOC)"
	@which $(PYDOC)
	@echo
	@echo "% $(PYDOC) --version"
	@$(PYDOC) --version
	@echo
	@echo "% which $(PYLINT)"
	@which $(PYLINT)
	@echo
	@echo "% $(PYLINT) --version"
	@$(PYLINT) --version
	@echo
	@echo "% which $(PYTHON)"
	@which $(PYTHON)
	@echo
	@echo "% $(PYTHON) --version"
	@$(PYTHON) --version
	
hackerrank:
	rm -rf CollatzHackerrank.py
	cat Collatz.py >> CollatzHackerrank.py
	cat RunCollatz.py | sed "/from Collatz/d" >> CollatzHackerrank.py