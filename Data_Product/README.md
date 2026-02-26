# Ministry of Age - Crab Predictor 🦀

This is a full-stack Machine Learning application with a Flask backend and a premium HTML/CSS frontend.

## 📂 Project Structure
```
/project-folder
├── cleanCrabAgePrediction.csv     # The dataset
├── verify_truth.py                # Script to verify model accuracy
├── backend/
│   ├── app.py                     # The Flask Server (Main Entry Point)
│   ├── train_model.py             # Script to retrain the model
│   └── requirements.txt           # List of libraries needed
├── crab_age_model_pipeline.pkl    # Trained Model (Auto-generated)
└── frontend/
    ├── index.html                 # Home Page
    ├── style.css                  # Ministry of Crab Theme
    └── ... (other pages)
```

## 🚀 How to Run on Another PC

### Step 1: Copy Files
Copy this entire folder to the new computer.

### Step 2: Install Python
Make sure Python is installed. You can download it from [python.org](https://www.python.org/).
Ensure you check "Add Python to PATH" during installation.

### Step 3: Install Dependencies
Open a terminal (Command Prompt or PowerShell) inside this folder and run:
```bash
pip install -r backend/requirements.txt
```

### Step 4: Run the Application
In the same terminal, run:
```bash
python backend/app.py
```

### Step 5: Access the Website
Open your web browser and go to:
**http://127.0.0.1:5000/**

---

## 🔧 Troubleshooting
- **Missing Model Error?**
  If `crab_age_model_pipeline.pkl` is missing, run the training script:
  ```bash
  python backend/train_model.py
  ```
- **Port Already in Use?**
  If port 5000 is busy, edit `backend/app.py` and change `port=5000` to `port=5001`.
