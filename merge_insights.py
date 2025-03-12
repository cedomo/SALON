import os
from ChatGPT import gpt_completion as llm

insights_path = './insights/'

get_completion_from_msg = llm.get_completion_from_msg_with_turbo
def merge_insights(files):
    """
    Merge the content of multiple insight files into one.
    
    Args:
        files (list): List of file names containing insights to be merged.
        
    Returns:
        str: The merged insights content.
    """
    combined_insights = ""
    
    for file in files:
        file_path = os.path.join(insights_path, file)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                combined_insights += f.read() + "\n\n"
        else:
            print(f"Warning: The file {file} does not exist.")
     
    prompt = f"Read through the following paper insights and consider which of them are clear and actionable, paying particular attention to those that appear multiple times in these insights, and then give an optimized insight that combines these insights for analyzing sentiment in software engineering texts. Please answer within 300 words.\n\n{combined_insights}"
    
    # Call the GPT model to process the insights and generate a merged response
    messages = [{"role": "user", "content": prompt}]
    merged_insight = get_completion_from_msg(messages)
    
    return merged_insight.strip()

def save_merged_insights(merged_content, output_file_name):
    """
    Save the merged insights into a new file.
    
    Args:
        merged_content (str): The content to be saved.
        output_file_name (str): The name of the file where the content will be saved.
    """
    with open(os.path.join(insights_path, output_file_name), 'w', encoding='utf-8') as f:
        f.write(merged_content)
    print(f"Merged insights saved to {output_file_name}")

def main():
    # List of insight files to be merged
    insight_files = [
        #"Q3_1.txt", "Q3_2.txt", "Q3_3.txt", "Q3_4.txt", "Q3_5.txt","Q3_6.txt",
        #"Q3_7.txt","Q3_8.txt", "Q3_9.txt", "Q3_10.txt","Q3_11.txt", "Q3_12.txt","Q3_13.txt"
        "Q3_3.txt", "Q3_4.txt", "Q3_1.txt", "Q3_6.txt", "Q3_5.txt","Q3_8.txt",
        "Q3_2.txt","Q3_9.txt", "Q3_7.txt", "Q3_11.txt","Q3_10.txt", "Q3_13.txt","Q3_12.txt"
        #"Q3(free)_3.txt", "Q3(free)_4.txt", "Q3(free)_1.txt","Q3(free)_6.txt", "Q3(free)_5.txt", "Q3(free)_8.txt",
        #"Q3(free)_2.txt", "Q3(free)_9.txt", "Q3(free)_7.txt", "Q3(free)_11.txt", "Q3(free)_10.txt", "Q3(free)_13.txt", "Q3(free)_12.txt"
        #"Q1_3.txt", "Q1_4.txt", "Q1_1.txt", "Q1_6.txt", "Q1_5.txt", "Q1_8.txt",
        #"Q1_2.txt", "Q1_9.txt", "Q1_7.txt", "Q1_11.txt", "Q1_10.txt", "Q1_13.txt", "Q1_12.txt"
        #"Q1_1.txt", "Q1_2.txt", "Q1_3.txt", "Q1_4.txt", "Q1_5.txt","Q1_6.txt",
        #"Q1_7.txt","Q1_8.txt", "Q1_9.txt", "Q1_10.txt","Q1_11.txt", "Q1_12.txt","Q1_13.txt"
    ]

    merged_content = merge_insights(insight_files)
    
    # Save the merged content to a new file
    output_file_name = "Q7_923.txt"
    save_merged_insights(merged_content, output_file_name)

if __name__ == '__main__':
    main()
