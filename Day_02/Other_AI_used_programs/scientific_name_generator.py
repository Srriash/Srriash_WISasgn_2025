def get_scientific_name(common_name):
    # Dictionary of common animals and their scientific names
    scientific_names = {
        # Mammals
        "cat": "Felis catus",
        "dog": "Canis lupus familiaris",
        "human": "Homo sapiens",
        "lion": "Panthera leo",
        "tiger": "Panthera tigris",
        "elephant": "Loxodonta africana",
        "giraffe": "Giraffa camelopardalis",
        "zebra": "Equus quagga",
        "panda": "Ailuropoda melanoleuca",
        "wolf": "Canis lupus",
        "bear": "Ursus arctos",
        "brown bear": "Ursus arctos",
        "polar bear": "Ursus maritimus",
        "dolphin": "Delphinus delphis",
        "whale": "Balaenoptera musculus",
        "blue whale": "Balaenoptera musculus",
        "humpback whale": "Megaptera novaeangliae",
        "gorilla": "Gorilla gorilla",
        "chimpanzee": "Pan troglodytes",
        "orangutan": "Pongo pygmaeus",
        "horse": "Equus caballus",
        "cow": "Bos taurus",
        "sheep": "Ovis aries",
        "goat": "Capra hircus",
        "pig": "Sus scrofa domesticus",
        "rabbit": "Oryctolagus cuniculus",
        "mouse": "Mus musculus",
        "rat": "Rattus norvegicus",
        "kangaroo": "Macropus rufus",
        "koala": "Phascolarctos cinereus",
        "rhinoceros": "Rhinoceros unicornis",
        "hippopotamus": "Hippopotamus amphibius",
        "deer": "Cervus elaphus",
        "moose": "Alces alces",
        
        # Birds
        "chicken": "Gallus gallus domesticus",
        "eagle": "Aquila chrysaetos",
        "penguin": "Sphenisciformes",
        "emperor penguin": "Aptenodytes forsteri",
        "owl": "Strigiformes",
        "parrot": "Psittaciformes",
        "peacock": "Pavo cristatus",
        "swan": "Cygnus olor",
        "duck": "Anas platyrhynchos",
        "pigeon": "Columba livia",
        "sparrow": "Passer domesticus",
        "crow": "Corvus corone",
        "flamingo": "Phoenicopterus roseus",
        "ostrich": "Struthio camelus",
        
        # Reptiles
        "snake": "Serpentes",
        "python": "Python molurus",
        "cobra": "Naja naja",
        "crocodile": "Crocodylus niloticus",
        "alligator": "Alligator mississippiensis",
        "turtle": "Testudines",
        "sea turtle": "Chelonia mydas",
        "lizard": "Lacertilia",
        "gecko": "Gekkonidae",
        "iguana": "Iguana iguana",
        
        # Amphibians
        "frog": "Rana temporaria",
        "toad": "Bufo bufo",
        "salamander": "Salamandra salamandra",
        "newt": "Triturus vulgaris",
        
        # Fish
        "salmon": "Salmo salar",
        "tuna": "Thunnus thynnus",
        "shark": "Selachimorpha",
        "great white shark": "Carcharodon carcharias",
        "goldfish": "Carassius auratus",
        "clownfish": "Amphiprioninae",
        "angelfish": "Pterophyllum",
        "swordfish": "Xiphias gladius",
        
        # Insects
        "butterfly": "Lepidoptera",
        "monarch butterfly": "Danaus plexippus",
        "bee": "Apis mellifera",
        "ant": "Formicidae",
        "spider": "Araneae",
        "scorpion": "Scorpiones",
        "grasshopper": "Caelifera",
        "cricket": "Gryllidae",
        "ladybug": "Coccinellidae",
        "firefly": "Lampyridae",
        
        # Plants
        "peas": "Pisum sativum",
        "rose": "Rosa",
        "sunflower": "Helianthus annuus",
        "oak": "Quercus",
        "maple": "Acer",
        "pine": "Pinus",
        "bamboo": "Bambusoideae",
        "rice": "Oryza sativa",
        "wheat": "Triticum aestivum",
        "corn": "Zea mays",
        "potato": "Solanum tuberosum",
        "tomato": "Solanum lycopersicum",
        "carrot": "Daucus carota",
        "apple": "Malus domestica",
        "banana": "Musa",
        "orange": "Citrus × sinensis",
        "grape": "Vitis vinifera",
        "coconut": "Cocos nucifera",
        "lotus": "Nelumbo nucifera",
        "orchid": "Orchidaceae"
    }
    
    # Convert input to lowercase for case-insensitive matching
    common_name = common_name.lower().strip()
    
    # Return the scientific name if found, otherwise return a message
    return scientific_names.get(common_name, "Scientific name not found in database")

def main():
    print("Welcome to the Scientific Name Generator!")
    print("Enter 'quit' to exit the program")
    
    while True:
        # Get input from user
        common_name = input("\nEnter a common animal name: ")
        
        # Check if user wants to quit
        if common_name.lower() == 'quit':
            print("Thank you for using the Scientific Name Generator!")
            break
        
        # Get and display the scientific name
        result = get_scientific_name(common_name)
        print(f"\nCommon name: {common_name}")
        print(f"Scientific name: {result}")

if __name__ == "__main__":
    main()