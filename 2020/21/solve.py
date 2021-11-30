"""Advent Of Code #21."""
with open("input") as f:
    data = f.read()

# data = """\
# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)
# """

data = data.replace("(", "").replace(")", "").replace(",", "")

ingredients = []
allergens = []
for food in data.splitlines():
    ingredient, allergen = food.split(" contains ")
    ingredient = set(ingredient.split())
    allergen = set(allergen.split())
    ingredients.append(ingredient)
    allergens.append(allergen)


# Part 1
def find(ingredients, allergens):
    """Find ingredient/allergene to remove."""
    all_allergens = set()
    for allergen in allergens:
        all_allergens = all_allergens.union(allergen)

    for a in all_allergens:
        ingredient = None
        allergen = None
        for i in range(len(ingredients)):
            if a in allergens[i]:
                if ingredient is None:
                    ingredient = ingredients[i]
                    allergen = allergens[i]
                else:
                    ingredient = ingredient.intersection(ingredients[i])
                    allergen = allergen.intersection(allergens[i])
        if len(ingredient) == 1 and len(allergen) == 1:
            return ingredient.pop(), allergen.pop()

    return None, None


pairs = []
while True:
    ingredient, allergen = find(ingredients, allergens)
    if ingredient is None or allergen is None:
        break
    pairs.append((allergen, ingredient))
    for i in range(len(ingredients)):
        ingredients[i].discard(ingredient)
    for i in range(len(allergens)):
        allergens[i].discard(allergen)

no_allergens = sum(len(ingredient) for ingredient in ingredients)
print("Part 1:", no_allergens)
assert no_allergens == 2412

# Part 2
pairs = sorted(pairs)
dangerous = ",".join([second for _, second in pairs])
print("Part 2:", dangerous)
assert dangerous == "mfp,mgvfmvp,nhdjth,hcdchl,dvkbjh,dcvrf,bcjz,mhnrqp"
