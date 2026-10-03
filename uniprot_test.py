#radhe radhe
import requests
def get_protein_info(proname, species):

#proname=input("enter the name of the protien who's structure you want to display ")
#species=input("Enter species ")
    url="https://rest.uniprot.org/uniprotkb/search"
    search_para={
        "query":f"{proname} AND organism_name:\"{species}\"",
        "format":"json" 
    }
    response=requests.get(url,params=search_para)
    #print(response.json())
    proteins = []
    data=response.json()
    for result in data["results"]:
        protein_name = result["proteinDescription"]["recommendedName"]["fullName"]["value"]
        accession = result["primaryAccession"]
        organism = result["organism"]["scientificName"]
        proteins.append({
        "name": protein_name,
        "accession": accession,
        "organism": organism
    })
        '''
        #print(protein_name)
        if proname.lower()== protein_name.lower():
            accession = result["primaryAccession"]
            sequence = result["sequence"]["value"]
            length = result["sequence"]["length"]
            organism = result["organism"]["scientificName"]
            print(accession)
            print(sequence)
            print(length)
            print(organism)
            print(protein_name)
            
            #print(
            # result["primaryAccession"],
            #  result["proteinDescription"]["recommendedName"]["fullName"]["value"],
            # result["organism"]["scientificName"],
       '''
        '''         
        # )
    protein_info = {
                "name": protein_name,
                "accession": accession,
                "sequence": sequence,
                "length": length,
                "organism": organism
            }
    print("displaying protien info: ")
    print(protein_info)
    print(protein_info["accession"])
    '''
        '''
    alphafold_url = f"https://alphafold.ebi.ac.uk/api/prediction/{protein_info['accession']}"
    responsealpha = requests.get(alphafold_url)
    print("Status code:", responsealpha.status_code)
    alphafold_data = responsealpha.json()
    print(alphafold_data)
    structure_url = alphafold_data[0]["pdbUrl"]

    #print("Structure URL:")
    #print(structure_url)
    structure_response = requests.get(structure_url)

    #print("Structure status:", structure_response.status_code)
    #print(structure_response.text[:500])
    with open("protein_structure.pdb", "w") as file:
        file.write(structure_response.text)

    print("Structure file saved!")
    '''
    return proteins
def get_structure(accession):
    
    alphafold_url = f"https://alphafold.ebi.ac.uk/api/prediction/{accession}"

    responsealpha = requests.get(alphafold_url)

    alphafold_data = responsealpha.json()

    structure_url = alphafold_data[0]["pdbUrl"]

    structure_response = requests.get(structure_url)

    with open("protein_structure.pdb", "w") as file:
        file.write(structure_response.text)

    return structure_url