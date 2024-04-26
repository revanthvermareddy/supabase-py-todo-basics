from dotenv import load_dotenv
load_dotenv()

import os
from datetime import datetime, timedelta, timezone
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

# 1. select operation
# data = supabase.table("todos").select("*").execute()
# data = supabase.table("todos").select("id, name").execute()
# data = supabase.table("todos").select("id, name").eq("name", "Item 1").execute()

# 2. insert operation
# created_at = datetime.now(timezone.utc) - timedelta(hours=3)
# data = supabase.table("todos").insert({"name":"Item 3", "created_at": str(created_at)}).execute()
# print(f'inserted data: {data}')
# data = supabase.table("todos").select("*").execute()
# print(f'data: {data}')

# 3. updated operation
# data = supabase.table("todos").update({"name": "Item 4"}).eq("name", "Item 3").execute()
# print(f'updated data: {data}')

# 4. delete operation
# data = supabase.table("todos").delete().eq("name", "Item 4").execute()
# print(f'deleted data: {data}')