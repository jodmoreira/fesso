from transformers import GPT2TokenizerFast
import nltk
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import db_handler
import pandas as pd
import re

pd.options.display.max_columns = None
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

def tokens_handler(text: str) -> int:
    """count the number of tokens in a string"""
    tokens = tokenizer.encode(text)
    num_tokens = len(tokens)
    return tokens, num_tokens

def meta_text_handler(row) -> int:
    """
    Calculate the length of a concatenated string of label, title, sub_title, and date_published
    Parameters:
    df (pd.DataFrame): dataframe with label, title, sub_title, and date_published columns
    
    Returns:
    int: the length of the concatenated string after being encoded with the tokenizer
    """

    label = row["label"].replace("Descrição de chapéu","")
    title = row["title"]
    sub_title = row["sub_title"]
    date_published = row["date_published"].replace("\n","")
    label_str = f"rotulo: {label}\n"
    title_str = f"titulo: {title}\n"
    sub_title_str = f"sub-titulo: {sub_title}\n"
    date_published_str = f"data de publicação: {date_published}\n"
    post_meta_text = f"{label_str}{title_str}{sub_title_str}{date_published_str}conteúdo da matéria: "
    post_meta_text_tokens, post_meta_text_lenght = tokens_handler(post_meta_text)
    return post_meta_text, post_meta_text_lenght

def slice_text(df: pd.DataFrame, non_body: pd.Series, 
               non_body_lenght: pd.Series) -> pd.Series:
    max_len = 1015
    chunks = []
    texts = df["post_content"]
    for index, text in texts.items():
        tokens, num_tokens = tokens_handler(text)
        non_body = df.loc[index, "post_meta_text"]
        non_body_lenght = df.loc[index, "post_meta_text_lenght"]
        start = 0
        end = min(max_len, (num_tokens - non_body_lenght))
        while start < num_tokens:
            chunk = tokenizer.decode(tokens[start:end])
            chunk = f"{non_body}{chunk}"
            chunk = re.sub(' +', ' ', chunk)
            chunks.append(chunk)
            start = end
            end = min((end + max_len), num_tokens)
    output = pd.Series(chunks)
    return output

if __name__ == "__main__":
    training_data = db_handler.read_table_posts()
    df = pd.DataFrame(training_data)
    df[['post_meta_text', 'post_meta_text_lenght']] = df.apply(meta_text_handler, axis=1, result_type="expand")
    processed_text = slice_text(df, df["post_meta_text"], df["post_meta_text_lenght"])
    processed_text.to_csv("processed_text.csv", index=False)