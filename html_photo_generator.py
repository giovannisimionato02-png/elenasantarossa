import os
import re

# Ottiene la cartella base (dove risiede questo script html_photo_generator.py)
base_dir = os.path.dirname(os.path.abspath(__file__))

# 1. Configura i percorsi
image_folder = os.path.join(base_dir, 'static', 'opere')
html_file = os.path.join(base_dir, 'index.html')  

valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.avif')

# Funzione per l'ordinamento naturale dei file (1, 2, ..., 9, 10, 11)
def natural_sort_key(filename):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', filename)]

images = sorted(
    [f for f in os.listdir(image_folder) if f.lower().endswith(valid_extensions)],
    key=natural_sort_key
)

# 2. Genera il blocco HTML della galleria
gallery_html = '<div class="galleria">\n'
for index, img in enumerate(images, start=1):
    title = os.path.splitext(img)[0].replace('-', ' ').replace('_', ' ').capitalize()
    
    gallery_html += '    <div class="elemento-galleria">\n'
    gallery_html += '        <div>\n'
    gallery_html += f'            <img src="static/opere/{img}" \n'
    gallery_html += f'                 alt="{title}" \n'
    gallery_html += '                 class="foto-profilo"\n'
    gallery_html += f'                 onclick="document.getElementById(\'modal-{index}\').showModal()">\n'
    gallery_html += '        </div>\n'
    gallery_html += f'        <div class="titolo-foto">{title}</div>\n'
    gallery_html += f'        <dialog id="modal-{index}" onclick="this.close()">\n'
    gallery_html += f'            <img src="static/opere/{img}" alt="{title} ingrandita">\n'
    gallery_html += '        </dialog>\n'
    gallery_html += '    </div>\n'
gallery_html += '</div>'

# 3. Legge e aggiorna il file HTML tra i marcatori <!-- GALLERY_START --> e <!-- GALLERY_END -->
if os.path.exists(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    start_marker = '<!-- GALLERY_START -->'
    end_marker = '<!-- GALLERY_END -->'

    if start_marker in content and end_marker in content:
        start_idx = content.find(start_marker) + len(start_marker)
        end_idx = content.find(end_marker)
        new_content = content[:start_idx] + '\n' + gallery_html + '\n' + content[end_idx:]

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"File '{os.path.basename(html_file)}' aggiornato con successo!")
    else:
        print("I marcatori <!-- GALLERY_START --> e <!-- GALLERY_END --> non sono stati trovati nel file HTML.")
else:
    print(f"File {html_file} non trovato.")