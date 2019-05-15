def removeDuplicateLabels(labels):
    for i, k in enumerate(labels):
        if k == "ARTS" or k == "CULTURE & ARTS":
            labels[i] = "ARTS & CULTURE"
        elif k == "STYLE":
            labels[i] = "STYLE & BEAUTY"
        elif k == "WELLNESS" or k == "HEALTHY LIVING":
            labels[i] = "HOME & LIVING"
        elif k == "PARENTS":
            labels[i] = "PARENTING"
        elif k == "WORLDPOST":
            labels[i] = "WORLD NEWS"
        elif k == "COLLEGE":
            labels[i] = "EDUCATION"
        elif k == "TASTE":
            labels[i] = "FOOD & DRINK"
        elif k == "GREEN":
            labels[i] = "ENVIRONMENT"
    
    return labels