import os
from supabase import create_client

url = "https://ezoxfuxdtqgykhxoteii.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV6b3hmdXhkdHFneWtoeG90ZWlpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE1MzA2NTMsImV4cCI6MjA5NzEwNjY1M30.ZOV6bRblkLxuWIIfcXVBsTHJGx2PSGZIsmuZyzzumkA"

client = create_client(url, key)
response = client.table("messages").select("*").order("created_at", desc=True).limit(10).execute()
for msg in reversed(response.data or []):
    print(f"[{msg.get('created_at')}] {msg.get('role').upper()}: {msg.get('content')}")
    if msg.get('generated_code'):
        print(f"CODE:\n{msg.get('generated_code')}")
    print("-" * 50)
