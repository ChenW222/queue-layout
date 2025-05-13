## Requirements

Before starting, ensure you have the following installed:

- Python 3
- pip
- Git

---

## Step 1: Clone the Repository

Open a terminal and run the following commands:

```bash
git init
git remote add origin https://github.com/ChenW222/queue-layout
git pull origin master
```
## Step 2: Create a Virtual Environment

Create a Python virtual environment to manage dependencies locally:

```bash
python -m venv .venv
```

## Step 3: Activate the Virtual Environment

On Linux users:
```bash
source env/bin/activate
```
On Windows:
```
.venv\Scripts\activate
```
## Step 4: Install Dependencies

With the virtual environment activated, install the required packages:

```bash
python3 -m pip install -r requirements.txt
```
## Step 5: Run the Program

Run the program with the sample input file:
```
python3 main.py res/sample1
```
This will generate an output folder containing visualized graph pages.
