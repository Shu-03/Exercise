# 作者：shu qi
# 开发时间：2022/11/2 9:27
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import squarify

products_df = pd.read_csv("products.csv")
aisles_df = pd.read_csv("aisles.csv")
departments_df = pd.read_csv("departments.csv")
#print(departments_df)
order_products_prior_df = pd.merge(products_df, aisles_df, on='aisle_id', how='left')
order_products_prior_df = pd.merge(order_products_prior_df, departments_df, on='department_id', how='left')
order_products_prior_df.head()
temp = order_products_prior_df[['product_name', 'aisle', 'department']]
temp = pd.concat([
    order_products_prior_df.groupby('department')['product_name'].nunique().rename('products_department'),
    order_products_prior_df.groupby('department')['aisle'].nunique().rename('aisle_department')
], axis=1).reset_index()
temp = temp.set_index('department')
temp2 = temp.sort_values(by="aisle_department", ascending=False)
#print(temp)
#print(temp2)
x = 0
y = 0
width = 150
height = 150
cmap = matplotlib.cm.viridis
mini, maxi = temp2.products_department.min(), temp2.products_department.max()
norm = matplotlib.colors.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in temp2.products_department]
colors[1] = "#FBFCFE"
labels = ["%s\n%d aisle num\n%d products num"% (label) for label in
          zip(temp2.index, temp2.aisle_department, temp2.products_department)]
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, aspect="equal")
ax = squarify.plot(temp2.aisle_department, color=colors, label=labels, ax=ax, alpha=.9)

'''

fig.suptitle("How are aisles organized within departments", fontsize=20 )
ax.set_xticks([])
ax.set_yticks([])
img = plt.imshow([temp2.products_department], cmap=cmap)
img.set_visible(False)
fig.colorbar(img, orientation="vertical", shrink=.96)
fig.text(.76, .9, "numbers of products", fontsize=14)'''
plt.show()