# Miniature Stellar Array Controller 

Welcome to the Miniature Stellar Array Controller project! This is a simple Python application designed to demonstrate a complete, working CI/CD (Continuous Integration/Continuous Deployment) pipeline using GitHub Actions.

The application itself simulates the control of a stellar array, allowing for alignment and power adjustments. However, its primary purpose is to showcase automated testing, building, and simulated deployment.

##  Features

* **Simple Python Application**: A `StellarArray` class with methods to `align`, `adjust_power`, and get `status`.
* **Automated Tests**: Unit tests written with `pytest` to ensure code quality.
* **Containerization**: A `Dockerfile` to package the application into a consistent environment.
* **CI/CD Pipeline**: Automated workflow using GitHub Actions (`.github/workflows/ci-cd-pipeline.yml`) that triggers on every push to the `main` branch.

##  Technologies Used

* **Python 3.9+**
* **pytest** (for testing)
* **Docker** (for containerization)
* **GitHub Actions** (for CI/CD automation)

##  Project Structure

stellar-array-controller/
├── .github/
│   └── workflows/
│       └── ci-cd-pipeline.yml  # GitHub Actions workflow definition
├── Dockerfile                  # Instructions to build the Docker image
├── requirements.txt            # Python project dependencies (e.g., pytest)
├── stellar_controller.py       # Main Python application logic
└── test_controller.py          # Pytest unit tests for the application
└── README.md                   # This file


##  CI/CD Pipeline Overview

The CI/CD pipeline is defined in `.github/workflows/ci-cd-pipeline.yml` and is automatically triggered by a `push` or `pull_request` to the `main` branch.

The pipeline performs the following steps:

1.  **Checkout Code**: Fetches the latest version of your repository's code.
2.  **Set up Python**: Configures the specified Python environment (e.g., Python 3.9).
3.  **Install Dependencies**: Installs necessary Python packages listed in `requirements.txt` (primarily `pytest`).
4.  **Run Tests**: Executes the automated tests using `pytest`. If any test fails, the pipeline stops, preventing deployment of faulty code.
5.  **Build Docker Image**: If all tests pass, it builds a Docker image of the application named `stellar-array-controller:latest`.
6.  **Simulate Deployment**: Performs a simulated deployment, echoing messages to the console indicating a successful deployment to a "Test Rig". In a real-world scenario, this step would deploy the application to a staging or production environment.

## 🛠 Getting Started & Seeing CI/CD in Action

1.  **Clone the repository :**
    ```bash
    git clone https://github.com/amirmahdiBeirami/stellar-array-controller.git
    cd stellar-array-controller
    ```

2.  **Make a small code change:**
    For example, open `stellar_controller.py` and modify one of the print statements or a calculation.
    *Example: In the `align` method, change the message:*
    ```python
    # In stellar_controller.py
    # Original:
    # message = f"{self.name} aligned to {self.alignment_degrees} degrees. Current Power: {self.power_output_gw} GW."
    # New:
    message = f"**URGENT RE-ALIGNMENT** {self.name} is now precisely aligned to {self.alignment_degrees} degrees. Power: {self.power_output_gw} GW. Check telemetry!"
    ```

3.  **Commit and push the change:**
    ```bash
    git add stellar_controller.py
    git commit -m "Test: Updated stellar alignment confirmation message"
    git push origin main
    ```

4.  **Observe the CI/CD Pipeline:**
    * Go to your GitHub repository in your web browser.
    * Click on the **"Actions"** tab.
    * You will see a new workflow run triggered by your push. Click on it to see the steps (Checkout, Set up Python, Install Dependencies, Run Tests, Build Docker Image, Simulate Deployment) execute in real-time.


##  Purpose of this Demo

This project serves as a practical, hands-on example for understanding and demonstrating:
* The core principles of CI/CD.
* How to set up a basic pipeline using GitHub Actions.
* The benefits of automating software testing and deployment processes, such as:
    * Faster feedback cycles.
    * Reduced manual errors.
    * Increased deployment frequency and reliability.
    * Improved developer productivity.
