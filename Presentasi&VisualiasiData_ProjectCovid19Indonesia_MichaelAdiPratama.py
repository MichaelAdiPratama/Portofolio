import pandas as pd
import matplotlib.pyplot as plt
# =================== Plot Line Chart Total Cases =======================================================
# Baca dataset COVID-19 Indonesia (pastikan kolom Date dan Total_Cases tersedia)
# link = "covid19Indonesia.csv"
# covid_data = pd.read_csv(link,parse_dates=["Date"],index_col="Province")
# covid_data.columns = covid_data.columns.str.replace(' ','_')

# Data Preprocessing:
# covid = covid_data[covid_data["Date"] == ("2022-09-15")] #dipilih tanggal terakhir pada dataset
# covid = covid[covid.index.notnull()] #drop index yang terdapat missing value
# covid.head(10)


# df = covid_data[['Total_Active_Cases']]

# print(df)
# # Konversi kolom 'Date' menjadi tipe datetime
# covid_data['Date'] = pd.to_datetime(covid_data['Date'])

# # Filter data untuk Provinsi Jawa Timur dan Jakarta
# jawa_timur_data = covid_data[(covid_data['Province'] == 'Jawa Timur') & (covid_data['Date'] >= '2020-03-01') & (covid_data['Date'] <= '2022-12-31')]
# jakarta_data = covid_data[(covid_data['Province'] == 'DKI Jakarta') & (covid_data['Date'] >= '2020-03-01') & (covid_data['Date'] <= '2022-12-31')]

# # Atur ukuran plot
# plt.figure(figsize=(12, 6))

# # Plot time series untuk Provinsi Jawa Timur
# plt.plot(jawa_timur_data['Date'], jawa_timur_data['Total Deaths'], label='Jawa Timur', color='orange', marker='o')

# for i, txt in enumerate(jakarta_data['Total Deaths']):
#     if i % 60 == 0:
#         plt.annotate(txt, (jakarta_data['Date'].iloc[i], txt), textcoords="offset points", xytext=(0,3), ha='right')

# # Plot time series untuk Provinsi Jakarta
# plt.plot(jakarta_data['Date'], jakarta_data['Total Deaths'], label='Jakarta', color='blue', marker='o')

# for i, txt in enumerate(jawa_timur_data['Total Deaths']):
#     if i % 60 == 0:
#         plt.annotate(txt, (jawa_timur_data['Date'].iloc[i], txt), textcoords="offset points", xytext=(0,5), ha='left')
# # Tambahkan judul dan keterangan sumbu
# plt.title('Time Series of COVID-19 Cases in Jawa Timur and Jakarta (Mar 2020 - Dec 2022)')
# plt.xlabel('Date')
# plt.ylabel('Total Cases')

# # Tambahkan legenda
# plt.legend()

# # Putar label tanggal agar lebih mudah dibaca
# plt.xticks(rotation=45)

# # Tampilkan plot
# plt.tight_layout()
# plt.show()
#==================================================================================================================

#=================== Tree Maps Plot Total Deaths =======================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Atur ukuran plot
# plt.figure(figsize=(12, 8))
# filtered_data = covid_data[covid_data['Location'] != 'Indonesia']

# fig = px.treemap(filtered_data, 
#                  path=['Province'], 
#                  values='Total Deaths',
#                  color='Total Deaths',
#                  color_continuous_scale='YlOrBr',
#                  title='Treemap of Total Deaths Seluruh Provinsi di Indonesia',
#                  hover_data=['Total Deaths'])

# # Tampilkan plot
# fig.show()
# ==================================================================================================================

# import pandas as pd
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# # Load dataset
# data = pd.read_excel('DataCovid19Cum.xlsx')  # Gantilah 'nama_file_dataset.csv' dengan nama file dataset Anda

# # Load peta Indonesia
# indonesia_map = mpimg.imread('peta-indonesia2jpg.jpg')  # Gantilah 'path/to/indonesia_map.png' dengan path ke peta Indonesia

# # Plot scatter plot pada peta
# fig, ax = plt.subplots(figsize=(4, 4))
# scatter = ax.scatter(data['Longitude'], data['Latitude'], c='black', s=data['TotalCases']*1, alpha=0.6)

# # Menambahkan colorbar
# cbar = plt.colorbar(scatter)
# cbar.set_label('Total Recovered')

# # Menampilkan peta Indonesia sebagai background
# ax.imshow(indonesia_map, extent=[95, 141, -10, 6], alpha=0.5)

# # Menambahkan label dan judul
# plt.title('Scatter Plot TotalCases di Indonesia')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')

# # Menampilkan plot
# plt.show()

# # ============================= Total Deaths ================================================================
# # import pandas as pd
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# # Load dataset
# data = pd.read_excel('DataCovid19Cum.xlsx')  # Gantilah 'nama_file_dataset.csv' dengan nama file dataset Anda

# # Load peta Indonesia
# indonesia_map = mpimg.imread('peta-indonesia2jpg.jpg')  # Gantilah 'path/to/indonesia_map.png' dengan path ke peta Indonesia

# # Plot scatter plot pada peta
# fig, ax = plt.subplots(figsize=(4, 4))
# scatter = ax.scatter(data['Longitude'], data['Latitude'], c='red', s=data['TotalDeaths']*1, alpha=0.6)

# # Menambahkan colorbar
# cbar = plt.colorbar(scatter)
# cbar.set_label('Total Deaths')

# # Menampilkan peta Indonesia sebagai background
# ax.imshow(indonesia_map, extent=[95, 141, -10, 6], alpha=0.5)

# # Menambahkan label dan judul
# plt.title('Scatter Plot TotalDeaths di Indonesia')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')

# # Menampilkan plot
# plt.show()



# # ============================= Total Recovered ================================================================
# # import pandas as pd
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# # Load dataset
# data = pd.read_excel('DataCovid19Cum.xlsx')  # Gantilah 'nama_file_dataset.csv' dengan nama file dataset Anda

# # Load peta Indonesia
# indonesia_map = mpimg.imread('peta-indonesia2jpg.jpg')  # Gantilah 'path/to/indonesia_map.png' dengan path ke peta Indonesia

# # Plot scatter plot pada peta
# fig, ax = plt.subplots(figsize=(4, 4))
# scatter = ax.scatter(data['Longitude'], data['Latitude'], c='green', s=data['TotalRecovered']*1, alpha=0.6)

# # Menambahkan colorbar
# cbar = plt.colorbar(scatter)
# cbar.set_label('Total Recovered')

# # Menampilkan peta Indonesia sebagai background
# ax.imshow(indonesia_map, extent=[95, 141, -10, 6], alpha=0.5)

# # Menambahkan label dan judul
# plt.title('Scatter Plot TotalRecovered di Indonesia')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')

# # Menampilkan plot
# plt.show()

# ==================================================================================================================