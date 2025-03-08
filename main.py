import asyncio
from introspective_agent import get_introspective_agent

introspective_agent = get_introspective_agent()

# Kullanıcıdan Sorgu Alma ve Çalıştırma
print("Galeri Asistanına hoş geldiniz. Çıkış yapmak için 'exit' yazın.")
while True:
    user_input = input("Komut: ")
    if user_input.lower() == "exit":
        break

    # Asenkron olarak çalıştır
    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(introspective_agent.achat(user_input))
    print(response)

