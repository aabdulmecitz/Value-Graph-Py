import numpy as np
import matplotlib.pyplot as plt

def compound_interest_monthly(principal, rate, months):
    """
    principal: Başlangıç yatırımı (ana para)
    rate: Aylık faiz oranı (örneğin %30 için 0.30)
    months: Faiz uygulanacak toplam ay sayısı
    """
    amounts = [principal]  # Başlangıç parası
    for month in range(1, months + 1):
        principal = principal * (1 + rate)  # Her ay faiz uygulanır
        amounts.append(principal)
    return amounts

def on_key(event):
    # ESC veya 'q' tuşuna basıldığında uygulamayı kapat
    if event.key == 'escape' or event.key == 'q':
        print("Uygulama kapatılıyor...")
        plt.close()

principal = 30000  # Başlangıç yatırımı
rate = 0.30  # Aylık faiz oranı (aylık %30)
rate_p = 0.10  # Aylık %10 faiz oranı
months = 36  # 36 ay boyunca faiz uygulanacak

# Faizli tutarların hesaplanması
amounts = compound_interest_monthly(principal, rate, months)
amounts_p = compound_interest_monthly(principal, rate_p, months)

# Bin birimine dönüştür (1000'e böl)
amounts_thousands = [amount / 1000 for amount in amounts]
amounts_p_thousands = [amount / 1000 for amount in amounts_p]

# Grafik oluşturma
plt.figure(figsize=(12, 6))  # Geniş bir grafik
plt.plot(range(months + 1), amounts_thousands, label='Aylık %30 Bileşik Faiz (Kasa)', color='blue', marker='o')
plt.plot(range(months + 1), amounts_p_thousands, label='Aylık %10 Bileşik Faiz (Yatırımcı)', color='red', marker='o')

# Y ekseni sınırlarını ayarla
max_amount = max(max(amounts_thousands), max(amounts_p_thousands))
plt.ylim(0, max_amount * 1.1)  # En yüksek miktardan biraz fazlasını göster

# Bilimsel notasyonu devre dışı bırak
plt.ticklabel_format(style='plain', axis='y')

# Eksen etiketleri ve başlık
plt.title('Aylık Bileşik Faiz Hesaplaması (36 Ay)')
plt.xlabel('Ay')
plt.ylabel('Toplam Miktar (Bin TL)')
plt.grid(True)

# Değerleri yalnızca belirli noktalara metin olarak ekle
for i in range(0, months + 1, 6):  # Her 6 ayda bir ekle
    plt.text(i, amounts_thousands[i], f"{int(amounts_thousands[i]):,}K", 
             fontsize=10, color='blue', ha='center')
    plt.text(i, amounts_p_thousands[i], f"{int(amounts_p_thousands[i]):,}K", 
             fontsize=10, color='red', ha='center')

# Eksen formatını Türk formatına çevir
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", " ")))
plt.gcf().canvas.mpl_connect('key_press_event', on_key)

plt.legend()
plt.show()
