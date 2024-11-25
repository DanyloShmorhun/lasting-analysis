# Dictionary for correcting typos and variations in drug names
typo_corrections = {
    # Analgesics
    'parascetamol': 'paracetamol',
    'parasetamol': 'paracetamol',
    'paracetyesmol': 'paracetamol',
    'paraceyesmol': 'paracetamol',
    'peracetamol': 'paracetamol',
    'paracet': 'paracetamol',
    'paracetmol': 'paracetamol',
    'paraceyesmol': 'paracetamol',
    'parace': 'paracetamol',
    'sanmol': 'paracetamol',  # Brand name
    'farmadol': 'paracetamol',
    'pamol': 'paracetamol',
    # Antibiotics
    'ampicilin': 'ampicillin',
    'ampicillia': 'ampicillin',
    'ampiciullin': 'ampicillin',
    'ampicilliin': 'ampicillin',
    'sampicillin': 'ampicillin',
    'amoxicilin': 'amoxicillin',
    'amoicellin': 'amoxicillin',
    'amoxson': 'amoxicillin',
    'gentamicyn': 'gentamicin',
    'gentamisin': 'gentamicin',
    'gentamycin': 'gentamicin',
    'bentangcin': 'gentamicin',
    'halmycin': 'gentamicin',
    'cefotaxim': 'cefotaxime',
    'cefotaxin': 'cefotaxime',
    'cefotaxil': 'cefotaxime',
    'cefotacime': 'cefotaxime',
    'cefotax': 'cefotaxime',
    'ceftriaxon': 'ceftriaxone',
    'cetriaxon': 'ceftriaxone',
    'ceftriakson': 'ceftriaxone',
    'ceftriyesxon': 'ceftriaxone',
    'ceftonaxon': 'ceftriaxone',
    'cefmaxone': 'ceftriaxone',
    'cloramfenicol': 'chloramphenicol',
    'clorampenicol': 'chloramphenicol',
    'clorafenicol': 'chloramphenicol',
    'chloromfenical': 'chloramphenicol',
    'chloromfenicol': 'chloramphenicol',
    # Anticonvulsants
    'diaxepam': 'diazepam',
    'stesolid': 'diazepam',
    'setosal': 'diazepam',
    # Antiemetics
    'donperidon': 'domperidone',
    'vometa': 'domperidone',
    'vomitas': 'domperidone',
    'vosedon': 'domperidone',
    'vasedon': 'domperidone',
    'domperiudon': 'domperidone',
    # Mucolytics
    'ambroxce': 'ambroxol',
    'ambroksol': 'ambroxol',
    'mukos': 'ambroxol',
    'mucos': 'ambroxol',
    # Bronchodilators
    'ventolin': 'salbutamol',
    'ventolen': 'salbutamol',
    'ventolene': 'salbutamol',
    'ventoline': 'salbutamol',
    'ventolyn': 'salbutamol',
    'hentolin': 'salbutamol',
    # Steroids
    'dexavefosme': 'dexamethasone',
    'dexamethason': 'dexamethasone',
    'dekamethason': 'dexamethasone',
    'deksametason': 'dexamethasone',
    'dekame': 'dexamethasone',
    # Vitamins and Minerals
    'as falat': 'folic acid',
    'as folat': 'folic acid',
    'asam fo lot': 'folic acid',
    'asam folat': 'folic acid',
    'thiamu': 'thiamine',
    'thiamu ltd': 'thiamine',
    'thyesmicin': 'thiamine',
    'zinckid': 'zinc',
    'zincpro': 'zinc',
    'zinckpro': 'zinc',
    'zinc pro': 'zinc',
    # Probiotics
    'lacto b': 'lacto b',
    'l-bio': 'lacto b',
    'lacto-bio': 'lacto b',
    'lactob': 'lacto b',
    'lactobio': 'lacto b',
    'lacto bio': 'lacto b',
    'probiotik': 'probiotic',
    'probiotil': 'probiotic',
    'dialac': 'probiotic',
    'protexin': 'probiotic',
    # Antiprotozoals
    'metromidazole': 'metronidazole',
    'metronidazol': 'metronidazole',
    # Antitubercular Drugs
    'rimactazid': 'rimactazid',
    # Electrolyte Supplements
    'kci pulvus': 'potassium chloride',
    'kcl': 'potassium chloride',
    'kci': 'potassium chloride',
    # Others
    'colisinten': 'colistin',
    'colistin': 'colistin',
    'cefixim': 'cefixime',
    'sporetik': 'cefixime',
    'cetofaxime': 'cefotaxime',
    'cetotaxim': 'cefotaxime',
    'kalpicillin': 'ampicillin',
    'puluus': 'pulvis',
    'imboost': 'immunomodulator',
    'pct': 'paracetamol',
    'vosealon': 'domperidone',
    'trymetropin sulfameloxasol': 'cotrimoxazole',
    'trymetroprim sulfamethoxazol': 'cotrimoxazole',
    'tyrmetroprim sulfamethoxazol': 'cotrimoxazole',
    'sanprima': 'cotrimoxazole',
    'apialys': 'vitamin',
    'dalacin c': 'clindamycin',
    'clindamycin': 'clindamycin',
    'aldacho': 'spironolactone',
    'frosemin': 'furosemide',
    'koreksi kalium': 'potassium chloride',
    'onepratole': 'omeprazole',
    'pridrop': 'prednisolone',
    # Add more corrections as needed
}

