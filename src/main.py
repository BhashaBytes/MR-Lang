import subprocess

mapping = {
    "दाखवा": "print", "dakhava": "print",
    "घ्या": "input", "ghya": "input",
    "जर": "if", "jar": "if",
    "अन्यजर": "elif", "anyajar": "elif",
    "अन्यथा": "else", "anyatha": "else",
    "साठी": "for", "sathi": "for",
    "जोपर्यंत": "while", "joparyant": "while",
    "परिभाषक": "def", "paribhashakara": "def",
    "वर्ग": "class", "varg": "class",
    "परतद्या": "return", "paratdya": "return",
    "थांबा": "break", "thamba": "break",
    "चालू ठेवा": "continue", "chalutheva": "continue",
    "आयात करा": "import", "aayatkara": "import",
    "पासून": "from", "pasun": "from",
    "म्हणून": "as", "mhanun": "as",
    "सोबत": "with", "sobat": "with",
    "प्रयत्न करा": "try", "prayatnakara": "try",
    "शिवाय": "except", "sivay": "except",
    "शेवटी": "finally", "shevti": "finally",
    "खरे": "True", "khare": "True",
    "खोटे": "False", "khote": "False",
    "काहीनाही": "None", "kahinahi": "None",
    "किंवा": "or", "kinva": "or"
}

def translate(code: str) -> str:
    for mr, py in mapping.items():
        code = code.replace(mr, py)
    return code

with open("test.mr", "r", encoding="utf-8") as f:
    mr_code = f.read()

python_code = translate(mr_code)

with open("temp.py", "w", encoding="utf-8") as f:
    f.write(python_code)

subprocess.run(["python3", "temp.py"])
