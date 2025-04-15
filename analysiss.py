
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка Excel-файла
xlsx_path = "livestock_kazakhstan_2024.xlsx"
df_raw = pd.read_excel(xlsx_path, sheet_name='1.', header=None)

# Извлекаем таблицу по строкам
df_livestock = df_raw.iloc[6:34, [0, 1, 4]]
df_livestock.columns = ['Продукция', '2024 год', '2023 год']
df_livestock.reset_index(drop=True, inplace=True)
df_livestock.dropna(how='all', inplace=True)
df_livestock['Продукция'] = df_livestock['Продукция'].astype(str).str.strip()
df_livestock = df_livestock[df_livestock['Продукция'].str.len() > 1]
df_livestock['2024 год'] = pd.to_numeric(df_livestock['2024 год'], errors='coerce')
df_livestock['2023 год'] = pd.to_numeric(df_livestock['2023 год'], errors='coerce')

# Обработка пропусков
print("Пропущенные значения:")
print(df_livestock.isnull().sum())

# Расчёт прироста
df_livestock['Рост (%)'] = ((df_livestock['2024 год'] - df_livestock['2023 год']) / df_livestock['2023 год']) * 100

# Первичный осмотр
print("\nПервые строки:")
print(df_livestock.head())

print("\nСтатистика:")
print(df_livestock.describe())

# Визуализация: Улучшенный Bar chart
df_sorted = df_livestock.sort_values(by='2024 год', ascending=False)

plt.figure(figsize=(14, 7))
x = df_sorted['Продукция']
indices = range(len(x))
width = 0.35

plt.bar(indices, df_sorted['2023 год'], width=width, label='2023 год')
plt.bar([i + width for i in indices], df_sorted['2024 год'], width=width, label='2024 год')
plt.xticks([i + width / 2 for i in indices], x, rotation=45, ha='right')
plt.title('Сравнение производства продукции животноводства (2023 vs 2024)')
plt.xlabel('Вид продукции')
plt.ylabel('Объём')
plt.legend()
plt.tight_layout()
plt.savefig("bar_chart_readable.png")
plt.close()

# Визуализация: Улучшенная Histogram
plt.figure(figsize=(10, 6))
plt.hist(df_livestock['2024 год'].dropna(), bins=10, edgecolor='black', color='orange')
plt.title('Гистограмма распределения продукции (2024 год)')
plt.xlabel('Объём (в штуках/тоннах)')
plt.ylabel('Количество категорий')
plt.grid(True)
plt.ticklabel_format(style='plain', axis='x')  # отключаем экспоненциальный формат
plt.tight_layout()
plt.savefig("histogram_2024_readable.png")
plt.close()

print("\nГрафики сохранены как bar_chart_readable.png и histogram_2024_readable.png")
