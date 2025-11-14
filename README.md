# facial-emotional-detection

## Setup Instructions

### 1- Clone the repository:

```shell
  git clone git@github.com:codehass/facial-emotional-detection.git
```

### 2- database configuration:

- Create a `.env` file in the root directory of the project.
- Copy the content of the `.env.example` file into the newly created `.env` file and replace it with your real data.

  ```shell
  cp .env.example .env
  ```

### 3- Install the dependencies:

- For python version I used 3.11.14
- You can use pyenv to manage python versions.
- Make sure to install python 3.11.14 using pyenv:
- Use the version locally and create a virtual environment:

  ```shell
    cd facial-emotional-detection
    pyenv local 3.11.14
  ```

  ```shell
    python -m venv venv
    source venv/bin/activate
  ```

- Install the required packages:

  ```shell
    pip install -r requirements.txt
  ```

### 4- Run the application:

- Start the application using the following command:

  ```shell
    cd backend
    uvicorn backend.main:app --reload
  ```

### 5- Access the application:

- Open your web browser and navigate to `http://localhost:8000/docs`

### 6- Run Tests:

- To run the tests, use the following command:

  ```shell
    python -m unittest discover -s tests
  ```
