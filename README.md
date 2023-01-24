# fesso
Running GPT model from Open AI direct on terminal

Access https://beta.openai.com/account/api-keys to get new api key. <br>
Store the value safely as a enviroment variable using OPENAI_API_KEY as key.

To generate binary file run pyinstaller.<br>
`python -m pip install pyinstaller`<br>
Run the command to get binary:<br>
`pyinstaller --onefile fesso.py`<br>

To optimize answers to your needs, add substrings such as "**command to**", "**who is**", "**what is**" to the beginning of the prompt.<br>
To have larger or smaller results edit the `--max_tokens` parameter.<br>
It is also possible to try cheaper models such as curie, babbage or ada. Check documentation: <br>
https://beta.openai.com/docs/models/gpt-3