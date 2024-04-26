from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

bucket_name: str = "image-bucket"

# 1. get public signed url
# data = supabase.storage.from_(bucket_name).get_public_url("7-eleven.webp")
# print(f"data: {data}")

# 2. upload image
data = supabase.storage.from_(bucket_name).upload(file="dave.webp", path="dave.webp", file_options={"content-type": "image/jpeg"})
print(f"data: {data}")