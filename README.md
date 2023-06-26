# Ukraine Alarms API

![Ukraine Alarms API Logo](https://raw.githubusercontent.com/MixFix7/Ukraine-Alarms-Api/main/apiLogo.png)

## Description

Ukraine Alarms API is a Django-based API that provides real-time information about air pollution alerts in Ukraine. It serves as a reliable data source for obtaining up-to-date information on air pollution levels and current air alarm notifications in all regions of Ukraine.

## Features

- Speed of information provision
- Accuracy of alarm information
- Easy integration with your applications or services.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/ukraine-alarms-api.git
   ```

2. Navigate to the project directory:

   ```shell
   cd ukraine-alarms-api
   ```

3. Create and activate a virtual environment:

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

5. Run the database migrations:

   ```shell
   python manage.py migrate
   ```

6. Start the development server:

   ```shell
   python manage.py runserver
   ```

7. The API will be accessible at: `http://localhost:8000/`

## Usage

The API provides the following endpoints:

- `GET /api/ukraineAlarms/`: Get current air alarm notifications in all regions of Ukraine.

## Examples

### Getting current air alarm notifications

Request:
```shell
GET /api/ukraineAlarms/
```

Response:
```json
[
    {
        "id": 1,
        "Region": "Запорізька",
        "Region_en": "Zaporizhzhya",
        "Alarm": false,
        "datetime": "2023-06-26 22:41:31.307666"
    },
   
    {
        "id": 2,
        "Region": "Донецька",
        "Region_en": "Donetsk",
        "Alarm": false,
        "datetime": "2023-06-26 22:41:31.326398"
    },
   
    {
        "id": 3,
        "Region": "Харківська",
        "Region_en": "Kharkiv",
        "Alarm": false,
        "datetime": "2023-06-26 22:41:31.341349"
    },
```


## Conclusion

This README provides an overview of the Ukraine Alarms API and details on its installation and usage. You can utilize this API to obtain updated information on air pollution levels and air alarm notifications in Ukraine.

## Important

There should be a file in the API that receives alarm data, for my safety, this file is not there.
