# Test Makefile

## Variables/Ingredients

SHELL := /bin/bash
.PHONY := help
.DEFAULT_RULES := help setup build

## Recipe/Targets
help:
	## Display help message
	@echo -e "[+] help : Display Help message"
	@echo -e "[+] setup : Perform setup"
	@echo -e "[+] build : Build from Source"

setup:
	## Perform setup 

build: setup
	## Build from source
	@make -j3

