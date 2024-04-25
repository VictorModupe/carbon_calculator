# Personal Carbon Calculator

This Python app uses Streamlit to calculate the Carbon Footprint.

## Setup Instructions

### Step 1: Install Python

Download and install the appropriate Python installer for your operating system:
- [Python Downloads](https://www.python.org/downloads/)

### Step 2: Install Visual Studio Code (Optional)

Download and install Visual Studio Code, a code editor that supports Python development:
- [Visual Studio Code](https://code.visualstudio.com/)




### Step 3: Install pip

Install pip, the Python package installer, by running the following command in your terminal or command prompt:

pip install pip --user




### Step 4: Install Streamlit

Install Streamlit, the Python library used to create the web app, by running the following command:


pip install streamlit


Alternatively, you can open your terminal or command prompt as an administrator and run:


pip install streamlit


### Step 5: Install Dependencies

Install the required Python dependencies listed in the `requirements.txt` file:


pip install -r requirements.txt




### Step 6: Create Python Environment (Optional)

If you prefer, you can create a virtual environment using venv. Run the following command to create a virtual environment named "world":



python -m venv world


Activate the virtual environment by running:
- On Windows: `world\Scripts\activate`
- On macOS/Linux: `source world/bin/activate`

## Running the Streamlit App

To run the Streamlit app, execute the following command in your terminal or command prompt:


streamlit run app.py



## Project Structure

Personal-Carbon-Calculator/
│
├── app.py # Streamlit app code
├── requirements.txt # List of Python dependencies
├── README.md # Project documentation
├── images/ # Directory for images used in the app
│ ├── king.jpg
│ ├── queen.jpg
│ └── pawn.jpg
└── venv/ # Directory for Python virtual environment (created by venv)





## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
