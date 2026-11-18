import os
import sys
import importlib.util

# Ermittelt den Basispfad (wo menu.py bzw. die EXE ausgeführt wird)
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
    sys.path.append(base_path)  # Wichtig für PyInstaller, damit die Skripte gefunden werden!
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

def run_script_by_path(relative_path, module_name):
    """Lädt ein Python-Skript dynamisch über seinen Pfad relativ zur menu.py."""
    try:
        full_path = os.path.normpath(os.path.join(base_path, relative_path))
        
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Datei nicht gefunden: {full_path}")
            
        spec = importlib.util.spec_from_file_location(module_name, full_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        
        if module_name in sys.modules:
            del sys.modules[module_name]
            
    except Exception as e:
        print(f"\nFehler beim Ausführen von {module_name}: {e}")
        input("\nDrücke Enter, um fortzufahren...")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 40)
        print("      Week3 - MENÜ")
        print("=" * 40)
        print("1) Company name generator")
        print("2) Englishvoc")
        print("3) IMPKA")
        print("4) Projekt")
        print("5) Pysik")
        print("6) Rock_paper_sicors..")
        print("7) Sme")
        print("8) What should i do")
        print("9) Beenden")
        print("=" * 40)
        
        auswahl = input("Bitte eine Option wählen (1-9): ").strip()
        
        if auswahl == "1":
            run_script_by_path("campany name generator.py", "campany name generator")
        elif auswahl == "2":
            run_script_by_path("englishvoc.py", "englishvoc")
        elif auswahl == "3":
            run_script_by_path("IMPKA.py", "IMPKA")
        elif auswahl == "4":
            run_script_by_path("projekt.py", "projekt")
        elif auswahl == "5":
            run_script_by_path("pysik.py", "pysik")
        elif auswahl == "6":
            run_script_by_path("rock_paper_sicors...py", "rock_paper_sicors..")
        elif auswahl == "7":
            run_script_by_path("sme.py", "sme")
        elif auswahl == "8":
            run_script_by_path("what should i do.py", "what should i do")
        elif auswahl == "9":
            print("\nProgramm beendet.")
            break
        else:
            input("\nUngültige Auswahl. Drücke Enter...")
            continue
            
        input("\nDrücke Enter, um zum Menü zurückzukehren...")

if __name__ == "__main__":
    main()
