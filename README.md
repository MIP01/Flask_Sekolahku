# Description
This API project using Flask framework, designed to course registration system with JWT authentication for user access and Marshmallow for input validation. Students can browse courses, register securely, and avoid errors like duplicates or overcapacity. Admins can manage courses and monitor usage, ensuring an efficient registration process.

# How to setup
1. create .env and insert
    *   ```
        DATABASE_URL=mysql://your-username:your-password@localhost/your-db-name 
        ```
    *   ```
        JWT_SECRET_KEY = your-secret-key
        ```
2. install dependencies
    ```
    pip install -r requirements.txt
    ```
3. apply changes to the database
    ```
    flask db upgrade
    ```
