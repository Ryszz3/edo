# import base64
#
# from google import genai
# from openai import OpenAI
# import os
#
# from edo.settings import BASE_DIR
#
# def excel_to_csv(path):
#
#
#
# def consolidate_excel(path_1, path_2):
#     path_1 = BASE_DIR / path_1
#     path_2 = BASE_DIR / path_2
#     print(path_1)
#     print(path_2)
#     if os.path.isfile(path_1) and os.path.isfile(path_2):
#         client = OpenAI(
#
#             base_url="https://api.proxyapi.ru/openai/v1",
#         )
#
#         def encode_file(path: str):
#             with open(path, "rb") as f:
#                 encoded = base64.b64encode(f.read()).decode("utf-8")
#
#             return (
#                     "data:"
#                     "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#                     ";base64,"
#                     + encoded
#             )
#
#         file1_base64 = encode_file(path_1)
#         file2_base64 = encode_file(path_2)
#
#         response = client.responses.create(
#             model="gpt-4o",
#             input=[
#                 {
#                     "role": "user",
#                     "content": [
#                         {
#                             "type": "input_file",
#                             "filename": str(path_1).split("/")[-1],
#                             "file_data": file1_base64,
#                         },
#                         {
#                             "type": "input_file",
#                             "filename": str(path_2).split("/")[-1],
#                             "file_data": file2_base64,
#                         },
#                         {
#                             "type": "input_text",
#                             "text": "проанализируй данные и объедини их, пришли мне результат в csv формате",
#                         },
#                     ],
#                 }
#             ],
#         )
#         print(response.output_text)
#
# p_1 = 'uploads/excel/Лист_Microsoft_Excel.xlsx'
# p_2 = 'uploads/excel/Лист_Microsoft_Excel_vEDG9JF.xlsx'
#
# consolidate_excel(p_1, p_2)
