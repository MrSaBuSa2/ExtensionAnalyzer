from magic_db import MAGIC_SIGNATURES
from extension_map import EXTENSION_MAP

def read_file_signature(file_path, num_bytes=16):
    with open(file_path, 'rb') as f:
        return f.read(num_bytes)

def analyze_file_signature(file_path):
    signature = read_file_signature(file_path)

    for magic, description in MAGIC_SIGNATURES.items():
        if signature.startswith(magic):
            return description

    return "Unknown file type"

def compare_file_extension(file_path):
    detected = analyze_file_signature(file_path)
    ext = file_path.split('.')[-1].lower()
    claimed = EXTENSION_MAP.get(ext, "Unknown file type")

    return {
        "file": file_path,
        "extension_claim": claimed,
        "detected_header": detected,
        "match": claimed == detected
    }
