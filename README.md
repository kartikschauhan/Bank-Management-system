# 🏦 Bank Management System

Welcome to the **Bank Management System**! This is a simple banking system built using **Python** and **MySQL**, allowing users to manage their accounts seamlessly. 💰✨

---

## 📌 Features

✅ **Open a New Account** – Create an account with a unique account number. 🔑  
✅ **Check Balance** – View the available balance in your account. 💵  
✅ **Deposit Money** – Add money to your account. 📥  
✅ **Withdraw Money** – Debit money from your account. 📤  
✅ **Deactivate Account** – Permanently delete your account. ❌  
✅ **Admin Mode** – The bank manager can handle multiple customers. 👨‍💼

---

## 🛠️ Technologies Used

- **Python** 🐍 – For backend logic and user interaction
- **MySQL** 🗄️ – For storing customer data
- **MySQL Connector** 🔗 – To connect Python with MySQL

---

## 🚀 How to Run the Project

1. **Install MySQL Connector**
   ```sh
   pip install mysql-connector-python
   ```

2. **Create MySQL Database**
   ```sql
   CREATE DATABASE Bank_Management_system;
   USE Bank_Management_system;
   CREATE TABLE user (
       acc_no INT PRIMARY KEY,
       name VARCHAR(100),
       phone_no BIGINT,
       amount DOUBLE
   );
   ```

3. **Run the Python Script**
   ```sh
   python bank_system.py
   ```

---

## 📷 Screenshots
![img](https://github.com/user-attachments/assets/be093e97-8293-48b7-bc10-f16fd4615226)

---

## 📞 Contact Information

👤 **Kartik Singh Chuahan**  
📧 **Email:** kartikrajput4466@gmail.com  
🔗 **LinkedIn:** [Kartik Singh Chauhan](https://www.linkedin.com/in/kartik-chauhan-linkdin/)  

---

### 🌟 If you like this project, don't forget to ⭐ it!

Happy Coding! 🚀🎉

