# Project Name
> Brief project description - A concise overview of what the project does and its purpose, focusing on integrating Apache Airflow with GitHub Actions.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Workflow Overview](#workflow-overview)
- [Testing](#testing)
- [Deployment](#deployment)

## Introduction
This project automates the testing and deployment of Apache Airflow DAGs using GitHub Actions. It ensures that DAGs are automatically tested for errors before they are deployed to an Airflow environment, enhancing reliability and efficiency in managing workflows.

## Prerequisites
- GitHub Account
- Access to an Apache Airflow environment
- Basic understanding of YAML and Python

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
   ```
2. **Configure Airflow**
   Ensure Apache Airflow is installed and configured in your environment.
   Set up necessary Airflow configurations as outlined in airflow.cfg.
3. **Set up GitHub Secrets**
   AIRFLOW_WEB_SERVER: Your Airflow web server address.
   SSH_KEY: SSH key for secure communication with the Airflow server.

## Workflow Overview
The project uses GitHub Actions defined in .github/workflows/ci_cd_pipeline.yml to manage the lifecycle of Airflow DAGs:

1. Test: On every push to the main branch or on pull request, DAGs are tested for syntax and logical errors.
2. Deploy: If tests pass, DAGs are automatically deployed to the specified Airflow environment.
3. GitHub Actions Breakdown
4. Checkout Code: Fetches the latest code from the GitHub repository.
5. Setup Python Environment: Configures the Python environment needed for testing.
6. Install Dependencies: Installs required Python packages from requirements.txt.
7. Run Tests: Executes tests located in the tests/ directory.
8. Deploy: If all tests pass, the deployment script scripts/deploy_dags.sh is executed to transfer DAGs to the Airflow server.

## Testing

To run tests:
```bash
pytest tests/
```

Ensure you have all dependencies installed as per the requirements.txt.

## Deployment

DAGs are deployed to the Airflow environment using SSH. The deployment process is triggered automatically upon a successful test phase in the GitHub Actions workflow.
