import json
import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

title_site = "weather"


URL = "https://open-weather13.p.rapidapi.com/city/landon/EN"

headers = {
	"x-rapidapi-key": "5b93debdaamsh2e5a6f40014819dp1bc16fjsn00adc9661c18",
 	"x-rapidapi-host": "open-weather13.p.rapidapi.com"
 }

response = requests.get(URL, headers=headers, timeout=3000)

@app.route("/data", methods=["GET"])
def get_data():
    response = requests.get(URL, headers=headers, timeout=3000)
    response.raise_for_status()  
    data = response.json()
    return render_template('data.html', data=data)




if __name__ == "__main__":
    app.run(debug=True)



# with open("data_example.json", "w", encoding="utf-8") as file:
#     json.dump(
#         response.json(),
#         file,
#         indent=4,
#     )
# print(response.json())

# with open("data_example.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
# print(f"{data=}")