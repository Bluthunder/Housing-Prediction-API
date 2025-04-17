# 1. Use an official lightweight Python image as the base
FROM python:3.12-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Explanation:
# - PYTHONDONTWRITEBYTECODE=1 prevents Python from writing .pyc files
# - PYTHONUNBUFFERED=1 ensures output is logged directly to stdout/stderr

# 3. Set the working directory in the container
WORKDIR /app

# 4. Copy requirements file to install dependencies
COPY requirements.txt .

# 5. Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 6. Copy the FastAPI app code into the container
COPY ./app ./app

# 7. Expose the port the FastAPI app will run on
EXPOSE 7001

# 8. Command to run the app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7001"]
