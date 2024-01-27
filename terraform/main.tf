terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.13.0"
    }
  }
}

provider "google" {
    # Configuration options
  project     = "de-zoomcamp-2024-412209"
  region      = "us-central1"
}