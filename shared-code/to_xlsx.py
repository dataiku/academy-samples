import dataiku
import pandas as pd
import io
import pickle

def dataframe_to_xlsx(input_dataframe, folder_name, output_file_name):
    folder = dataiku.Folder(folder_name)
    folder_infos = folder.get_info()
    if folder_infos["type"] == "S3":
        file = output_file_name + '.xlsx'
        xl_bytes = io.BytesIO()
        
        with pd.ExcelWriter(xl_bytes, engine='openpyxl') as writer:
            input_dataframe.to_excel(writer, index=False, encoding='utf-8')

        with folder.get_writer(file) as fwriter:
            fwriter.write(xl_bytes.getvalue())
    else:
        folder_path = folder.get_path()
        folder_path = folder_path + '/' + output_file_name + '.xlsx'
        writer = pd.ExcelWriter(folder_path, engine='openpyxl')
        input_dataframe.to_excel(writer, index=False, encoding='utf-8')
        
        writer.save()
    
