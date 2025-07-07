import deepchem as dc
from rdkit import Chem
from rdkit.Chem import AllChem
import random
import numpy as np

# Przykładowe proste fragmenty molekuł (baza do losowania SMILES)
fragments = [
    "C", "O", "N", "Cl", "Br", "F",
    "CC", "CO", "CN", "CCO", "CNC",
    "CCC", "CCN", "CCCl", "CCBr",
    "C=O", "C#N", "C=C", "C#C"
]

# Funkcja generująca losową molekułę (SMILES) przez łączenie fragmentów
def generate_random_smiles(max_fragments=5):
    mol_smiles = ""
    n = random.randint(2, max_fragments)
    for _ in range(n):
        mol_smiles += random.choice(fragments)
    return mol_smiles

# Wczytujemy model DeepChem (tu przyjmujemy, że masz wytrenowany model lub wgrywasz go)
# Dla uproszczenia tu tworzymy model dummy (nie trenujemy go na danych, ale powinieneś)
featurizer = dc.feat.ConvMolFeaturizer()
model = dc.models.GraphConvModel(1, mode='classification')

# Tu powinieneś załadować model wytrenowany na danych antywściekliznowych:
# np. model.restore('sciezka_do_modelu')

# Tu damy dummy predict - zamienimy na coś prostego, bo model jest nieprzetrenowany
def predict_activity(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return 0.0
    X = featurizer.featurize([mol])
    # model.predict zwróci prawdopodobieństwo
    # ale model jest nieprzetrenowany, więc dajmy losowo wysoką aktywność dla "dobrych" fragmentów
    score = 0
    for frag in ["C=O", "N", "O"]:
        if frag in smiles:
            score += 0.4
    return min(score + random.uniform(0, 0.2), 1.0)

# Główna pętla szukająca leku
best_smiles = None
best_score = 0
max_iterations = 10000

for i in range(max_iterations):
    candidate = generate_random_smiles()
    score = predict_activity(candidate)
    if score > best_score:
        best_score = score
        best_smiles = candidate
        print(f"[{i}] Nowy najlepszy lek: {best_smiles} z aktywnością {best_score:.3f}")
        if best_score > 0.95:
            print("Znaleziono skuteczny lek!")
            break

if best_smiles:
    print("\n=== RECEPTURA LEKU ===")
    print(f"SMILES: {best_smiles}")
    print(f"Przewidywana aktywność: {best_score:.3f}")
else:
    print("Nie znaleziono skutecznego leku w danym limicie iteracji.")
