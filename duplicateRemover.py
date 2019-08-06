# -*- coding: utf-8 -*-

import json
from sets import Set
from collections import defaultdict

def main():
    jsonSource = open("jsonSource.json", "r")
    outputFile = open("extractedProducts.json", "w+")

    productsSource = json.load(jsonSource)
    productKeys = productsSource.keys()

    newProductJSON = {}


    subCategorySet = defaultdict(int)
    subSubCategorySet = defaultdict(int)

    outputFileArray = Set()

    for productKey in productKeys:
        currentProduct = productsSource[productKey]
        subCategory = currentProduct["Meta"]["SubCategory"]

        meta = currentProduct["Meta"]
        if "SubSubCategory" in meta:
            subSubCategory = currentProduct["Meta"]["SubSubCategory"]
            subSubCategorySet[subSubCategory] = 0

        subCategorySet[subCategory] = 0

    for productKey in productKeys:
       currentProduct = productsSource[productKey]

       for cat in subCategorySet:
          stringCat = str(cat)
          if stringCat == currentProduct["Meta"]["SubCategory"]:
              subCategorySet[cat] += 1

       for cat in subSubCategorySet:
          stringCat = str(cat)
          meta = currentProduct["Meta"]
          if "SubSubCategory" in meta:
              if stringCat == currentProduct["Meta"]["SubSubCategory"]:
                  subSubCategorySet[cat] += 1

       #We are simply overwriting the key in our json
       newProductJSON[productKey] = currentProduct

    sortedSubCatSet = sorted(subCategorySet)
    sortedSubSubCatSet = sorted(subSubCategorySet)

    print(sortedSubCatSet)
    print(sortedSubSubCatSet)
    json.dump(newProductJSON, outputFile)

if __name__ == '__main__':
    main()
