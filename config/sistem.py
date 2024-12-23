import os
import xml.etree.ElementTree as ET
from datetime import datetime
from xml.dom import minidom

# Aquí establecemos BASE_DIR para que siempre apunte a la raíz del proyecto, independientemente de donde esté el script.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Este es el directorio donde está el script (config)
PROJECT_DIR = os.path.dirname(BASE_DIR)  # Esto asegura que 'PROJECT_DIR' es la raíz del proyecto

FILES_DIR = os.path.join(PROJECT_DIR, 'pages')  # Asegura que 'files' esté en la raíz
SITEMAP_FILE = os.path.join(PROJECT_DIR, 'sitemap.xml')  # Asegura que 'sitemap.xml' esté en la raíz

def get_files():
    files = []
    for root, dirs, filenames in os.walk(FILES_DIR):
        for filename in filenames:
            if filename.endswith('.html') or filename.endswith('.php'):
                files.append(os.path.relpath(os.path.join(root, filename), PROJECT_DIR))
    return files

def update_sitemap():
    files = get_files()

    current_date = datetime.now().strftime('%Y-%m-%d')

    urlset = ET.Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    index_url = ET.SubElement(urlset, 'url')
    loc = ET.SubElement(index_url, 'loc')
    loc.text = 'index.html'
    lastmod = ET.SubElement(index_url, 'lastmod')
    lastmod.text = current_date
    priority = ET.SubElement(index_url, 'priority')
    priority.text = '1.00'

    for file in files:
        url = ET.SubElement(urlset, 'url')
        loc = ET.SubElement(url, 'loc')
        loc.text = f'{file}'
        lastmod = ET.SubElement(url, 'lastmod')
        lastmod.text = current_date
        priority = ET.SubElement(url, 'priority')
        priority.text = '0.80'

    tree = ET.ElementTree(urlset)
    xml_str = ET.tostring(urlset, encoding='utf-8', method='xml').decode()

    xml_str = minidom.parseString(xml_str).toprettyxml(indent="    ")

    with open(SITEMAP_FILE, 'w', encoding='utf-8') as f:
        f.write(xml_str)

    print(f'Sitemap actualizado en {SITEMAP_FILE}')

if __name__ == '__main__':
    update_sitemap()
