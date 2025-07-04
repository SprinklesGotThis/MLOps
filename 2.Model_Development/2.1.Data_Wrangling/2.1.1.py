# Import frameworks
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('style_Matplotlib_charts.mplstyle')

data_frame = pd.read_csv("2.Model_Development/2.1.Data_Wrangling/2.1.2.diabeties_sample_data.csv")
# Target = A measure of disease progression in one year
data_frame.head()
data_frame.info()
data_frame.describe()
# plot a line graph 
data_frame.plot()
# Plot a histogram of a column
plt.hist(data_frame['BMI'])
plt.title(f"Histogram of {data_frame['BMI'].name}")
plt.ylabel('Count')
plt.xlabel(f'{data_frame["BMI"].name}')
plt.show()
# Scatter plot 2 columns to see the relationship
plt.scatter(data_frame['BMI'], data_frame['Target'])
plt.title(f"Scatter of {data_frame['BMI'].name} against {data_frame['Target'].name}")
plt.ylabel(f'{data_frame['Target'].name} Data')
plt.xlabel(f'{data_frame['BMI'].name} Data')
plt.show()
# Scatter plot multiples columns to see the relationship
x_plot = ['BMI', 'BP']
for col in x_plot:
    plt.scatter(data_frame[col], data_frame['Target'], marker='x')
plt.title(f"Scatter of {*x_plot,} against {data_frame['Target'].name}")
plt.ylabel(f'{data_frame['Target'].name} Data')
plt.xlabel(f'{*x_plot,} Data')
plt.show()
# Scatter plot 2 columns in separate charts with a shared y-axis
fig, (ax1, ax2) = plt.subplots(1,2, sharey=True)
plt.suptitle(f"Scatter of {data_frame['BMI'].name} and {data_frame['BP'].name} against {data_frame['Target'].name}")
ax1.set_ylabel(f'{data_frame['Target'].name} Data')

ax1.scatter(data_frame['BMI'], data_frame['Target'])
ax1.set_xlabel(f'{data_frame['BMI'].name} Data')

ax2.scatter(data_frame['BP'], data_frame['Target'])
ax2.set_xlabel(f'{data_frame['BP'].name} Data')

plt.show()
# 3D Scatter plot 3 columns to see the relationship

x_plot = ['BMI', 'BP']

fig = plt.figure()
plt.suptitle(f"3D Scatter of {*x_plot,} against {data_frame['Target'].name}")
ax = fig.add_subplot(111, projection='3d')

ax.scatter(data_frame[x_plot[0]], data_frame[x_plot[1]], data_frame['Target'], color='blue')

x1_range = np.linspace(data_frame[x_plot[0]].min(), data_frame[x_plot[0]].max())
x2_range = np.linspace(data_frame[x_plot[1]].min(), data_frame[x_plot[1]].max())
X1_grid, X2_grid = np.meshgrid(x1_range, x2_range)


ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Target')

plt.show()
# 3D Scatter plot 3 columns to see the relationship

x_plot = ['BMI', 'BP']

fig = plt.figure()
plt.suptitle(f"3D Scatter of {*x_plot,} against {data_frame['Target'].name}")
ax = fig.add_subplot(111, projection='3d')

ax.scatter(data_frame[x_plot[0]], data_frame[x_plot[1]], data_frame['Target'], color='blue')

x1_range = np.linspace(data_frame[x_plot[0]].min(), data_frame[x_plot[0]].max())
x2_range = np.linspace(data_frame[x_plot[1]].min(), data_frame[x_plot[1]].max())
X1_grid, X2_grid = np.meshgrid(x1_range, x2_range)


ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Target')

plt.show()