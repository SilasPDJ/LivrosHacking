echo "This creates a new script, pass the arg as script name.\n chmod +x will allow the script to run"
$(touch $1)
$(chmod +x $1)
$(gedit $1)
