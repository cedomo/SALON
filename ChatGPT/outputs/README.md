# README

This folder stores all the results of experiments mentioned in the essay. The name of each result is formatted like below:

```
(extraction model name)_(classification model name)_(base prompt)
```

To be more specific, *extraction model name* refers to the LLM model we use to extract the insights from essays; *classification model name* refers to the LLM model we use to execute the classification tasks; *base prompt* refers to the prompt we enhance with the insight.

In each folder, we stores the *.csv* and *.txt* files of each experiment. *px.y* in the name represents different combinations of questions and essays. *x* represents the question index (Q1 or Q3), while *y* represents the essay index(the order is slightly different from that in our essay). In particular, *px.y* represent the integrated insight when *x* is 4.

The paper mapping  index during development:

1. "SentiStrength-SE- Exploiting domain specificity for improved sentiment analysis in software engineering text.pdf"
2. "Exploiting the Unique Expression for Improved Sentiment Analysis in Software Engineering Text.pdf"
3. "SentiCR- A Customized Sentiment Analysis Tool for Code Review Interactions.pdf"
4. "Entity-Level Sentiment Analysis of Issue Comments.pdf"
5. "SEntiMoji-An Emoji-Powered Learning Approach for Sentiment Analysis in Software Engineering.pdf"
6. "Sentiment Polarity Detection for Software Development.pdf"
7. "Assessment of off-the-shelf SE-specific sentiment analysis tools_ An extended replication study .pdf"
8. "Can We Use SE-specific Sentiment Analysis Tools in a Cross-Platform Setting_.pdf"
9. _"Development and Application of Sentiment Analysis Tools in Software Engineering_ A Systematic Literature Review.pdf"
10. "Incorporating Pre-trained Transformer Models into TextCNN for Sentiment Analysis on Software Engineering Texts.pdf"
11. "Opinion Mining for Software Development_ A Systematic Literature Review.pdf"
12. "Revisiting Sentiment Analysis for Software Engineering in the Era of Large Language Models.pdf"
13. "“Looks Good To Me ;-)__ Assessing Sentiment Analysis Tools for Pull Request Discussions.pdf"
