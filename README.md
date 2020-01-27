# Automate Splunk DB Connect Collections and Inputs

This python script generate db_connections.conf and db_inputs.conf for splunk_app_db_connect AddOn. You can create the date, put it in your TAs local Folder and restart Splunk, but please do not first test this in production ;)

1. Modify inputs_full.csv according to your databases
2. Run `python generate_db_connections_conf_full.py`
3. Revies the two newly generated files in the same directoy as your script and inputs_full.csv and add it to the Splunk DB Connect AddOns local folder in your test stage
4. Restart Splunk


