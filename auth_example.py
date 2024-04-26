from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client, Client
from gotrue.errors import AuthApiError

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

users_email: str = input("Enter your email: ")
users_password: str = input("Enter your password: ")
# user = supabase.auth.sign_up({ "email": users_email, "password": users_password })
# print(f'user: {user}')

data = supabase.table("todos").select("*").execute()
print(f'Data before sign-in: {data}')

user = None
try:
    user = supabase.auth.sign_in_with_password({ "email": users_email, "password": users_password })
    # print(f'user: {user}')
except AuthApiError as e:
    print(f'Login failed: {e}')

data = supabase.table("todos").select("*").execute()
print(f'Data after sign-in: {data}')

# print(f'user.session.access_token: {user.session.access_token}')

supabase.auth.sign_out()