# AWS Production Notes App

A containerized Flask web application built to simulate a production-ready deployment workflow.

## Tech Stack

- Python 3.13
- Flask
- Docker
- Git & GitHub

## Features

- Simple note submission form
- In-memory storage
- Containerized using Docker
- Runs on port 8000

## Run Locally (Without Docker)

python app/app.py

## Run With Docker

Build image:

docker build -t notes-app .

Run container:

docker run --rm -p 8000:8000 notes-app

Then open:

http://127.0.0.1:8000

## Architecture

Browser → Flask App → In-Memory Storage

## Purpose

This project demonstrates:

- Containerization
- Local development workflow
- Git version control
- Secure GitHub authentication using Personal Access Tokens