import requests, json, os


contract_address = "0x29d2bcf0d70f95ce16697e645e2b76d218d66109"
API_KEY = os.getenv("API_KEY")

req = requests.get(
    url="https://api.etherscan.io/v2/api",
    params={
        "apikey": API_KEY,
        "chainid": 1,
        "module": "contract",
        "action": "getsourcecode",
        "address": contract_address
    }
)

project_name = req.json()["result"][0]["ContractName"]
os.mkdir(f"test/{project_name}")
# print(project_name)

data = json.loads(req.json()["result"][0]["SourceCode"][1:-1])

for key, item in data["sources"].items():
    source_code = item["content"]
    filename = key.split("/")[-1]
    path = key.replace(f"/{filename}", "")
    # print(path)
    # print(filename)
    # print(source_code)
    os.makedirs(f"test/{project_name}/{path}", exist_ok=True)
    with open(f"test/{project_name}/{path}/{filename}", "w") as f:
        f.write(source_code)
        f.close()
