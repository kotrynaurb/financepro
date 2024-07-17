import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_income_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('income')
    plt.plot(x, y, color='#9061F9', linewidth=3)
    plt.xticks(rotation=45)
    plt.xlabel('date')
    plt.ylabel('amount')
    plt.style.use('seaborn-v0_8-pastel')
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_expenses_bar(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('expenses')
    plt.bar(x, y, color='#9061F9', linewidth=3)
    plt.xticks(rotation=45)
    plt.xlabel('date')
    plt.ylabel('amount')
    plt.style.use('seaborn-v0_8-pastel')
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_expenses_bar(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('expenses')
    plt.bar(x, y, color='#9061F9', linewidth=3)
    plt.xticks(rotation=45)
    plt.xlabel('category')
    plt.ylabel('amount')
    plt.style.use('seaborn-v0_8-pastel')
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_bills_scatter(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('bills')
    plt.scatter(x, y, s=100, color='#9061F9', edgecolor='black', linewidth=1, alpha=0.75)
    plt.xticks(rotation=45)
    plt.xlabel('billing date')
    plt.ylabel('amount')
    plt.style.use('seaborn-v0_8-pastel')
    plt.tight_layout()
    graph = get_graph()
    return graph
