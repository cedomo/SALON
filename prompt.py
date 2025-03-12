# basic SA prompt
def basic_prompt(index, text):
    # From "Sentiment Analysis in the Era of Large Language Models: A Reality Check"
    prompt_0_1 = f'''Please perform Sentiment Classification task. Given the sentence, assign a sentiment label from ['positive','neutral','negative']. Return label only without any other text.\n\nSentence: {text}\nLabel: '''

    # From  "LARGE LANGUAGE MODELS ARE HUMAN-LEVEL PROMPT ENGINEERS"
    # https://github.com/keirp/automatic_prompt_engineer/blob/main/demo.py
    prompt_0_2 = f"""Instruction: write \"positive\" if the input is a positive review, \"neutral\" if the input is a neutral review, and \"negative\" if the input is a negative review.\nInput: {text}\nOutput: """

    prompts = [prompt_0_1, prompt_0_2]
    return prompts[index - 1]


# Enhanced prompt
def enhanced_basic_prompt_1(insight, text):
    prompt = insight \
             + "\n\n" + \
             f"Considering that, please perform Sentiment Classification task. Given the sentence, assign a sentiment label from ['positive','neutral','negative']. Return label only without any other text.\n\nSentence: {text}\nLabel: "
    return prompt


def enhanced_basic_prompt_2(insight, text):
    prompt = insight \
             + "\n\n" + \
             f"Considering that, instruction: write \"positive\" if the input is a positive review, \"neutral\" if the input is a neutral review, and \"negative\" if the input is a negative review.\nInput: {text}\nOutput: "
    return prompt


enhanced_prompt_def_arr = [enhanced_basic_prompt_1, enhanced_basic_prompt_2]


def get_prompt(base_index, def_index, prompt_index, text):
    def_index = int(def_index)
    prompt_index = int(prompt_index)
    if def_index == 0:
        return basic_prompt(prompt_index, text)

    insight_path = 'insights/'
    insight_name = f'Q{def_index}_{prompt_index}.txt'
    with open(insight_path + insight_name, 'r', encoding='utf-8') as file:
        insight = file.read()

    enhanced_prompt = enhanced_prompt_def_arr[base_index - 1]
    return enhanced_prompt(insight, text)
