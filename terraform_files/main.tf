terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.3.0"
    }
  }
}

provider "google" {
  credentials = "./keys.json"
  project     = "devops-assessment-436417"
  region      = "us-central1"
}

resource "google_cloud_run_service" "backend" {
  name     = "backend"
  location = "us-central1"
  template {
    spec {
      containers {
        image = "gcr.io/devops-assessment-436417/backend:latest"
        ports {
          container_port = 8080
        }
      }
    }
  }
}

resource "google_cloud_run_service" "frontend" {
  name     = "frontend"
  location = "us-central1"
  template {
    spec {
      containers {
        image = "gcr.io/devops-assessment-436417/frontend:latest"
        ports {
          container_port = 8080
        }
      }
    }
  }
}

output "backend_url" {
  value = google_cloud_run_service.backend.status[0].url
}

output "frontend_url" {
  value = google_cloud_run_service.frontend.status[0].url
}
