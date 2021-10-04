import seaborn as sns
from datetime import date
from datetime import timedelta
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt

from type_reader import type_org
from lang_reader import lang_org

sns.set(style="whitegrid")
# sns.set_color_codes("Spectral")
direct = f"./code/orgs-{date.today() - timedelta(days = 2)}/"  # edit date differance or type in full path

plt.figure(2, figsize=(20, 15))
the_grid = GridSpec(1, 3)

plt.subplot(the_grid[0, 2], title="Organisation Types")
sns.barplot(
    x=list(type_org(direct).values()),
    y=list(type_org(direct).keys()),
    orient="h",
    palette="rocket",
)

plt.subplot(the_grid[0, 0], title="Five most commmon languages")
sns.barplot(
    x=list(lang_org(direct).values()),
    y=list(lang_org(direct).keys()),
    orient="h",
    palette="Spectral",
)

plt.suptitle("Statistics of Google Summer of Code Organisations", fontsize=16)

plt.savefig("bars.svg")
