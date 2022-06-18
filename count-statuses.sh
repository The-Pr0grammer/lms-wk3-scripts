#!/bin/bash

awk '{ print $9 }' ./apache_access | sort -n | uniq -c | awk '{print $2,$1}' | sort -nrk2