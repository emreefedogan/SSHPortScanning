# FastAPI SSH Network Scanner

Bu proje, FastAPI kullanarak belirli bir ağ aralığında IP adreslerini tarayan ve açık olan IP adreslerine eş zamanlı SSH bağlantısı açan bir uygulamadır. Uygulama, `nmap` kütüphanesini kullanarak ağ taraması yapar ve `asyncssh` kütüphanesi ile SSH bağlantıları kurar.

## Gereksinimler

- Python 3.7 veya üzeri
- Aşağıdaki Python kütüphaneleri:
  - fastapi
  - uvicorn
  - asyncssh
  - python-nmap
  - python-dotenv

## Kurulum

1. **Gereksinimleri Yükleyin**:
   Aşağıdaki komutu kullanarak gerekli kütüphaneleri yükleyin:

   ```bash
   pip install fastapi uvicorn asyncssh python-nmap python-dotenv
   ```

   Alternatif olarak, `requirements.txt` dosyasını oluşturabilirsiniz. Aşağıdaki içeriği `requirements.txt` dosyasına ekleyin:

   ```plaintext
   fastapi
   uvicorn
   asyncssh
   python-nmap
   python-dotenv
   ```

   Ardından, aşağıdaki komutla bağımlılıkları yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

2. **.env Dosyasını Oluşturun**:
   Proje dizininde bir `.env` dosyası oluşturun ve SSH kullanıcı adı ve şifresini ekleyin:

   ```plaintext
   SSH_USERNAME=your_username
   SSH_PASSWORD=your_password
   ```

   `your_username` ve `your_password` kısımlarını kendi SSH kimlik bilgilerinizle değiştirin.

## Kullanım

1. **Uygulamayı Başlatın**:
   Aşağıdaki komutu kullanarak uygulamayı başlatın:

   ```bash
   uvicorn app:app --reload
   ```

2. **Ağ Taramasını Başlatın**:
   Tarayıcınızda `http://127.0.0.1:8000/scan` adresine giderek ağ taramasını başlatın. Uygulama, belirtilen ağ aralığında açık olan IP adreslerini tarayacak ve bu adreslere eş zamanlı olarak SSH bağlantıları açacaktır.

## Açıklama

- **scan_network**: Belirtilen ağ aralığında IP adreslerini tarar ve açık olanları döndürür.
- **ssh_connect**: Açık olan IP adresine SSH bağlantısı açar ve belirli bir komutu çalıştırır.
- **main**: Ağı tarar ve bulunan IP adreslerine eş zamanlı olarak SSH bağlantıları açar.
- **/scan**: Ağ taramasını başlatan HTTP GET endpoint'idir.

## Güvenlik Uyarısı

Anahtarın otomatik olarak eklenmesini sağlamak için `known_hosts=None` kullanılmıştır. Bu, güvenlik açısından riskli olabilir. Gerçek uygulamalarda, sunucuların anahtarlarını güvenilir bir şekilde yönetmek önemlidir.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır.
