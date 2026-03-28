# study-plan-genarator
# 📚 Personalized Study Plan Generator

## 📌 Project Description

The **Personalized Study Plan Generator** is a simple web-based application that helps students create an effective study plan based on their academic performance.

The system analyzes student marks and available study hours to generate a prioritized study schedule.

---

## 🎯 Objective

To assist students in:

* Identifying strong and weak subjects
* Allocating study time efficiently
* Improving overall academic performance

---

## 📥 Inputs

The application takes the following inputs:

* **Student Marks** (for each subject, out of 70)
* **Available Study Hours**

---

## ⚙️ Processing Logic

1. Subjects are categorized based on marks:

   * **High Priority** → Marks ≥ 55
   * **Medium Priority** → Marks between 35 and 54
   * **Low Priority** → Marks < 35

2. Each priority is assigned a weight:

   * High → 3
   * Medium → 2
   * Low → 1

3. Study hours are distributed proportionally:

   ```
   Subject Hours = (Weight / Total Weight) × Available Hours
   ```

---

## 📤 Output

The system generates:

* 📊 Study plan in tabular format
* ⏱ Allocated study hours per subject
* 🎯 Priority level (High / Medium / Low)
* 🏆 Top performing subject
* ⚠️ Weakest subject

---

## 🛠️ Technologies Used

* **HTML** → Structure
* **CSS** → Styling
* **JavaScript** → Logic & calculations

---

## 🚀 How to Run the Project

1. Download or clone the repository:

   ```
   git clone <your-repo-link>
   ```

2. Open the file:

   ```
   study.html
   ``

3. Enter:

   * Subject marks
   * Study hours

4. Click:

## 📷 Sample Output

| Subject | Marks | Priority | Hours |
| ------- | ----- | -------- | ----- |
| IDS     | 65    | High     | 3.0   |
| SMDS    | 40    | Medium   | 2.0   |
| MEFA    | 30    | Low      | 1.0   |

## 💡 Features

* Dynamic study plan generation
* Simple and user-friendly interface
* Real-time calculation
* Performance-based prioritization
## 📌 Conclusion

This project demonstrates how basic programming concepts can be used to solve real-world problems like time management and study planning.

