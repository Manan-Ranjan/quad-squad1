import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize=(12, 8))

# set height of bar
Male = [1, 1, 1, 8, 22, 12, 30, 1, 8, 22, 12]
Female = [28, 6, 16, 5, 10,28, 6, 16, 5, 10, 16]

# Set position of bar on X axis
br1 = np.arange(len(Male))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

# Make the plot
plt.bar(br1, Male, color='r', width=barWidth,
        edgecolor='grey', label='Male')
plt.bar(br2, Female, color='g', width=barWidth,
        edgecolor='grey', label='Female')

# Adding Xticks
plt.xlabel('Age Group', fontweight='bold', fontsize=15)
plt.ylabel('Causes', fontweight='bold', fontsize=15)
plt.xticks([r + barWidth for r in range(len(Male))],
           ['14-20', '21-25', '26-30', '31-35', '36-40', '41-45','46-50','51-55','56-60','61-65','66-73'])
plt.yticks([r + barWidth for r in range(len(Female))],
           ['Air Pollution', 'Alcohol Use', 'Dust Allergy', 'Occupational Hazards', 'Genetic Risks',
            'Chronic Lung Disease','Balanced Diet','Obesity','Smoking','Passive Smoking','Passive Smoking'])


plt.legend()
plt.show()