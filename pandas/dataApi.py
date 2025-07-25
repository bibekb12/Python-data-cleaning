import requests as rq


def demo_data():
    try:

        api_key = "B6MhurhAH9A9EyrF3sNH8qIshKTbfWIXteuNXZVI"
        url = (
            "https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=100&api_key="
            + api_key
        )

        response = rq.get(url)
        result = response.json()

        return {"data": result, "header": response.headers}
    except Exception as e:
        return {"error": str(e)}
