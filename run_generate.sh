#!/bin/bash

# Display a start message
echo "Starting the Python script..."

# Execute the Python script
python generate.py

# Check if the script executed successfully
if [ $? -eq 0 ]; then
  echo "Script executed successfully!"
else
  echo "Script failed to execute."
  exit 1
fi

# Display a completion message
echo "Done."