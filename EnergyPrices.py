import pandas as pd
import requests
import matplotlib.pyplot as plt
from datetime import date
import mplcursors as mpc



date_string = date.today().strftime('%Y-%m-%d')
url = "https://api.energidataservice.dk/dataset/elspotprices?start="+date_string+"&sort=HourDK%20ASC&filter={%22PriceArea%22:%22DK2%22}"

response = requests.get(url)

json_data = response.json()
df = pd.DataFrame(json_data['records'])
df.plot(x='HourDK', y='SpotPriceDKK', marker="*")
plt.xlabel("DatoTid")
plt.ylabel("Pris DKK")
plt.gcf().text(0.02, 0.9, "Day ahead spotprices in DK and neighboring countries \nPrices in DKK are not updated during weekends and on public holidays. Prices in DKK will be updated at the first coming work day.\nIn Nord Pool Spot market players can buy and sell electricity for delivery the following day in their own area - Norway, Sweden, Finland, Denmark or Germany. The day-ahead prices indicate the balance between supply and demand.",fontsize=8)
plt.legend()
plt.grid()
mpc.cursor(hover=True)
plt.show()