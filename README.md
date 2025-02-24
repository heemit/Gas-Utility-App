# Gas Utility App

This Django-based application allows users to manage gas utility services. Users can request services, track their service status, view past requests, and more. The app includes features such as file uploads, user authentication, and service request history tracking.

## Features

- **Service Requests**: Create, edit, and manage gas utility service requests.
- **User Authentication**: Secure login, registration, and logout functionality are provided for users.
- **Service Tracking**: Track the status of each service request (e.g., pending, in-progress, resolved).
- **File Uploads**: Attach files such as images or PDFs to service requests.
- **History Tracking**: Automatically track changes to service requests with django-simple-history.
- **Responsive Design**: The app is mobile-friendly, with a modern and clean interface powered by Bootstrap.

## Requirements

Before starting, ensure that you have the following installed:

- **Python 3.x**: The project is built with Python 3.
- **Django>=5.0**: The Django framework for web development.
- **Additional Libraries**:
  - `django-simple-history==3.0.0`: To track changes to models.
  - `django-model-utils==4.1.1`: For additional model utilities.
  - `whitenoise==6.5.0`: To serve static files in production.
  - `gunicorn==23.0.0`: A WSGI HTTP server for running the app.

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2. **Create a virtual environment**

    If you don't have a virtual environment already, create one:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**

    Install the required dependencies listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**

    Run the migrations to set up the database schema:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for admin access)**

    To access the Django admin panel, create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create a superuser.

6. **Run the development server**

    Start the development server:

    ```bash
    python manage.py runserver
    ```

    Access the site by going to:

    ```
    http://127.0.0.1:8000/
    ```

    The admin panel is available at:

    ```
    http://127.0.0.1:8000/admin/
    ```

7. **Access the website**

    Go to `http://127.0.0.1:8000/` to view the homepage and browse the blogs.

## Images

![image](https://github.com/user-attachments/assets/0e336e7b-fd5f-4d3e-8582-a0dd0f3ce0fd)

![image](https://github.com/user-attachments/assets/e056a481-c7e5-4134-b728-544083c37ca2)

![image](https://github.com/user-attachments/assets/d2317cf1-5273-40c8-b5f4-9fa82644504e)

![image](https://github.com/user-attachments/assets/256f2c97-08bd-4e08-bfa7-12f94f22f6a8)

![image](https://github.com/user-attachments/assets/b01a590c-73f3-4e5d-af99-3eac8e9c183c)

![image](https://github.com/user-attachments/assets/e2a69584-f3a9-4fe2-8d92-5785f96997ea)

![image](https://github.com/user-attachments/assets/94377ce1-b09e-4e4e-a876-8cb8e7508f15)

![image](https://github.com/user-attachments/assets/da252865-8364-451e-9df9-604ed2140463)

![image](https://github.com/user-attachments/assets/1edddf46-e6e2-420f-a00d-457709899796)

![image](https://github.com/user-attachments/assets/b44fb762-b7d5-4a35-bea2-1c71126739c2)

![image](https://github.com/user-attachments/assets/6cf9221d-efb4-4ec6-8576-4a071ee2a309)

![image](https://github.com/user-attachments/assets/cdb77d84-f9c5-4c07-819f-31befdeaf5b3)

![image](https://github.com/user-attachments/assets/ada43980-7d0f-43c0-91ea-529fd7ffefe4)

![image](https://github.com/user-attachments/assets/962d1122-82a1-49be-9a26-1233b925f7ba)
