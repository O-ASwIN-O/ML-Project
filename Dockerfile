FROM python:3.10.19-slim

WORKDIR /app

# Install minimal build/runtime deps required by some packages (catboost/xgboost)
RUN apt-get update \
	&& apt-get install -y --no-install-recommends libgomp1 \
	&& rm -rf /var/lib/apt/lists/*

# Install Python dependencies first (leverages Docker cache)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . /app

EXPOSE 5000
CMD ["python", "app.py"]