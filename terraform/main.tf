terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.13.0"
    }
  }
}

provider "google" {
  # Configuration options
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}

resource "google_storage_bucket" "bucket-demo" {
  name     = var.gcs_bucket_name
  location = var.location
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.bigquery_dataset_name
  location   = var.location
}
