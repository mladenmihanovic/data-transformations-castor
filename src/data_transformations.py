import pandas as pd

def map_user_guids_to_user_ids(dataFrame):
    df = dataFrame  
    
    df = df.rename(columns={"user_id": "user_guid"})
    df = df.rename(columns={"manager_id": "manager_guid"})

    user_guid_to_id = {guid: idx for idx, guid in enumerate(df["user_guid"].unique(), start=1)}

    df["user_id"] = df["user_guid"].map(user_guid_to_id)
    df["manager_id"] = df["manager_guid"].map(user_guid_to_id)

    df = df.drop(columns=["user_guid", "manager_guid"])
    return df

def obfuscate_data(data_frame, column_name, obfuscate_func):
    df = data_frame.copy()
    df[column_name] = df[column_name].apply(obfuscate_func)
    return df


def transform_date(df, column_name: str, input_date_format, output_date_format) -> str:
    df[column_name] = pd.to_datetime(df[column_name], errors="coerce", utc=True, format=input_date_format)
    df[column_name] = df[column_name].dt.strftime(output_date_format)

    return df
