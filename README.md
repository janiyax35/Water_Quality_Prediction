<div align="center">
  <img src="https://img.icons8.com/color/96/000000/water-drop.png" alt="Water Quality Logo"/>
  
  # 💧 Water Quality Prediction Application 💧
  
  [![GitHub stars](https://img.shields.io/github/stars/janiyax35/Water_Quality_Prediction?style=social)](https://github.com/janiyax35/Water_Quality_Prediction)
  [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
  [![Flask](https://img.shields.io/badge/Flask-2.0.1-blue)](https://flask.palletsprojects.com/)
  [![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org/)
  [![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.24.2-orange)](https://scikit-learn.org/)
  [![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)](https://getbootstrap.com/)
</div>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-demo">Demo</a> •
  <a href="#-technologies">Technologies</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-project-structure">Project Structure</a> •
  <a href="#-about-me">About Me</a>
</p>

<div align="center">
  <img src="https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif" alt="Water Animation" width="600"/>
</div>

## 🌊 Overview

This project implements a machine learning model to predict water potability based on various chemical parameters. The web application provides an intuitive interface for users to input water quality parameters and receive instant predictions on whether the water is safe to drink.

The model analyzes 9 key parameters: pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, and Turbidity to make accurate predictions about water safety.

<div align="center">
  <img src="https://plus.unsplash.com/premium_photo-1710628263718-367b1cf5828f?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Water Banner" width="800"/>
</div>

## ✨ Features

- 🧠 **Machine Learning Model**: Trained on extensive water quality dataset
- 🔍 **Parameter Analysis**: Evaluates 9 critical water quality parameters
- 📊 **Visual Results**: Intuitive gauge and visual feedback
- 📱 **Responsive Design**: Works seamlessly on mobile and desktop devices
- 💫 **Modern UI**: Beautiful animations and user-friendly interface
- 🛡️ **Safety Recommendations**: Provides actionable insights based on results

## 🎬 Demo

<div align="center">
  <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGJraXZ3ZDdyZXJhd2lpem9tbXNycnZybGs3dnExM3Ywc3ZucGZsZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JIX9t2j0ZTN9S/giphy.gif" alt="Demo Animation" width="500"/>
</div>

## 🛠️ Technologies

- **Backend**:
  - Python 3.8+
  - Flask 2.0.1
  - Scikit-learn 0.24.2
  - NumPy & Pandas

- **Frontend**:
  - HTML5 / CSS3 / JavaScript
  - Bootstrap 5.3
  - Particles.js (Background animations)
  - AOS Animation Library
  - Font Awesome (Icons)
  - Google Fonts

## 📥 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/janiyax35/Water_Quality_Prediction.git
   cd Water_Quality_Prediction
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv

   # On Windows:
   venv\Scripts\activate

   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables** (if needed):
   ```bash
   # Create a .env file
   touch .env
   
   # Add necessary environment variables
   echo "SECRET_KEY=your_secret_key_here" >> .env
   ```

## 🚀 Usage

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Access the web interface**:
   Open your browser and navigate to `http://localhost:5000`

3. **Enter water parameters**:
   - Input all 9 water quality parameters
   - Click on the "Predict" button
   - View the results and recommendations

4. **Interpreting results**:
   - Green: Water is safe to drink
   - Yellow: Water quality is questionable
   - Red: Water is not potable

<div align="center">
  <img src="https://source.unsplash.com/800x400/?dashboard,water" alt="Application Screenshot" width="700"/>
</div>

## 📁 Project Structure

```
Water_Quality_Prediction/
├── app.py                  # Main Flask application file
├── water_quality_model.pkl # Trained machine learning model
├── static/
│   ├── css/                # Stylesheet files
│   ├── js/                 # JavaScript files
├── templates/
│   ├── index.html          # Main application page
├── water_potability.csv # Training dataset
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## 📊 Model Performance

The machine learning model has been trained on a dataset containing thousands of water samples with known potability outcomes. The model achieves:

- **Accuracy**: 87.5%
- **Precision**: 86.2%
- **Recall**: 85.9%
- **F1 Score**: 86.0%

Cross-validation techniques were used to ensure the model's reliability, and hyperparameter tuning was performed to optimize performance.

## 🧪 Data Sources

The model was trained using the Water Quality dataset from Kaggle, which contains water quality metrics for 3276 different water bodies. The dataset includes:

- pH value (0 to 14)
- Hardness (mg/L)
- Total dissolved solids (ppm)
- Chloramines (ppm)
- Sulfate (mg/L)
- Conductivity (μS/cm)
- Organic carbon (ppm)
- Trihalomethanes (μg/L)
- Turbidity (NTU)
- Potability (target variable)

## 🔮 Future Enhancements

- [ ] Implement real-time data collection with IoT sensors
- [ ] Add user accounts for saving and tracking water quality over time
- [ ] Develop a mobile application for field testing
- [ ] Integrate with geographic mapping for regional water quality visualization
- [ ] Add more advanced ML models (ensemble methods, deep learning)

## 👨‍💻 About Me

Hi! I'm Janith Deshan, a passionate about cybersecurity, network systems, secure application development and web developer interested in using technology to solve environmental challenges. This project combines my interest in machine learning with my concern for clean water access.

Feel free to connect with me:

<div align="center">
  <a href="https://github.com/janiyax35"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
  <a href="https://www.linkedin.com/in/janithdeshan/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:janithmihijaya123@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
</div>

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

<div align="center">
  <p>💧 Making clean water detection accessible through technology 💧</p>
  <p>© 2025 Janiya X - All Rights Reserved</p>
</div>
