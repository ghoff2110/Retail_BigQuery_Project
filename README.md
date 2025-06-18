# Retail Project - Data Simulation & BigQuery Integration

This project generates simulated retail data including products, customers, and sales.  
The data is then loaded into Google BigQuery for analysis.

## Prerequisites

- Python 3.8+  i worked on 3.12 v
- Python libraries: `pandas`, `faker`, `google-cloud-bigquery`  
- Google Cloud Platform account with a project configured, BigQuery and Cloud Storage APIs enabled  
- GCP service account with roles `BigQuery Data Editor` and `Storage Admin` and the JSON key file (generated from the gcp)

Don't forget to install this library Faker : pip install pandas faker google-cloud-bigquery

## Installation

1. Clone the repository:  
```bash
git clone https://github.com/yourusername/retail-project.git
cd retail-project
