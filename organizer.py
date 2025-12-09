import os
import shutil

# --- CONFIGURARE ---
# Definim extensiile și folderele destinație
EXTENSION_MAP = {
    'Imagini': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp'],
    'Documente': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.doc'],
    'Video': ['.mp4', '.mkv', '.avi', '.mov'],
    'Muzica': ['.mp3', '.wav', '.flac'],
    'Arhive': ['.zip', '.rar', '.7z', '.tar'],
    'Executabile': ['.exe', '.msi', '.bat']
}

def organize_folder(target_folder):
    """
    Scanează folderul și mută fișierele în sub-foldere bazate pe extensie.
    """
    # Verificăm existența folderului
    if not os.path.exists(target_folder):
        print(f"[EROARE] Folderul '{target_folder}' nu exista!")
        return

    print(f"--- Incepem organizarea in: {target_folder} ---\n")

    # Luăm toate fișierele (excludem folderele)
    files = [f for f in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, f))]
    
    moved_count = 0

    for file in files:
        # Ignorăm scriptul însuși ca să nu se mute singur
        if file == "organizer.py":
            continue

        # Obținem extensia
        _, extension = os.path.splitext(file)
        extension = extension.lower()

        # Căutăm unde trebuie să meargă
        destination_folder = None
        for folder_name, extensions in EXTENSION_MAP.items():
            if extension in extensions:
                destination_folder = folder_name
                break
        
        # Dacă are o categorie cunoscută
        if destination_folder:
            dest_path = os.path.join(target_folder, destination_folder)
            
            # Creăm folderul dacă nu există
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
                print(f"[INFO] Creat folder nou: {destination_folder}")

            # Mutăm fișierul
            try:
                shutil.move(os.path.join(target_folder, file), os.path.join(dest_path, file))
                print(f"[MUTAT] {file} -> {destination_folder}")
                moved_count += 1
            except Exception as e:
                print(f"[EROARE] {file}: {e}")

    print(f"\n--- GATA! Am mutat {moved_count} fisiere. ---")

if __name__ == "__main__":
    # Cerem calea de la utilizator sau folosim folderul curent
    user_input = input("Introdu calea folderului de curatat (sau ENTER pentru folderul curent): ")
    
    target_dir = user_input.strip() if user_input.strip() != "" else "."
    organize_folder(target_dir)
    
    input("\nApasa ENTER pentru a iesi...")