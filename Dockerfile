# Sử dụng Python 3.12 slim image tối ưu
FROM python:3.12-slim

# Cài đặt các package hệ thống cần thiết
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Thiết lập working directory
WORKDIR /app

# Copy file requirements trước để cache layer docker
COPY requirements.txt .

# Cài đặt dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source code
COPY . .

# Expose port
EXPOSE 8000

# Chạy ứng dụng
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
