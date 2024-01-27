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
  project = "de-zoomcamp-2024-412209"
  region  = "us-central1"
}

resource "google_storage_bucket" "bucket-demo" {
  name          = "data-bucket-2024"
  location      = "US"
  force_destroy = true
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id                  = "data_zoomcamp_2024"
  friendly_name               = "test"
  description                 = "dataset for test"
  location                    = "EU"
  default_table_expiration_ms = 3600000

  labels = {
    env = "default"
  }

  access {
    role   = "READER"
    domain = "hashicorp.com"
  }
}
