import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd

# G = nx.erdos_renyi_graph(1000, 0.05)
# G = nx.watts_strogatz_graph(1000, 50, 0.1)
# G = nx.barabasi_albert_graph(1000, 25)
filename = ''

degree_sequence = [d for n, d in G.degree()]
sns.histplot(data=degree_sequence, kde=True, color='orange')
plt.xlabel('degree')
plt.ylabel('number of vertices')
plt.savefig(f'../imgs/{filename}_P.pdf')
plt.show()

c = nx.clustering(G)
sns.histplot(data=c, kde=True, color='forestgreen')
plt.xlabel('clustering coefficient')
plt.ylabel('number of vertices')
plt.savefig(f'../imgs/{filename}_C.pdf')
plt.show()

cc = nx.closeness_centrality(G)
sns.histplot(data=cc, kde=True, color='midnightblue')
plt.xlabel('closeness centrality')
plt.ylabel('number of vertices')
plt.savefig(f'../imgs/{filename}_CC.pdf')
plt.show()

bcv = nx.betweenness_centrality(G)
sns.histplot(data=list(bcv.values()), kde=True, color='orangered')
plt.xlabel('betweenness centrality')
plt.ylabel('number of vertices')
plt.savefig(f'../imgs/{filename}_CB.pdf')
plt.show()