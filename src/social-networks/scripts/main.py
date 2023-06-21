import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd

# DATE_FILE = '../data/weighted_OVERALL_dolphin_florida.graphml'
# DATE_FILE = '../data/hyena_holekamp_networkA_attribute.graphml'
# DATE_FILE = '../data/mice_lopes_attribute.graphml'
# DATE_FILE = '../data/facebook.edges'
# DATE_FILE = '../data/twitchES.edges'

filename = ''

if DATE_FILE[-7:] == 'graphml':
    G = nx.read_graphml(DATE_FILE)
else:
    G = nx.Graph()
    with open(DATE_FILE) as f:
        lines = f.readlines()
        for line in lines:
            a = int(line.strip().split()[0])
            b = int(line.strip().split()[1])
            G.add_edge(a, b)
            # w = float(line.strip().split()[2])
            # G.add_edge(a, b, weight=w)

print(G.number_of_edges(), G.number_of_nodes())

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

# bcv = nx.betweenness_centrality(G, weight='weight', normalized=False)
# sns.histplot(data=list(bcv.values()), kde=True, color='purple')
# plt.yscale('log')
# plt.ylim(0.8, 200)
# plt.gca().yaxis.set_major_formatter(ticker.ScalarFormatter())
# plt.xlabel('betweenness centrality')
# plt.ylabel('number of vertices')
# plt.show()