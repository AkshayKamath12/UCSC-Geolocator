# Use the newly created image as the base image
FROM base_image

# Set the working directory
WORKDIR /app

# Copy the necessary files
COPY . /app

# Install any dependencies if needed
RUN pip install --ignore-installed -r requirements.txt

# Command to run the model.py script
CMD ["python", "model.py"]