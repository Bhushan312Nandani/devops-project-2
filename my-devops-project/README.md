# DevOps Learning App

This repository is now a real DevOps learning project with:

- a working Python web service
- containerization via `Dockerfile`
- automated CI with GitHub Actions in `.github/workflows/ci.yml`
- tests that run on every push

## What this project shows

- Real GitHub Actions automation: on every push to `main`, GitHub runs `pip install`, `pytest`, and `docker build`
- A runnable web service with health and version endpoints
- A Docker image build that can be deployed or inspected
- A documented learning path for DevOps beginners

## How to use locally

1. Install Docker.
2. Build the container from the inner app folder:

```powershell
cd my-devops-project\my-devops-project
docker build -t devops-learning-app .
```

3. Run the container:

```powershell
docker run -p 5000:5000 devops-learning-app
```

4. Open `http://localhost:5000` in your browser.

5. Check the service endpoints:

```powershell
curl http://localhost:5000/health
curl http://localhost:5000/version
curl http://localhost:5000/info
```

## API endpoints

- `GET /` - app home page with link information
- `GET /health` - service health check
- `GET /version` - returns the app version and build metadata
- `GET /info` - returns service metadata and supported endpoints

## GitHub Actions automation

Push to `main`, then open the GitHub repository's Actions tab and verify the workflow run.

The workflow performs:

1. Checkout the repository
2. Set up Python 3.11
3. Install dependencies from `requirements.txt`
4. Run `pytest tests`
5. Build the Docker image using `Dockerfile`

That is the actual DevOps automation in this repo.
