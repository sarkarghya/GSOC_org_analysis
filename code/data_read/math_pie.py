import seaborn as sns
from datetime import date
from datetime import timedelta
import matplotlib.pyplot as plt

from student_reader import stu_num

direct = f"./code/orgs-{date.today() - timedelta(days = 2)}/"  # edit date differance or type in full path

plt.pie(
    list(stu_num(direct).values()),
    labels=list(stu_num(direct).keys()),
    colors=sns.color_palette("pastel")[0:5],
    autopct="%.0f%%",
)

plt.title(label="Percent organisations by number of students", fontweight=10, pad="2.0")
plt.savefig("stupi.svg")
