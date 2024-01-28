variable "credentials" {
  description = "my credentials"
  default     = "./keys/creds.json"

}

variable "project" {
  description = "Project"
  default     = "de-zoomcamp-2024-412209"
}

variable "region" {
  description = "Project region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bigquery_dataset_name" {
  description = "My Bigquery Dataset Name"
  default     = "data_zoomcamp_2024"
}

variable "gcs_bucket_class" {
  description = "Storage Class Name"
  default     = "STANDARD"
}

variable "gcs_bucket_name" {
  description = "My google cloud storage bucket Name"
  default     = "data-bucket-2024"
}

variable "dataset_name" {
  description = "My Bigquery Dataset Name"
  default     = "data_zoomcamp_2024"
}