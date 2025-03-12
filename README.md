# SALON
Project structure：

│ ├── ChatGPT/

│ ├────── outputs/ # The results of different insight prompts in the experiment

│ ├────── gpt_completion.py # How to configure ChatGPT API

│ ├── essays/ 

│ ├── human_labeled/ # Test set and its manual annotation

│ ├── input/ # The pure texts of test set

│ ├── insights/

│ ├── questions/

│ ├── analysis_senti_for_file.py # Main program entry, used to set which prompt to complete the SA4SE tasks

│ ├── data analysis.xlsx # Detailed evaluation data for all experiments

│ ├── evaluate.py

│ ├── insight_extractor.py

│ ├── merge_insights.py # Merge insights from different essays

│ └── prompts.py
