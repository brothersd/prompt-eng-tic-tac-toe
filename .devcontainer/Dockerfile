# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your python script into the container
# Note: Ensure your main file is named 'tic_tac_toe.py' or update below
COPY . .

# Run the game
# The -u flag ensures python output is sent straight to terminal without buffering
#CMD ["python", "-u", "tic_tac_toe.py"]