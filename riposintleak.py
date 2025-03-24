import requests, base64, json, os, pyperclip

def generate_key():
    values = ["3rqf", "W4ET", "21E2", "241D", "qfw", "GW34", "EG", "52", "AA", "D32", "1", "x", "qw", "G"]
    order = [11, 0, 4, 1, 11, 2, 3, 7, 9, 5, 8, 6, 13, 10]
    reordered = [values[i] for i in order]
    reordered.insert(3, "Z")
    reordered.insert(7, "Y")
    reordered.insert(15, "X")
    return "".join(ch for ch in reordered if ch not in ["Z", "Y", "X"])

def decode_encrypted_data(encrypted_str: str, token: str):
    try:
        if len(encrypted_str) % 4:
            encrypted_str += '=' * (4 - len(encrypted_str) % 4)
        decoded = base64.b64decode(encrypted_str).decode('utf-8')
        result = ""
        token_len = len(token)
        key_len = len(generate_key())
        for i in range(len(decoded)):
            token_val = ord(token[i % token_len]) - 32
            key_val = ord(generate_key()[i % key_len]) - 32
            offset = (token_val + key_val) % 95
            char = chr((ord(decoded[i]) - 32 - offset + 95) % 95 + 32)
            result += char
        return json.loads(result)
    except Exception as ex:
        return f"Decoding failed: {str(ex)}"

def Username_Search(auth_token: str, username: str ):
    params = {
        "query": f"{username}",
        "type": "username",
        "search_option": "quick",
        "page": 1,
        "stealerlogs": "true",
        "dbleaks": "true",
        "dbleaks2": "true",
        "from_date": "false",
        "to_date": "false",
        "country": "false",
        "result_id": "false",
        "sort": "desc"
    }

    headers = {
        "Host": "osintleak.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
        "Accept": "*/*",
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
        "Referer": "https://osintleak.com/dashboard/search",
        "DNT": "1",
        "Connection": "keep-alive"
    }

    response = requests.get("https://osintleak.com/api/v1/search/", headers=headers, params=params)

    if response.status_code == 200:
        json_data = response.json()
        encrypted_data = json_data.get("data")
        if encrypted_data:
            decrypted_data = decode_encrypted_data(encrypted_data, auth_token)
            pyperclip.copy(decrypted_data)
            if isinstance(decrypted_data, dict):
                with open(os.getcwd() + "\\decrypted_output.json", "w", encoding="utf-8") as f:
                    json.dump(decrypted_data, f, indent=2)
                print("Decrypted response saved to decrypted_output.json")
            else:
                print(f"Decoding error: {decrypted_data}")
        else:
            print("No data found in response.")
    else:
        print(f"Request failed: {response.status_code}")
        print(response.text)

token = "" #token here
username = input("Enter The Username: ")
Username_Search(token, username)