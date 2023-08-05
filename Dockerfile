# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install  -r requirements.txt

# Copy the Django project code to the container
COPY . .

# Expose the port on which the Django application will run (default is 8000)
EXPOSE 80

# Set environment variables if necessary
# ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Run database migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
