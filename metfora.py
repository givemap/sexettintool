import os
print("\033[95m")
os.system("clear")
srum = open("surum.txt")
surum = srum.read()
print('''
                   /|_
                  /   |_
                 /     /     __  __      _    __                 	
                /      >    |  \/  | ___| |_ / _| ___  _ __ __ _ 	
               (      >	    | |\/| |/ _ \ __| |_ / _ \| '__/ _` |
              /      /	    | |  | |  __/ |_|  _| (_) | | | (_| |
             /     /	    |_|  |_|\___|\__|_|  \___/|_|  \__,_|
            /      /
         __/      \_____   Yaptığınız ve yapacağınız her şeyden siz sorumlusunuz
        /'             |	 hiçbir şekilde sorumluluk kabul edilmez.
         /     /-\     /
        /      /  \--/	    1-) Kurulum (bazı durumlarda kök kullanıcı gerektirir)
       /     /
      /      /		    2-) İletişim
     (      >
    /      >		    3-) Aracı güncelle
   /     _|
  /  __/		    4-) Bu dizine aracı yükle
 /_/
			    5-) Bu dizinden aracı sil
			   
			    6-) Sexettintool'a giriş yap

                            7-) Bu araç içindekiler ne işe yarıyor?
''')

metfora = input("Hangisini seçiyorsunuz? ")


import subprocess
import sys

# Python paketleri
python_packages = [
    'requests',
    'opencv-python',
    'opencv-python-headless',  
    'numpy',
    'selenium',
    'youtube_dl',  
    'yt_dlp',
    'pynput',
    'phonenumbers',
    'geocoder',
    'pyzipper',
    'beautifulsoup4', 
    'pyautogui',
    'telethon',
    'tensorflow',
    'joblib',
    'pillow',  
    'exifread',
    'scikit-learn',  
    'scapy',  
    'pybluez',  
    'moviepy', 
    'paramiko',  
]

# APT paketleri
apt_packages = [
    'chkrootkit',
    'zip',
    'unzip',
    'neofetch',
    'figlet',
    'mpv',
    'searchsploit',
    'wafw00f',
    'ncrack',
    'nmap',
    'metasploit-framework',
    'nikto',
    'lynis',
    'crunch',
    'ike-scan',
    'macchanger',
    'net-tools',
    'wpscan',
    'sqlmap',
    'hydra',
    'aircrack-ng',
    'php',
    'pyinstaller',
]

def install_python_package(package):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    except subprocess.CalledProcessError:
        print(f"\033[91m{package} paketi yüklenemedi\033[97m")

def install_apt_package(package):
    try:
        subprocess.check_call(['sudo', 'apt-get', 'install', '-y', package])
    except subprocess.CalledProcessError:
        print(f"\033[91m{package} uygulaması yüklenemedi\033[97m")

def yukleme_baslat():
    for package in python_packages:
        print(f"\033[94m{package} yükleniyor...\033[97m")
        install_python_package(package)
    
    for package in apt_packages:
        print(f"\033[94m{package} yükleniyor...\033[97m")
        install_apt_package(package)

if(metfora=="1"):
	yukleme_baslat()


elif(metfora=="2"):
	print('''
Telegram = @furkande
Discord = Sexettin
Telegram Genel Kanal = t.me/sexettin
Instagram = Sexettin
Youtube = Sexettin
Discord Sunucusu = https://discord.com/invite/DTN5RSvYvw
Github = sexettin78
	''')

elif(metfora=="3"):
	os.system("git pull")
	os.system("git fetch")


elif(metfora=="4"):
	os.system("cd ..")
	os.system("git clone https://github.com/sexettin78/sexettintool.git")

elif(metfora=="5"):
	print("\033[91mBu dizindeki araç ve ilgili her şey kaldırılacak")
	sec = input("Kaldırmak istediğinize emin misiniz? y/n ")
	if(sec=="y"):
		os.system("cd ..")
		os.system("rm -rf sexettintool")
	elif(sec=="n"):
		print("İşlem iptal edildi")

elif(metfora=="6"):
	os.system("clear")
	os.system("python3 sexettintoolsv"+surum+".py")

