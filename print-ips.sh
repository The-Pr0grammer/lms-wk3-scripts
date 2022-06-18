#!/bin/bash

awk '{ print $1 } ' ./apache_access | sort | uniq | wc -l