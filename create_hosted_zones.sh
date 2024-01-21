#!/bin/bash

while IFS= read -r domain; do
    echo "Creating hosted zone for $domain..."
    ./create_hosted_zone.py "$domain"
done < domains.txt
