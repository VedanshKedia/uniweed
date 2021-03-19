import pandas as pd

df = pd.read_excel("alert.xlsx", index_col = False)
 
def message(code, language_code):
    df_code = df[df.code==code]
    df_lang = df_code[df_code.language==language_code]
    alert_message = df_lang['message'].iloc[0]
    print("message= ", alert_message)
    return alert_message
    
    