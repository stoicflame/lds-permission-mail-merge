#!/bin/bash

for i in $(ls); do pdftk /tmp/2017_parental_or_guardian_permission_medical_release.pdf fill_form "$i" output ${i%.*}.pdf; done