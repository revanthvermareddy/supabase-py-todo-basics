from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client, Client
from supabase_functions.errors import FunctionsRelayError, FunctionsHttpError


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def test_func():
  try:
    resp = supabase.functions.invoke("hello-world", invoke_options={'body':{'name':'Revanth'}})
    return resp
  except (FunctionsRelayError, FunctionsHttpError) as exception:
    err = exception.to_dict()
    print(err.get("message"))

resp = test_func()
print(f'resp: {resp}')