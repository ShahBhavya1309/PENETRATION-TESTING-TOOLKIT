import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_forms(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for i in form.find_all(["input", "textarea"]):
        name = i.attrs.get("name")
        if name:
            inputs.append({"name": name})
    return {"action": action, "method": method, "inputs": inputs}

def submit_form(form, url, payload):
    target = urljoin(url, form["action"])
    data = {i["name"]: payload for i in form["inputs"]}
    if form["method"] == "post":
        return requests.post(target, data=data)
    return requests.get(target, params=data)

def scan(url):
    print(f"\n[+] Scanning for vulnerabilities: {url}")
    forms = get_forms(url)
    for form in forms:
        f = get_form_details(form)
        res_xss = submit_form(f, url, "<script>alert(1)</script>")
        if "<script>alert(1)</script>" in res_xss.text:
            print("[!!] XSS found!")

        res_sql = submit_form(f, url, "' OR '1'='1")
        if any(x in res_sql.text.lower() for x in ["error", "sql", "query"]):
            print("[!!] SQL Injection found!")
