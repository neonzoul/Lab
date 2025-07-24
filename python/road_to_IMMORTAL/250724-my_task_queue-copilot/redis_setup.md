# Redis Setup Instructions

## Option 1: Docker (Recommended)

If you have Docker Desktop installed:

```bash
docker run -d -p 6379:6379 redis
```

## Option 2: Windows Redis Installation

1. Download Redis for Windows from: https://github.com/microsoftarchive/redis/releases
2. Extract and run redis-server.exe
3. Default port 6379 should work

## Option 3: WSL2 with Redis

If you have WSL2:

```bash
sudo apt update
sudo apt install redis-server
sudo service redis-server start
```

## Option 4: Use Redis Cloud (Free)

1. Go to https://redis.com/redis-enterprise-cloud/
2. Create a free account
3. Get connection details and update app.py accordingly

## Testing Redis Connection

Once Redis is running, you can test the connection:

```bash
redis-cli ping
```

Should return: PONG
