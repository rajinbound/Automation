import requests
import json

response = requests.get('http://api.plos.org/search?q=title:DNA',
             params={'author_display':'Lukas Nejdl'},)
'''
print(response.text)
print(type(response.text))
dict_response = json.loads(response.text)
print(dict_response[0]['isbn'])
print(dict_response[1]['book_name'])
'''


json_response = response.json()
print((json_response))
print(json_response["response"]["numFound"], "\n")
print(json_response["response"]["maxScore"], "\n")
#print(json_response["response"]["docs"][0])
assert response.status_code == 200
print(response.headers)
#assert response.headers['Content-Type'] == 'application/json;charset=utf-8'
# Retrieve the more details and a specific detail by publication date

for existing in json_response["response"]['docs']:
    print(existing, "\n", "\n", "\n")

    if existing["publication_date"] == '2007-03-14T00:00:00Z':
        print(existing)
        break

expected_output = {'id': '10.1371/journal.pone.0000290', 'journal': 'PLoS ONE',
                'eissn': '1932-6203', 'publication_date': '2007-03-14T00:00:00Z',
                'article_type': 'Research Article',
                'author_display': ['Rayna I. Kraeva', 'Dragomir B. Krastev', 'Assen Roguev', 'Anna Ivanova', 'Marina N. Nedelcheva-Veleva', 'Stoyno S. Stoynov'],
                'abstract': ['Nucleic acids, due to their structural and chemical properties, can form double-stranded secondary structures that assist the transfer of genetic information and can modulate gene expression. However, the nucleotide sequence alone is insufficient in explaining phenomena like intron-exon recognition during RNA processing. This raises the question whether nucleic acids are endowed with other attributes that can contribute to their biological functions. In this work, we present a calculation of thermodynamic stability of DNA/DNA and mRNA/DNA duplexes across the genomes of four species in the genus Saccharomyces by nearest-neighbor method. The results show that coding regions are more thermodynamically stable than introns, 3′-untranslated regions and intergenic sequences. Furthermore, open reading frames have more stable sense mRNA/DNA duplexes than the potential antisense duplexes, a property that can aid gene discovery. The lower stability of the DNA/DNA and mRNA/DNA duplexes of 3′-untranslated regions and the higher stability of genes correlates with increased mRNA level. These results suggest that the thermodynamic stability of DNA/DNA and mRNA/DNA duplexes affects mRNA transcription.'], 'title_display': 'Stability of mRNA/DNA and DNA/DNA Duplexes Affects mRNA Transcription',
                'score': 6.5221877}


assert existing == expected_output













