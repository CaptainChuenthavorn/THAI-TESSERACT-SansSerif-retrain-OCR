import os
import random
import pathlib
import subprocess

training_text_file = 'langdata/tha.training_text'
fontconf_dir = ''
lines = []

with open(training_text_file, 'r',encoding='utf-8') as input_file:
    for line in input_file.readlines():
        lines.append(line.strip())

output_directory = 'tesstrain/data/Prompt-ground-truth'

if not os.path.exists(output_directory):
    os.mkdir(output_directory)

random.shuffle(lines)

count = 10

lines = lines[:count]


#Prompt thin is Prompt weight=255 
prompt_font_list = ['Prompt','Prompt weight=255','Prompt bold','Prompt Italic']
NotoSansThai_font_list = ['Noto Sans Thai','Noto Sans Thai light','Noto Sans Thai Bold']
# font_training_name = []
font_prompt_context=['Normal','Light','Bold','Italic']
for font_index,font_name in enumerate(prompt_font_list):
    line_count = 0
    for line in lines:
        # training_text_file_name = pathlib.Path(training_text_file).stem
        training_font_name = "prompt"
        line_training_text = os.path.join(output_directory, f'{training_font_name}_{font_prompt_context[font_index]}_{line_count}.gt.txt')
        with open(line_training_text, 'w',encoding='utf-8') as output_file:
            output_file.writelines([line])

        file_base_name = f'{training_font_name}_{font_prompt_context[font_index]}_{line_count}'
#work tesseract5
        # subprocess.run([
        #         'text2image',
        #         '--resolution=600',
        #         f'--fontconfig_tmpdir={fontconf_dir}',
        #         f'--font={font_name}',
        #         '--ptsize=16',
        #         f'--text={line_training_text}',
        #         f'--outputbase={output_directory}/{file_base_name}',
        #         '--max_pages=1',
        #         '--strip_unrenderable_words',
        #         '--leading=32',
        #         '--xsize=3500',
        #         '--ysize=700',
        #         # '--char_spacing=1.0',
        #         '--exposure=0',
        #         # '--unicharset_file=langdata/Thai.unicharset'

        # ])
#tesseract 4
        subprocess.run([
                        'text2image',
                        '--resolution=600',
                        f'--fontconfig_tmpdir={fontconf_dir}',
                        f'--font={font_name}',
                        '--ptsize=16',
                        f'--text={line_training_text}',
                        f'--outputbase={output_directory}/{file_base_name}',
                        '--max_pages=2',
                        '--strip_unrenderable_words',
                        '--leading=32',
                        '--xsize=3500',
                        '--ysize=700',
                        # '--char_spacing=1.0',
                        '--exposure=0',
                        # '--unicharset_file=langdata/Thai.unicharset'

        ])
        line_count += 1
