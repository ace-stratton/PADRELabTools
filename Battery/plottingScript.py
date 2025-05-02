# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:30:46 2024

@author: user
"""
import pandas as pd
import matplotlib.pyplot as plt
import csv

filenames = ['ScienceModeDrain_NoSolarInput.csv', 'Battery Drain Data.csv']
fig2, ax3 = plt.subplots()

for i in range(len(filenames)):

    saveArray = pd.DataFrame.to_numpy(pd.read_csv(filenames[i], header=None))
    #saveArray = pd.read_csv('Battery Drain Data.csv', header=None).to_numpy()
    if i == 0:
        bV = saveArray[1,:]
        bI = saveArray[2,:]
    else:
        bV = saveArray[:,1]
        bI = saveArray[:,2]

    #plotting depth of discharge versus voltage and current

    # Calculating Depth Of Discharge
    if i == 1:
        tHours = (saveArray[:, 0])/60/60 #seconds to hours
        tHours = tHours-(tHours[1])
        Volts = (saveArray[:,1])*(10**-3) #Volts
        Amps = abs((saveArray[:,2])*(10**-3)) #Amps
        WhFull = 84 #Wh
    else:
        tHours = (saveArray[0,:])/60/60 #seconds to hours
        tHours = tHours-(tHours[1])
        Volts = (saveArray[1,:])*(10**-3) #Volts
        Amps = abs((saveArray[2,:])*(10**-3)) #Amps
        WhFull = 84 #Wh

    Wh = tHours*Volts*Amps
    leng = len(Amps)

    DrainPerc =(1-((WhFull-Wh)/WhFull))*100
    print(f'Total Time to Drain: {tHours[-1]} hours for {DrainPerc[-2]}% of battery capacity with a power draw of {abs(Amps[-2])}A')
    PercLoss = DrainPerc[-2]/tHours[-1]/abs(Amps[-2])
    print(f'Percent Loss: {PercLoss} %/hr/A, in 45 minutes it would be {PercLoss*0.75*abs(Amps[-2])} %')


    ax3.set_xlabel('Drainage Percent')
    ax3.set_title('Battery Performance Pre and Post Thermal Event')
    ax3.set_ylabel('Voltage (mV)')
    ax3.plot(DrainPerc[2:-2],bV[2:-2])

    if i == 1:
        with open('Voltage_vs_DoD.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Voltage', 'Percentage'])  # Header
            for j in range(len(DrainPerc)):
                writer.writerow([bV[j], DrainPerc[j]])
    # ax4 = ax3.twinx()
    # color = 'tab:red'
    # ax4.set_ylabel('Current (mA)', color=color)
    # ax4.plot(DrainPerc[2:-2], bI[2:-2], color=color)
    # ax4.tick_params(axis='y', labelcolor=color)

fig2.tight_layout()
ax3.legend(['Pre', 'Post'])
plt.show()
fig2.savefig('BatteryPerformance050125.png', dpi=300)