# Dictionary mapping drugs to their categories
drug_categories = {
    # Analgesics
    'paracetamol': 'analgesic',
    'ibuprofen': 'analgesic',
    # Antibiotics
    'ampicillin': 'antibiotic',
    'amoxicillin': 'antibiotic',
    'gentamicin': 'antibiotic',
    'cefotaxime': 'antibiotic',
    'ceftriaxone': 'antibiotic',
    'chloramphenicol': 'antibiotic',
    'cotrimoxazole': 'antibiotic',
    'metronidazole': 'antibiotic',
    'ciprofloxacin': 'antibiotic',
    'colistin': 'antibiotic',
    'cefixime': 'antibiotic',
    'clindamycin': 'antibiotic',
    # Anticonvulsants
    'diazepam': 'anticonvulsant',
    'phenobarbital': 'anticonvulsant',
    'carbamazepine': 'anticonvulsant',
    # Probiotics
    'lacto b': 'probiotic',
    'probiotic': 'probiotic',
    'dialac': 'probiotic',
    'protexin': 'probiotic',
    # Antiemetics
    'domperidone': 'antiemetic',
    'metoclopramide': 'antiemetic',
    # Mucolytics
    'ambroxol': 'mucolytic',
    'acetylcysteine': 'mucolytic',
    # Bronchodilators
    'salbutamol': 'bronchodilator',
    # Steroids
    'dexamethasone': 'steroid',
    'prednisolone': 'steroid',
    # Vitamins and Minerals
    'vitamin': 'vitamin',
    'folic acid': 'vitamin',
    'thiamine': 'vitamin',
    'zinc': 'mineral supplement',
    # Electrolyte Supplements
    'potassium chloride': 'electrolyte supplement',
    # Diuretics
    'furosemide': 'diuretic',
    'spironolactone': 'diuretic',
    'acetazolamide': 'diuretic',
    # Antivirals
    'aciclovir': 'antiviral',
    # Anthelmintics
    'pyrantel': 'anthelmintic',
    'pamoate': 'anthelmintic',
    # Nootropics
    'piracetam': 'nootropic',
    # Antitubercular Drugs
    'rimactazid': 'antitubercular',
    # Proton Pump Inhibitors
    'omeprazole': 'proton pump inhibitor',
    # Immunomodulators
    'immunomodulator': 'immunomodulator',
    # Antiprotozoals
    'metronidazole': 'antiprotozoal',
    # Add more drugs and categories as needed
}
