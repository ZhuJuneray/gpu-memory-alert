#!/bin/bash

# Example utility function to send emails
send_email() {
    local subject=$1
    local message=$2
    local recipient=$3
    echo "$message" | mail -s "$subject" "$recipient"
}
