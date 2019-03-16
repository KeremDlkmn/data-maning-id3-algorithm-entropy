# ID3 Algorithm - Calculate Entropy And Gain <br />
ID3 algorithm allows to solve classification problems using entropy. <br />
This module only calculates the entropy and gain of a data column <br />
**entropy** List elements must be two different elements <br />
**tripleFeatureGain** List elements must be three different elements <br />
## What is Entropy <br />
**Entropy** To describe entropy in a single word, the most appropriate word to be used for the definition will be irregularity(disorder) Ent.<br />
**---------------------------------------------------------------------** <br />
**Now, Let's look at Shannon's formula for entropy calculation**<br />
**---------------------------------------------------------------------** <br />
**m:** Number of Entropy to calculate<br/>
**pi:** Probability of i<br/>
![Shannon's Formula](https://cdn-images-1.medium.com/max/1760/1*_Sj7YkkUJSOzDRv9_DATlQ.png) <br />
## What is Gain <br />
**Gain** The decrease in entropy is expressed as gain. <br />
**---------------------------------------------------------------------** <br />
**Now, look at the formula of Gain**<br />
**---------------------------------------------------------------------** <br />
![Gain Formula](https://cdn-images-1.medium.com/max/1760/1*4mXO0Zkeh5WUp51k8FHqHg.png) <br />
## How Can I Use? <br />
**Entropy of the Class List** <br />
> import ID3Entropy <br />
> ClassList = [1,1,2,2,1,1,1,2,1,2,1,2,2,1,1,2,1,2,2,2] <br />
> HS = ID3Entropy.entropy(ClassList,1,2) <br/>
> print("{}".format("ClassList Entropy = "),HS) <br />

**Gain of the AttributeList**  <br />

> import ID3Entropy <br />
> ClassList = [1,1,2,2,1,1,1,2,1,2,1,2,2,1,1,2,1,2,2,2] <br />
> AttributeList = [1,3,2,3,1,1,2,2,3,1,3,3,3,2,3,1,3,2,1,3] <br />
> HS = ID3Entropy.entropy(ClassList,1,2) <br />
> print("{}".format("ClassList Entropy = "),HS) <br />
> gain = ID3Entropy.tripleFeatureGain(AttributeList,ClassList,1,2,3,1,2,HS) <br />
> print("{}".format("AttributeList Gain = "),gain) <br />
