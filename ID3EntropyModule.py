import math

"""DESCRIPTION
     ID3 algorithm allows to solve classification problems using entropy
       This module only calculates the entropy and gain of a data column
"""
def entropy(ClassList,X,Y):
    """
    DESCRIPTION
      Entropy Calculation for ID3 Algorithm
        Entropy finds only H(s)
    :param ClassList: [1,1,2,1,2]
    :param X: One of the values ​​in the list Sample: 1
    :param Y: Other Value in the List Sample: 2
    :return: HS
    """

    ClassListTotal = float(len(ClassList))
    ClassListSayX  = 0
    ClassListSayY  = 0

    for i in ClassList:
        if (i == X):
            ClassListSayX += 1
        elif(i == Y):
            ClassListSayY += 1

    print("|ClassListX| = ",ClassListSayX)
    print("|ClassListY| = ",ClassListSayY)
    print("|ClassListT| = ",ClassListTotal)

    ClassListXProbability = ClassListSayX / ClassListTotal
    ClassListYProbability = ClassListSayY / ClassListTotal

    print("|Cx Probability| = ",ClassListXProbability)
    print("|Cy Probability| = ",ClassListYProbability)

    HS = (-1) * ((ClassListXProbability * math.log(ClassListXProbability,2)) + ((ClassListYProbability * math.log(ClassListYProbability,2))))
    return HS

def tripleFeatureGain(AttributeList,ClassList,A1,A2,A3,C1,C2,HS):
    """
    DESCRIPTION
     This operation is repeated for all other attributes, and the maximum gain value is selected as the root node.
      Calculated three-variable list of earnings
    :param AttributeList: [1,2,3,2,1]
    :param ClassList: [1,1,2,1,2]
    :param A1: Other Value in the List Sample: 1 (AttributeList)
    :param A2: Other Value in the List Sample: 2 (AttributeList)
    :param A3: Other Value in the List Sample: 3 (AttributeList)
    :param C1: Other Value in the List Sample: 1 (ClassList)
    :param C2: Other Value in the List Sample: 2 (ClassList)
    :return: Gain(AttributeList,ClassList)
    """
    AttributeListTotal = float(len(AttributeList))
    AttributeA1Say = 0
    AttributeA2Say = 0
    AttributeA3Say = 0

    for i in AttributeList:
        if(i == A1):
            AttributeA1Say += 1
        elif(i == A2):
            AttributeA2Say += 1
        elif(i == A3):
            AttributeA3Say += 1

    print("|Attribute {}| = ".format(A1),AttributeA1Say)
    print("|Attribute {}| = ".format(A2),AttributeA2Say)
    print("|Attribute {}| = ".format(A3),AttributeA3Say)
    print("|AttributeListTotal| = ",AttributeListTotal)

    AttributeA1_1 = 0
    AttributeA1_2 = 0
    AttributeA2_1 = 0
    AttributeA2_2 = 0
    AttributeA3_1 = 0
    AttributeA3_2 = 0

    for i in range(len(AttributeList)):
        if(AttributeList[i] == A1):
            if(ClassList[i] == C1):
                AttributeA1_1 += 1
        if(AttributeList[i] == A1):
            if(ClassList[i] == C2):
                AttributeA1_2 += 1
        if(AttributeList[i] == A2):
            if(ClassList[i] == C1):
                AttributeA2_1 += 1
        if(AttributeList[i] == A2):
            if(ClassList[i] == C2):
                AttributeA2_2 += 1
        if(AttributeList[i] == A3):
            if(ClassList[i] == C1):
                AttributeA3_1 += 1
        if(AttributeList[i] == A3):
            if(ClassList[i] == C2):
                AttributeA3_2 += 1

    print("--------------------------------------")
    print(" {} -> {} ".format(A1,C1),AttributeA1_1)
    print(" {} -> {} ".format(A1,C2),AttributeA1_2)
    print("--------------------------------------")
    print(" {} -> {} ".format(A2,C1),AttributeA2_1)
    print(" {} -> {} ".format(A2,C2),AttributeA2_2)
    print("--------------------------------------")
    print(" {} -> {} ".format(A3,C1),AttributeA3_1)
    print(" {} -> {} ".format(A3,C2),AttributeA3_2)
    print("--------------------------------------")

    ProbabilityAttributeA1_1 = (AttributeA1_1 / AttributeA1Say)
    ProbabilityAttributeA1_2 = (AttributeA1_2 / AttributeA1Say)
    ProbabilityAttributeA2_1 = (AttributeA2_1 / AttributeA2Say)
    ProbabilityAttributeA2_2 = (AttributeA2_2 / AttributeA2Say)
    ProbabilityAttributeA3_1 = (AttributeA3_1 / AttributeA3Say)
    ProbabilityAttributeA3_2 = (AttributeA3_2 / AttributeA3Say)

    CalculateAttributeA1 = (-1) * ((ProbabilityAttributeA1_1 * math.log(ProbabilityAttributeA1_1,2)) + ((ProbabilityAttributeA1_2 * math.log(ProbabilityAttributeA1_2,2))))
    CalculateAttributeA2 = (-1) * ((ProbabilityAttributeA2_1 * math.log(ProbabilityAttributeA2_1,2)) + ((ProbabilityAttributeA2_2 * math.log(ProbabilityAttributeA2_2,2))))
    CalculateAttributeA3 = (-1) * ((ProbabilityAttributeA3_1 * math.log(ProbabilityAttributeA3_1,2)) + ((ProbabilityAttributeA3_2 * math.log(ProbabilityAttributeA3_2,2))))

    print("{} {} = ".format("Weighted Average",A1),CalculateAttributeA1)
    print("{} {} = ".format("Weighted Average",A2),CalculateAttributeA2)
    print("{} {} = ".format("Weighted Average",A3),CalculateAttributeA3)

    HSX = (((AttributeA1Say/AttributeListTotal)*(CalculateAttributeA1)) + ((AttributeA2Say/AttributeListTotal)*(CalculateAttributeA2)) + ((AttributeA3Say/AttributeListTotal)*(CalculateAttributeA3)))
    result = HS - HSX

    return result
