# Calculate API
### REST API service for calculating the cost of insurance depending on the type of load and the declared value.

---

## Setup:
1. Change credentials in config.py:
``` python
 POSTGRES_USERNAME = 'postgres'  # Your postgres username
 POSTGRES_PASSWORD = 'postgres'  # Your postgres password
 POSTGRES_DB = 'postgres'  # Database name
```
2. Clone this repository:
``` bash
 git clone https://github.com/schr1k/CalculateApi.git .
``` 
3. Install all necessary packages:
``` bash
 pip install -r requirements.txt
```
4. Build docker image:
``` bash
 docker-compose build
```
5. Run docker container:
``` bash
 docker-compose up -d
```

## Usage:
- Send json package to http://somedomain/rate to update insurance cost.
### Example:
```python
import requests

data = {
    "2020-08-01": [
        {
            "cargo_type": "Glass",
            "rate": "0.04"
        },
        {
            "cargo_type": "Other",
            "rate": "0.01"
        }
    ],
    "2020-08-02": [
        {
            "cargo_type": "Glass",
            "rate": "0.035"
        },
        {
            "cargo_type": "Other",
            "rate": "0.015"
        }
    ]
}

response = requests.post(url='http://somedomain/rate', json=data)
print(response.json())
```
- Send http request to http://somedomain/calculate to calculate insurance cost.
### Example: 
```python
import requests

response = requests.get(url='http://somedomain/calculate',
                        params={'cargo_type': 'Glass',
                                'value': 100,
                                'order_date': '2020-07-01'})
print(response.json())
```
