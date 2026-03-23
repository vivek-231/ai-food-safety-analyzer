# 🍽️ AI Food Safety Analyzer

An AI-powered web application that predicts the **health risk level caused by food adulteration** using Machine Learning.

---

## 🚀 Features

* 🔍 Predicts food adulteration risk: **Low / Medium / High**
* 🤖 Built using **Random Forest Classifier**
* 🌐 Interactive web app using **Streamlit**
* 📊 Trained on a real-world food adulteration dataset

---

## 🧠 Problem Statement

Food adulteration is a major public health concern. Detecting and prioritizing high-risk cases manually is time-consuming.
This project uses Machine Learning to **automatically predict the severity of health risk**, helping authorities take faster action.

---

## ⚙️ Tech Stack

* Python
* Scikit-learn
* Pandas, NumPy
* Streamlit

---

## 📊 Model Details

* **Algorithm:** Random Forest Classifier
* **Input Features:**

  * Product Name
  * Adulterant
  * Detection Method
  * Action Taken
* **Output:**

  * Health Risk Level (**Low / Medium / High**)

---

## 📁 Project Structure

```
ai-food-safety-analyzer/
│
├── app.py
├── model.pkl
├── food_adulteration_data.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📸 Demo

*(Add your app screenshot here)*

Example:

```
![App Screenshot](screenshot.png)
```

---

## 🎯 Use Case

This system can assist:

* 🏢 Food Safety Authorities (like FSSAI)
* 🧪 Food Inspectors
* 🏭 Quality Control Teams

👉 To **identify and prioritize high-risk adulteration cases efficiently**

---

## 🔮 Future Improvements

* Dropdown inputs with real food names
* Image-based adulteration detection (CNN)
* Mobile app integration
* Dashboard with analytics

---

## 👨‍💻 Author

**Vivek Vardhan**
GitHub: https://github.com/vivek-231

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