elif metfora=="7":
    print('''
Exploit Tarama Otomasyonu: Searchsploit kullanarak sizin için exploit tarama otomasyonu gerçekleştirir.

Güvenlik Duvarı Tespit Aracı: wafw00f ile güvenlik duvarı tespiti yapar

Kaba Kuvvet Saldırısı Aracı: 11 farklı seçenek sunar. İstediğiniz bağlantı türüne ncrack ile kaba kuvvet otomasyonu gerçekleştirebilirsiniz.

Port Tarama Aracı: Size sunulan 3 farklı tarama seçeneğini çalıştırabilirsiniz. nmap ile çalışır.

Rootkit Tarama Aracı: chkrootkit ile rootkit taraması başlatır.

Trojan Oluşturma Aracı: Size sunulan 6 farklı payload ile msfvenom otomasyonu sağlar.

Zaafiyet Analiz Aracı: nikto ile zaafiyet analizi yapar.

Zaafiyet Analiz Aracı 2: lynis ile zaafiyet analizi yapar.

Wordlist Oluşturma Aracı: crunch ile wordlist oluşturur. Sizden gerekli bilgileri alır ve uygun dosyayı verir.

Hedef Ip Vpn Kontrol Aracı: ike-scan kullanarak hedef ip adresini kontrol eder.

Mac Adresi Değiştirme Aracı: mac-changer ile 3 farklı mac değiştirme seçeneğine erişebilirsiniz.

Wordpress Tarama Aracı: wpscan ile kolayca wordpress eklenti, tema, yönetici ismi veya da hızlı tarama gerçekleştirebilirsiniz.

Derleme Aracı: belirttiğiniz python dosyasının kodlarına başkasının erişememesi için dosyayı derler. 

Veritabanı Çalma Aracı: sqlmap otomasyonu ile veritabanı çalma işlemi gerçekleştirir.

Etkinleştirme Kodu Oluşturucuları: Discord, Pubg, Google Play için etkinleştirme kodları oluşturmaya çalışır.

Şifre Oluşturucu: Belirlediğiniz uzunlukta, istediğiniz harfleri kullanarak güçlü şifreler oluşturur.

Şifre Oluşturucu v2 : Belirlediğiniz uzunlukta güçlü şifreler oluşturur.

Kullanıcı Adı ile Hesap Bulma (Statik): Statik olarak kullanıcı adından sosyal medya hesabı taraması yapar.

T¢ Son 2 Hane Bulma: Tc algoritmasını kullanarak matematiksel işlemlerle son 2 hane bulur.

An0nimSMS: Belirlediğiniz mesajı belirttiğiniz numaraya (Türkiye için kapalı) gönderir

Telefon Numarasından Şehir Bulma: Yurtdışı numaralarının bağlı olduğu şehri gösterir.

Panelsiz Mail (Statik): Rastgele, yönetim paneli olmayan mail oluşturur.

Admin Panel Tara (Statik): Girilen sitenin admin panelinin sahip olabileceği linkleri gösterir.

Spambot: Belirlediğiniz kelimeyi, belirlediğiniz kadar yazar. Örneğin istediğiniz kişiye art arda belirlediğiniz mesajı gönderebilirsiniz

Ip Adresinden Bilgi Topla: Belirttiğiniz ip adresine bağlı bilgileri gösterir.

UltraBot: Görüntüleme, giriş hilesi için kullanılabilir. Belirlediğiniz siteye art arda giriş yaparak izlenme/indirme arttırır.

Oto tıklayıcı: Belirlediğiniz saniye aralıklarıyla oto tıklama gerçekleştirir.

Sms Bomb: Belirlediğiniz numaraya farklı sms servislerinden art arda mesaj gönderir.

Zip Şifre Kırıcı: Zip dosyasının şifresini sözlük saldırısı ile kırar.

Wordlist Oluşturucu: Sexettintool kendi wordlist oluşturma algoritması.

Oltalama Araçları: Instagram ve ip adresi yakalamak için oltalama sunucusu oluşturur. Kullanıcının girdiği veriler size gelir.

Instagram Bot: Hesaplar dosyasına girdiğiniz hesaplar üzerinden topluca bir kişiyi takip ettirmek, takipten çıkartmak için kullanılabilir.

Sitedeki Linkleri Çekme: Belirtilen site üzerindeki bağlantıları listeler.

Sitedeki Yazıları Çekme: Belirtilen site üzerindeki paragrafları listeler.

Sitedeki Resim Yollarını Çekme: Belirtilen site üzerindeki resim yollarını listeler.

Dosyalar Arası Veri Karşılaştırma: Belirtilen dosyaların birbiri ile tamamen aynı olup olmadığını kontrol eder.

StnCrypt: Python veya html için değiştirme mantığıyla basit bir şifreleme yapar.

Dosya İçerisinde Arama İşlemleri (Linux): Dosya içerisinde belirlediğiniz kelimeyi/cümleyi ve ona bağlı metinleri listeler.

Admin Panel Bulucu (Dinamik): Belirtilen sitenin admin panelini, en çok tercih edilen admin panel yollarını deneyerek bulmaya çalışır.

Link Kısaltma Servisleri: is.gd veya da tinyurl ile istediğiniz linki kısaltır.

Whois Sorgulama: Belirtilen sitenin whois sorgulama sonucunu gösterir.

SSL Analizi: Belirtilen sitenin ssl sertifikası bilgilerini gösterir.

Rastgele İnsan Verisi Üret: api kullanarak rastgele insan verisi üretir

Rastgele İnsan Gönderisi Üret: api kullanarak rastgele insan gönderisi oluşturur.

Dns Bilgi Toplama: Belirtilen domain adresinin dns bilgilerini gösterir.

ISBN Numarasından Bilgi Toplama: ISBN numarası üzerinden kitap bilgisi toplar.

Mailin Geçerliliğini Kontrol Etme: api kullanarak belirtilen mail adresini dinler ve geçerliliğini kontrol eder.

Ip Adresi Zafiyet Analizi: api kullanarak ip adresi üzerinden zafiyet analizi gerçekleştirir.

SSH Brute Force: Belirtilen ssh sunucusuna sözlük saldırısı uygular.

Wifi Port Tarayıcı: Wifi üzerinde port taraması yapar

Anormal DNS Tespit Edici: Ağınız üzerinde belirlediğiniz istek sınırını aşan kullanıcıları listeler.

Dns Yönlendirici: Belirlediğiniz ip adresine dns yönlendirme saldırısı yapar. Aynı zamanda ağı dinleyebilirsiniz.

Wifi Dinleyicisi 1: Ağ üzerinde devamlı dinleme işlemi uygulayarak paket yönlendirmelerini listeler

Wifi Dinleyicisi 2: İlk seçenekten farklı bir dinleme gerçekleştirir.

Kaba Kuvvet Saldırısı v2 (mail): Hydra ile gmail ve hotmail için kaba kuvvet saldırısı yapar.

Şifreleme (md5,sha vs. şifrele) Aracı: Belirttiğiniz metni md5, sha1, sha224, sha256, sha384, sha512 ve blake2b algoritmaları ile şifreleyip tüm sonuçları gösterir.

DDOS Aracı: Sexettin'in sizin için hazırladığı 9 farklı saldırı seçeneği ile ddos saldırısı yapar. 9 saldırıdan 6 tanesi farklı boyutlarda paket gönderirken diğer saldırıların kendine has saldırı biçimi vardır. 

Site Kaynak Kodu Çekme Aracı: Belirtilen sitenin kaynak kodunu çekip kaydetmenize yarar.

İş Görür Araçlar: Videodan müziğe dönüştürme, müzik indirme, video indirme, py dosyasını exe formatına çevirme, terminalden dosya indirme ve terminalden müzik açma seçenekleri sunar.
 
Handshake Decrypter: aircrack-ng ile belirtilen wordlist ve handshake dosyalarını kullanarak wifi şifresini bulmaya çalışır.

Tersine Şifreleme (md5, sha vs. şifre kır): Sözlük saldırısı ile md5, sha1, sha224, sha256, sha384, sha512 ve blake2b şifrelerini çözmeye çalışır.

Directory Fuzzer: Belirtilen wordlist içerisindeki yolların, belirtilen site üzerinde olup olmadığını deneyerek kontrol eder.

Metforaya Bağlan: Sexettintool'u düzgün ve hatasız kullanmanız için kurulum yapar. Güncelleme, silme, yeniden yükleme veya da iletişim seçenekleri sunar.

Virüs Oluştur: 4 farklı virüs oluşturma seçeneği ile virüs oluşturmanızı sağlar. 

Linux Asistanı: Linux üzerinde temel işlemleri otomatize eder. Linux işletim sistemini Sexettintool ile kullanmaya başlayan kullanıcılar için idealdir.

Site Ip Bulma: Belirtilen sitenin ip adresini gösterir.

Index Oluşturucu: Sizin yönergelerinizle web sayfası oluşturur.

Xsnot: Sexettintool üzerinde not alma, not silme gibi işlemler yapmanızı sağlar.

FotoDit: Terminal üzerinde çeşitli fotoğraf düzenlemeleri yapmanızı sağlar.

Bilinen Kullanıcı Adını Sosyal Medyada Arama: Dinamik olarak hangi sitelerde belirtilen kullanıcı adı ile hesap açıldığını kontrol eder.

Exif İşlem Aracı: Exif verisi görüntüleme veya silme işlemleri yapabilirsiniz.

Site Fuzzing Aracı (Rastgele): Belirtile siteye farklı parametreler göndererek nasıl sonuç verdiğini kontrol eder.

Dosya Hash Adresi Bulma: Belirtilen dosyanın md5, sha1 veya sha256 hash adreslerini gösterir.

Dosya İzleme Monitörü: Belirtilen dizindeki dosya değişikliklerini izler.

Gelişmiş Şifreleme 1: Belirtilen metni veya dosyayı stncrypt pre 1 algoritması ile şifreler. Bu şifreleme algoritması sexettintool için özel yazıldı. İsterseniz şifreyi çözebilirsiniz.

Gelişmiş Şifreleme 2: Belirtilen metni veya dosyayı stncrypt pre 2 algoritması ile şifreler. Bu şifreleme algoritması sexettintool için özel yazıldı. Şifrenin her harfini rastgele şifreler ve bu rastgeleliği çözebilmek için bir anahtar oluşturur. Anahtar her zaman farklı olur. Anahtarı kaybetmediğiniz sürece şifreyi çözebilirsiniz. Kaybederseniz maalesef çözemezsiniz. Oluşturulan anahtarlar dosyaya özeldir. Her çalıştırmada farklı şifreler ve farklı anahtar oluşturur.

Yapay Zeka Şifre Analizi: Belirttiğiniz wordlist ile size özel bir yapay zeka modeli oluşturur. Bu model içerisine eklediğiniz şifreleri zayıf olarak kabul eder ve girdiğiniz şifreleri önceki zayıf şifrelerle kıyaslayarak şifre gücünü söyler.

Raspberry Pi Pico Hack

Sexettin Twin: Sexettin Twin saldırısı, ESP32 kullanarak bir ağın ikizini oluşturur ve kullanıcıyı oturum açması için yönlendirir. Kullanıcının girdiği verilere aynı ağa bağlanıp özel dosya ile ulaşabilirsiniz.

Blue-cough: Bluetooth cihazlarının port adreslerini tarar. İstediğiniz bluetooth cihazının sinyalini kesmenize yarar. İçerisinde bluetooth saldırı üzerine gelişmiş seçenekler mevcuttur.

Crawler-x11: Telegram üzerinde otomatik olarak hedef kullanıcının sizinle olan mesajlarını ve ortak gruptaki mesajlarını kayıt eder. Whatsapp için de çalışabilir.

Imitator-x11:  Belirtilen kişinin mesajlarını öğrenerek o kişinin bir kopyasını oluşturur. Örneğin bir insanın kopyasını oluşturup o kişi gibi merhaba kelimesi ile cümle kurmasını isteyebilirsiniz.
''')

else:
    print("Geçersiz seçenek")