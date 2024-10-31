# app.py
from fastapi import FastAPI
from dotenv import load_dotenv
import os
import asyncio
import asyncssh
import nmap

# .env dosyasını yükleyerek ortam değişkenlerini ayarlıyoruz
load_dotenv()
username = os.getenv("SSH_USERNAME")
password = os.getenv("SSH_PASSWORD")

app = FastAPI()

# Belirtilen ağ aralığında IP adreslerini tarayan bir fonksiyon
async def scan_network():
    scanner = nmap.PortScanner()
    # Tarama hızını artırmak için -T4 argümanını ekliyoruz
    scanner.scan('192.168.58.0/24', arguments='-p 22 --open -T4')  
    ip_list = [host for host in scanner.all_hosts() if scanner[host].has_tcp(22)]
    return ip_list

# Belirtilen IP adresine SSH bağlantısı açan bir fonksiyon
async def ssh_connect(ip):
    try:
        # Anahtarın otomatik olarak eklenmesini sağlıyoruz
        async with asyncssh.connect(ip, username=username, password=password, known_hosts=None) as conn:
            print(f"SSH bağlantısı kuruldu: {ip}")
            # Burada gerekli komutları çalıştırabilirsiniz, örneğin:
            result = await conn.run('echo Merhaba SSH', check=True)
            print(f"{ip} sonucu: {result.stdout}")
    except asyncssh.Error as e:
        print(f"SSH bağlantısı başarısız: {ip}, Hata: {e}")

# Ana fonksiyon, tarama ve bağlantıları yöneten
async def main():
    # Ağı tarıyoruz
    print("Ağı tarıyoruz...")
    ip_list = await scan_network()
    print(f"Bulunan IP adresleri: {ip_list}")
    
    # Tüm IP adreslerine eşzamanlı olarak SSH bağlantısı açıyoruz
    if ip_list:
        ssh_tasks = [ssh_connect(ip) for ip in ip_list]
        await asyncio.gather(*ssh_tasks)

@app.get("/scan")
async def scan():
    """Ağ taraması başlatan endpoint."""
    await main()
    return {"message": "Ağ taraması tamamlandı."}

# Programı çalıştırıyoruz
if __name__ == '__main__':
    asyncio.run(main())