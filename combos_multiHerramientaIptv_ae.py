import os
import datetime
import time
from colorama import Fore, Back, Style, init
import shutil
import urllib.request
import json
import unicodedata
import subprocess
import random
import sys
from tqdm import tqdm
import names
import string
from unidecode import unidecode
import time
try:
    import androidhelper
    droid = androidhelper.Android()
except:
    pass

# Inicializar colorama para colores en la consola
init(autoreset=True)

print('\n\033[93m+------------------------------------+\033[0m')
print('\033[42m\033[30mIdeas originales Angel Exspectrus \033[0m')
print('\033[92mGenerador Múltiple de combos\nMulti herramientas de iptv\033[0m')

# Lista de símbolos para contraseñas (sin comilla simple)
simbolos = ['!', '@', '#', '$', '%']

# Lista de dominios de correo
dominios = ['gmail.com', 'hotmail.com', 'outlook.com']

def obtener_nombre_apellido(capitalize_option):
    # Obtiene nombre y apellido de la API randomuser.me
    try:
        url = 'https://randomuser.me/api/'
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        nombre = unidecode(data['results'][0]['name']['first'])  # Elimina acentos
        apellido = unidecode(data['results'][0]['name']['last'])  # Elimina acentos
        
        # Reemplaza comillas simples y espacios
        nombre = nombre.replace("'", "").replace(" ", "")
        apellido = apellido.replace("'", "").replace(" ", "")
        
        # Aplica capitalización según la opción del usuario
        if capitalize_option == '4':  # Mezclar todas las opciones
            capitalize_option = random.choice(['1', '2', '3'])
        
        if capitalize_option == '1':  # Todo en minúsculas
            nombre = nombre.lower()
            apellido = apellido.lower()
        elif capitalize_option == '2':  # Primera letra mayúscula
            nombre = nombre.capitalize()
            apellido = apellido.capitalize()
        elif capitalize_option == '3':  # Todo en mayúsculas
            nombre = nombre.upper()
            apellido = apellido.upper()
        
        return nombre, apellido
    except Exception as e:
        print(f"\033[91mError al obtener datos de la API: {e}. Saltando este correo...\033[0m")
        return None, None  # Devuelve None si falla

def generar_fecha_nacimiento():
    # Genera una fecha de nacimiento aleatoria
    year = random.randint(1900, 2050)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return year, f"{year}{month:02d}{day:02d}"

def generar_correo_contrasena(dominio_seleccionado, capitalize_option, email_number_option, password_number_option, name_option, use_symbols, first_letter_option):
    # Genera un correo electrónico y contraseña según las opciones del usuario
    nombre, apellido = obtener_nombre_apellido(capitalize_option)
    
    if nombre is None or apellido is None:
        return None
    
    year, _ = generar_fecha_nacimiento()
    
    # Selecciona dominio
    if dominio_seleccionado == 'todos':
        dominio = random.choice(dominios)
    else:
        dominio = dominio_seleccionado
    
    # Selecciona número para el correo
    if email_number_option == '3':
        email_number_choice = random.choice(['1', '2', '4'])
    else:
        email_number_choice = email_number_option
    
    if email_number_choice == '1':
        numero_correo = str(year)
    elif email_number_choice == '2':
        numero_correo = str(random.randint(10, 99))
    else:
        numero_correo = ''
    
    # Selecciona componente de nombre para el correo
    if name_option == '4':
        name_choice = random.choice(['nombre', 'apellido', 'ambos'])
    else:
        name_choice = {'1': 'nombre', '2': 'apellido', '3': 'ambos'}[name_option]
    
    # Construye el correo
    if name_choice == 'nombre':
        correo = f"{nombre}{numero_correo}@{dominio}"
    elif name_choice == 'apellido':
        correo = f"{apellido}{numero_correo}@{dominio}"
    else:
        correo = f"{nombre}{apellido}{numero_correo}@{dominio}"
    
    correo = correo.replace("'", "")
    
    # Selecciona número para lacontraseña
    if password_number_option == '3':
        password_number_choice = random.choice(['1', '2', '4'])
    else:
        password_number_choice = password_number_option
    
    if password_number_choice == '1':
        numero_contrasena = str(year)
    elif password_number_choice == '2':
        numero_contrasena = str(random.randint(1000, 9999))
    else:
        numero_contrasena = ''
    
    # Aplica capitalización a la primera letra de la contraseña
    if first_letter_option == '3':
        first_letter_choice = random.choice(['1', '2'])  # Corrección del error
    else:
        first_letter_choice = first_letter_option
    
    if first_letter_choice == '1':
        nombre_contrasena = nombre.lower()
    else:
        nombre_contrasena = nombre.capitalize()
    
    nombre_contrasena = nombre_contrasena.replace(" ", "").replace("'", "")
    
    # Decide si incluir símbolos en la contraseña
    if use_symbols == '1':
        simbolo = random.choice(simbolos)
        contrasena = f"{nombre_contrasena}{numero_contrasena}{simbolo}"
    else:
        contrasena = f"{nombre_contrasena}{numero_contrasena}"
    
    contrasena = contrasena.replace("'", "")
    
    return f"{correo}:{contrasena}"

def generador_correos():
    # Menú para el generador de correos
    print('\n\033[93m+------------------------------------+\033[0m')
    print("\033[32mGenerador de correos electrónicos\033[0m")
    print("1. Gmail")
    print("2. Hotmail")
    print("3. Outlook")
    print("4. Todos")
    print('\033[93m+------------------------------------+\033[0m')

    opcion = input("\nOpción (1-4): ")

    if opcion == '1':
        dominio = 'gmail.com'
    elif opcion == '2':
        dominio = 'hotmail.com'
    elif opcion == '3':
        dominio = 'outlook.com'
    elif opcion == ' coincidentally':
        dominio = 'todos'
    else:
        print("Opción inválida, usando 'todos' por defecto.")
        dominio = 'todos'
    
    print('\n\033[93m+------------------------------------+\033[0m')
    print("\033[32mNombres y apellidos:\033[0m")
    print("1. Todo en minúsculas")
    print("2. Primera letra en mayúscula")
    print("3. Todo en mayúsculas")
    print("4. Mezclar todos")
    print('\033[93m+------------------------------------+\033[0m')
    capitalize_option = input("\nOpción (1-4): ")
    
    if capitalize_option not in ['1', '2', '3', '4']:
        print("Opción inválida, usando minúsculas por defecto.")
        capitalize_option = '1'
    
    print('\n\033[93m+------------------------------------+\033[0m')
    print("\033[32mUsar números en el correo:\033[0m")
    print("1. Usar año de nacimiento")
    print("2. Usar números aleatorios")
    print("3. Mezclar todos")
    print("4. No usar nada")
    print('\033[93m+------------------------------------+\033[0m')
    email_number_option = input("\nOpción (1-4): ")
    
    if email_number_option not in ['1', '2', '3', '4']:
        print("Opción inválida, usando números aleatorios por defecto.")
        email_number_option = '2'
    
    print('\n\033[93m+------------------------------------+\033[0m')
    print("\033[32mOpciones para contraseña:\033[0m")
    print("1. Usar año de nacimiento")
    print("2. Usar números aleatorios")
    print("3. Mezclar todos")
    print("4. No usar nada")
    print('\033[93m+------------------------------------+\033[0m')
    password_number_option = input("\nOpción (1-4): ")
    
    if password_number_option not in ['1', '2', '3', '4']:
        print("Opción inválida, usando números aleatorios por defecto.")
        password_number_option = '2'

    print('\n\033[93m+------------------------------------+\033[0m')
    print("\033[32mPrimera letra de la contraseña:\033[0m")
    print("1. Minúscula")
    print("2. Mayúscula")
    print("3. Mezclar ambas")
    print('\033[93m+------------------------------------+\033[0m')
    first_letter_option = input("\nOpción (1-3): ")
    
    if first_letter_option not in ['1', '2', '3']:
        print("Opción inválida, usando minúscula por defecto.")
        first_letter_option = '1'
    
    print('\n\033[93m+------------------------------------+\033[0m')
    print("\033[32mUsar símbolos en la contraseña:\033[0m")
    print("1. Usar símbolos")
    print("2. No usar símbolos")
    print('\033[93m+------------------------------------+\033[0m')
    use_symbols = input("\nOpción (1-2): ")
    
    if use_symbols not in ['1', '2']:
        print("Opción inválida, no se usarán símbolos por defecto.")
        use_symbols = '2'
    
    print('\n\033[93m+------------------------------------+\033[0m')
    print("\033[32mOpciones para el correo:\033[0m")
    print("1. Solo nombre")
    print("2. Solo apellido")
    print("3. Nombre y apellido")
    print("4. Todos")
    print('\033[93m+------------------------------------+\033[0m')
    name_option = input("\nOpción (1-4): ")
    
    if name_option not in ['1', '2', '3', '4']:
        print("Opción inválida, usando 'Nombre y apellido' por defecto.")
        name_option = '3'
    
    try:
        cantidad = int(input("\n¿Cuántos correos desea generar?: "))
        nombre_archivo = input("\nIngrese el nombre del archivo: ") + ".txt"
    except ValueError:
        print("Cantidad inválida, se generarán 10 correos por defecto.")
        cantidad = 10
        nombre_archivo = "correos_generados.txt"
    
    # Ruta para guardar en la carpeta /sdcard/combo/
    carpeta = "/sdcard/combo/"
    ruta = os.path.join(carpeta, nombre_archivo)
    
    # Crear la carpeta si no existe
    try:
        os.makedirs(carpeta, exist_ok=True)
    except Exception as e:
        print(f"Error al crear la carpeta /sdcard/combo/: {e}")
        return
    
    correos_generados = 0
    intentos = 0
    max_intentos = cantidad * 2
    
    try:
        with open(ruta, 'w') as archivo:
            with tqdm(total=cantidad, desc="Generando correos", unit="correo") as pbar:
                while correos_generados < cantidad and intentos < max_intentos:
                    linea = generar_correo_contrasena(dominio, capitalize_option, email_number_option, password_number_option, name_option, use_symbols, first_letter_option)
                    intentos += 1
                    if linea:
                        archivo.write(linea + '\n')
                        correos_generados += 1
                        pbar.update(1)
                        print(f" Correos restantes: {cantidad - correos_generados}", end='\r')
        print(f"\n\033[32mSe han generado {correos_generados} correos y guardado en {ruta}\033[0m")
        if correos_generados < cantidad:
            print(f"Advertencia: Solo se generaron {correos_generados} de {cantidad} correos solicitados debido a errores en la API.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def generar_combinaciones(nombres_archivo, combos_archivo):
    # Genera combinaciones a partir de archivos de nombres y combos
    with open(nombres_archivo, 'r') as f:
        nombres = [nombre.strip() for nombre in f]

    with open(combos_archivo, 'r') as f:
        combos = [combo.strip() for combo in f]

    resultados = []
    num_omitidas = 0
    for nombre in nombres:
        for combo in combos:
            resultado = combo.replace('usuario', nombre)
            if 'usuario' in resultado:
                num_omitidas += 1
            else:
                resultados.append(resultado)

    num_combinaciones = len(resultados)
    return resultados, num_combinaciones, num_omitidas

def remove_accents(text):
    # Elimina acentos de un texto
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')

def get_names(gender, quantity):
    # Obtiene nombres de la API randomuser.me según género y cantidad
    if gender == 'both':
        url = f"https://randomuser.me/api/?results={quantity}&nat=us,es,fr,gb"
    else:
        url = f"https://randomuser.me/api/?results={quantity}&gender={gender}&nat=us,es,fr,gb"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return [(remove_accents(user['name']['first']), 
                     remove_accents(user['name']['last'])) 
                    for user in data['results']]
    except Exception as e:
        print(f"Error al obtener nombres: {e}")
        return []

def format_name(name, case_option):
    # Formatea un nombre según la opción de capitalización
    if case_option == 'upper':
        return name.capitalize()
    elif case_option == 'lower':
        return name.lower()
    else:
        return random.choice([name.capitalize(), name.lower()])

def format_output(first_name, last_name, case_option, output_type, combo_option='both'):
    # Formatea la salida de nombres y apellidos
    formatted_first = format_name(first_name, case_option)
    formatted_last = format_name(last_name, case_option)
    
    if output_type == 'first':
        return [formatted_first]
    elif output_type == 'last':
        return [formatted_last]
    else:
        if combo_option == 'first_last':
            return [f"{formatted_first}{formatted_last}"]
        elif combo_option == 'last_first':
            return [f"{formatted_last}{formatted_first}"]
        else:
            return [f"{formatted_first}{formatted_last}", f"{formatted_last}{formatted_first}"]

def print_green_box(title, options):
    # Imprime un cuadro verde con título y opciones
    fixed_width = 38
    title = (title[:fixed_width-1] + '…') if len(title) > fixed_width else title.ljust(fixed_width)
    print(f"\033[32m┌{'─' * (fixed_width + 2)}┐\033[0m")
    print(f"\033[32m│ \033[93m{title}\033[32m │\033[0m")
    print(f"\033[32m├{'─' * (fixed_width + 2)}┤\033[0m")
    for opt in options:
        opt = (opt[:fixed_width-1] + '…') if len(opt) > fixed_width else opt.ljust(fixed_width)
        print(f"\033[32m│ {opt} │\033[0m")
    print(f"\033[32m└{'─' * (fixed_width + 2)}┘\033[0m")

def progress_bar(seconds):
    # Muestra una barra de progreso
    bar_length = 40
    for i in range(100):
        time.sleep(seconds/100)
        if i < 33:
            print(f"\r{Fore.RED}[{'●' * round(i*bar_length//100)}{'-' * (bar_length - round(i*bar_length//100))}]", end="", flush=True)
        elif i < 66:
            print(f"\r{Fore.YELLOW}[{'●' * round(i*bar_length//100)}{'-' * (bar_length - round(i*bar_length//100))}]", end="", flush=True)
        else:
            print(f"\r{Fore.GREEN}[{'●' * round(i*bar_length//100)}{'-' * (bar_length - round(i*bar_length//100))}]", end="", flush=True)
    print(f"\r{Fore.GREEN}[{'●' * bar_length}]")
    print(f"Proceso terminado")

def generador_nombres():
    # Generador de nombres
    gender_options = {'1': 'male', '2': 'female', '3': 'both'}
    print_green_box("Opciones de género disponibles:", ["1. Hombre", "2. Mujer", "3. Ambos"])
    gender_choice = input("\nSeleccione género (1, 2, 3): ")
    while gender_choice not in gender_options:
        print("Opción inválida. Use 1, 2 o 3.")
        gender_choice = input("Seleccione género (1, 2, 3): ")
    gender = gender_options[gender_choice]

    try:
        quantity = int(input("\n\033[93mCantidad de nombres a generar:\033[0m "))
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
    except ValueError as e:
        print(f"Error: {e if str(e) else 'Ingrese un número válido.'}")
        return

    case_options = {'1': 'upper', '2': 'lower', '3': 'both'}
    print_green_box("Formato de la primera letra:", ["1. Mayúscula", "2. Minúscula", "3. Ambas"])
    case_choice = input("\nSeleccione formato (1, 2, 3): ")
    while case_choice not in case_options:
        print("Opción inválida. Use 1, 2 o 3.")
        case_choice = input("Seleccione formato (1, 2, 3): ")
    case_option = case_options[case_choice]

    output_options = {'1': 'first', '2': 'last', '3': 'combo'}
    print_green_box("Combinación de nombres o apellidos:", ["1. Solo nombres", "2. Solo apellidos", "3. Ambos"])
    output_choice = input("\nSeleccione (1, 2, 3): ")
    while output_choice not in output_options:
        print("Opción inválida. Use 1, 2 o 3.")
        output_choice = input("Seleccione (1, 2, 3): ")
    output_type = output_options[output_choice]

    combo_option = 'both'
    if output_type == 'combo':
        combo_options = {'1': 'first_last', '2': 'last_first', '3': 'both'}
        print_green_box("Combinación con nombres y apellidos:", ["1. Nombre/Apellido", "2. Apellido/Nombre", "3. Ambas"])
        combo_choice = input("\nSeleccione combinación (1, 2, 3): ")
        while combo_choice not in combo_options:
            print("Opción inválida. Use 1, 2 o 3.")
            combo_choice = input("Seleccione combinación (1, 2, 3): ")
        combo_option = combo_options[combo_choice]

    file_name = input("\nNombre para guardar el archivo (sin .txt): ").strip()
    if not file_name:
        file_name = "nombres_generados"
    file_name += ".txt"

    print("\nProcesando nombres...")
    progress_bar(5)

    names_list = get_names(gender, quantity)
    if not names_list:
        print("\nNo se pudieron obtener nombres. Finalizando.")
        return

    formatted_names = []
    for first_name, last_name in names_list:
        result = format_output(first_name, last_name, case_option, output_type, combo_option)
        formatted_names.extend(result)

    output_dir = "/sdcard/combos_user"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except Exception as e:
        print(f"Error al crear la carpeta {output_dir}: {e}")
        return

    output_path = os.path.join(output_dir, file_name)
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            for name in formatted_names:
                f.write(name + '\n')
        print(f"\n\033[32mNombres guardados en: {output_path}\033[0m")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def generar_combo(rname, rlastname, num, combo_option):
    if combo_option == "1":
        all1 = f"{rname}{num}"
        alln = f"{all1}:{rname}"
        all2 = f"{rlastname}{num}"
        allf = f"{all2}:{rlastname}"
    elif combo_option == "2":
        all1 = f"{rname}"
        alln = f"{all1}:{rname}{num}"
        all2 = f"{rlastname}"
        allf = f"{all2}:{rlastname}{num}"
    else:
        all1 = f"{rname}{num}"
        alln = f"{all1}:{rname}{num}"
        all2 = f"{rlastname}{num}"
        allf = f"{all2}:{rlastname}{num}"
    return all1, alln, all2, allf


def generate_random_combos(user_length, pass_length, include_uppercase=True, include_lowercase=True, numbers=True, birth_year=False, year_position='right'):
    charset = ''
    if include_uppercase:
        charset += string.ascii_uppercase
    if include_lowercase:
        charset += string.ascii_lowercase
    if numbers and not birth_year:
        charset += string.digits
    if not charset:
        charset = string.ascii_lowercase

    username = ''.join(random.choice(charset) for _ in range(user_length))
    password = ''.join(random.choice(charset) for _ in range(pass_length))

    if birth_year:
        year = str(random.randint(1900, 2020))
        if year_position == 'left':
            username = username + year
        elif year_position == 'right':
            password = password + year
        elif year_position == 'both':
            username = username + year
            password = password + year
    return username, password

def generador_combos():
    output_dir = "/sdcard/combos_user"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print('\n\033[93m+--------------------------------------+\033[0m')
    print("\033[93m|\033[0m\033[42m\033[30m      Menú de generador de Combos     \033[0m\033[93m|\033[0m")
    print('\033[93m+--------------------------------------+\033[0m')
    print("\033[93m|\033[0m1.- User:Pass (Num. de 2000 a 2050)   \033[93m|\033[0m")
    print("\033[93m|\033[0m2.- User:Pass (Nombre-Nombre)         \033[93m|\033[0m")
    print("\033[93m|\033[0m3.- User:Pass (Núm. de 1 a 499)       \033[93m|\033[0m")
    print("\033[93m|\033[0m4.- User:Pass (Núm. de 500 a 999)     \033[93m|\033[0m")
    print("\033[93m|\033[0m5.- User:Pass (Alfanuméricos)         \033[93m|\033[0m")
    print("\033[93m|\033[0m6.- User:Pass (Año de Nacimiento)     \033[93m|\033[0m")
    print("\033[93m|\033[0m7.- User:Pass (2023 al 2026)          \033[93m|\033[0m")
    print("\033[93m|\033[0m8.- User:Pass (Núm. de 111 a 999)     \033[93m|\033[0m")
    print("\033[93m|\033[0m9.- User:Pass (Núm. de 123 a 12345)   \033[93m|\033[0m")
    print("\033[93m|\033[0m10.- User:Numero (12345..Random)      \033[93m|\033[0m")
    print("\033[93m|\033[0m11.- Combos numéricos (numero:número) \033[93m|\033[0m")
    print('\033[93m+--------------------------------------+\033[0m')

    menu = input("\nIngrese su elección: ")

    if menu == "11":

        RED = "\033[91m"
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        CYAN = "\033[96m"
        RESET = "\033[0m"

        EMOJI_PROGRESS = "🔄"
        EMOJI_DONE = "✅"
        EMOJI_STAR = "✨"

        def logo():
            print(f"{YELLOW}{EMOJI_STAR*3} combos numericos {EMOJI_STAR*3}\nCreado por Angel Exspectrus {EMOJI_STAR}\n{RESET}")

        def clear_line():
            sys.stdout.write("\r" + " " * 60 + "\r")
            sys.stdout.flush()

        def barra_progreso(actual, total):
            longitud_barra = 18
            porcentaje = actual / total
            cantidad_bloques = int(porcentaje * longitud_barra)
            barra = "■" * cantidad_bloques + "-" * (longitud_barra - cantidad_bloques)
            clear_line()
            sys.stdout.write(
                f"{CYAN}{EMOJI_PROGRESS} [{barra}] {actual}/{total} combos generados{RESET}"
            )
            sys.stdout.flush()

        def crear_combo(long_usuario, long_contra, modo_contra="random", contra_consec=None):
            usuario = "".join(random.choices("1234567890", k=long_usuario))
            if modo_contra == "consec":
                contra = contra_consec
            else:
                contra = "".join(random.choices("1234567890", k=long_contra))
            return f"{usuario}:{contra}"

        logo()

        try:
            total = int(input(f"{YELLOW}👉 ¿Cuántos combos quieres generar? {RESET} "))
            long_usuario = int(input(f"\n{YELLOW}😎 Longitud numérica para USUARIO: {RESET}"))

            print(f"\n{YELLOW}¿Qué tipo de contraseña quieres usar?{RESET}")
            print("1 - Consecutiva (ejemplo: 12345...)")
            print("2 - Aleatoria")
            print("3 - Ambos (mezclados)")
            opcion_contra = input("Elige opción (1, 2 o 3): ").strip()

            if opcion_contra not in ["1", "2", "3"]:
                print(f"{RED}Opción inválida, usando aleatoria por defecto.{RESET}")
                opcion_contra = "2"

            long_contra = int(input(f"\n{YELLOW}🔑 Longitud numérica para CONTRASEÑA: {RESET} "))

            contra_consec = None
            if opcion_contra in ["1", "3"]:
                base = "123456789"
                veces = (long_contra // 10) + 1
                contra_consec = (base * veces)[:long_contra]

            nombre_archivo = input(f"\n{YELLOW}💾 Nombre del archivo: {RESET} ").strip()
            if not nombre_archivo:
                nombre_archivo = "combos_generados"
        except Exception:
            print(f"{RED}✖ Entrada inválida, por favor ingresa números válidos.{RESET}")
            return True

        ruta_archivo = os.path.join(output_dir, nombre_archivo + ".txt")

        with open(ruta_archivo, "w") as f:
            for i in range(1, total + 1):
                if opcion_contra == "1":
                    combo = crear_combo(long_usuario, long_contra, "consec", contra_consec)
                elif opcion_contra == "2":
                    combo = crear_combo(long_usuario, long_contra, "random")
                else:  # opción 3: mezclado alternando consecutiva y aleatoria
                    if i % 2 == 0:
                        combo = crear_combo(long_usuario, long_contra, "consec", contra_consec)
                    else:
                        combo = crear_combo(long_usuario, long_contra, "random")

                f.write(combo + "\n")
                barra_progreso(i, total)
                time.sleep(0.01)

        clear_line()
        print(f"\n{GREEN}{EMOJI_DONE} ¡Listo! Se generaron {total} combos y se guardaron en: {ruta_archivo}{RESET}")

        return True

    if menu not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        print("Opción no válida. Intente de nuevo.")
        return True

    filename = input("\nIngrese el nombre para su archivo de combo (sin .txt): ")
    try:
        hwm = int(input("\n\033[93mNúmero de combos a generar:\033[0m "))
        if hwm <= 0:
            raise ValueError("El número debe ser mayor que 0.")
    except ValueError as e:
        print(f"Error: {e if str(e) else 'Ingrese un número válido.'}")
        return True

    combo_option = "3"
    if menu in ["1", "3", "4", "6", "7", "8"]:
        print("\n\033[93mGenerar combinación:\033[0m")
        print("1) Solo lado izquierdo")
        print("2) Solo lado derecho")
        print("3) Ambos lados")
        combo_option = input("\nElija una opción: ")
        if combo_option not in ["1", "2", "3"]:
            print("Opción de combinación no válida. Usando ambos lados por defecto.")
            combo_option = "3"

    if menu == "5":
        print("\n\033[93mGenerador de combos alfanuméricos\033[0m")
        print("\033[93mIdeas Angel Exspectrus\033[0m")

        print("\n\033[93mSelecciona el tipo de combo para generar:\033[0m")
        print("1. Solo letras")
        print("2. Letras y números")
        print("3. Letras y año de nacimiento")
        try:
            option_type = int(input("\nIngresa tu selección (1-3): "))
            if option_type not in [1, 2, 3]:
                raise ValueError("Selección inválida. Debe ser 1, 2 o 3.")
        except ValueError as e:
            print(f"Error: {e}")
            return True

        try:
            user_length = int(input("\nIngresa la longitud deseada para el usuario: "))
            pass_length = int(input("\nIngresa la longitud deseada para la contraseña: "))
            if user_length <= 0 or pass_length <= 0:
                raise ValueError("Las longitudes deben ser mayores que 0.")
        except ValueError as e:
            print(f"Error: {e}")
            return True

        birth_year = False
        year_position = 'right'
        if option_type == 3:
            print("\n\033[93mSelecciona dónde colocar el año de nacimiento:\033[0m")
            print("1. Izquierda")
            print("2. Derecha")
            print("3. Ambos")
            try:
                year_option = int(input("\nIngresa tu selección (1-3): "))
                if year_option not in [1, 2, 3]:
                    raise ValueError("Selección inválida. Debe ser 1, 2 o 3.")
                if year_option == 1:
                    year_position = 'left'
                elif year_option == 2:
                    year_position = 'right'
                elif year_option == 3:
                    year_position = 'both'
                birth_year = True
            except ValueError as e:
                print(f"Error: {e}")
                return True

        print("\n\033[93mSelecciona las opciones para las letras:\033[0m")
        print("1. Solo letras mayúsculas")
        print("2. Solo letras minúsculas")
        print("3. Ambas mayúsculas y minúsculas")
        try:
            option_case = int(input("\nIngresa tu selección (1-3): "))
            if option_case not in [1, 2, 3]:
                raise ValueError("Selección inválida. Debe ser 1, 2 o 3.")
        except ValueError as e:
            print(f"Error: {e}")
            return True

        include_uppercase = False
        include_lowercase = False
        numbers = False

        if option_type == 1:
            numbers = False
        elif option_type == 2:
            numbers = True
        elif option_type == 3:
            numbers = False

        if option_case == 1:
            include_uppercase = True
        elif option_case == 2:
            include_lowercase = True
        elif option_case == 3:
            include_uppercase = True
            include_lowercase = True

    lines_set = set()
    output_file = os.path.join(output_dir, f"{filename}.txt")
    batch = []

    with tqdm(total=hwm, desc="Generando combos", unit="líneas",
              bar_format="\033[32m{desc}\n{bar:20} {percentage:.1f}%\nTiempo estimado: {remaining_s:.1f}s\033[0m",
              ascii="□■", smoothing=0.1) as pbar:
        while len(lines_set) < hwm:
            rname = names.get_first_name()
            rlastname = names.get_last_name()

            if menu == "1":
                num = random.randint(2000, 2050)
                all1, alln, all2, allf = generar_combo(rname, rlastname, num, combo_option)
            elif menu == "2":
                all1 = rname
                alln = f"{all1}:{rlastname}"
                all2 = rlastname
                allf = f"{all2}:{rname}"
            elif menu == "3":
                num = random.randint(1, 499)
                all1, alln, all2, allf = generar_combo(rname, rlastname, num, combo_option)
            elif menu == "4":
                num = random.randint(500, 999)
                all1, alln, all2, allf = generar_combo(rname, rlastname, num, combo_option)
            elif menu == "5":
                username, password = generate_random_combos(user_length, pass_length, include_uppercase, include_lowercase, numbers, birth_year, year_position)
                line = f"{username}:{password}\n"
                if line not in lines_set:
                    lines_set.add(line)
                    batch.append(line)
                    pbar.update(1)
                continue
            elif menu == "6":
                num = random.randint(1960, 2050)
                all1, alln, all2, allf = generar_combo(rname, rlastname, num, combo_option)
            elif menu == "7":
                num = random.choice(["2023", "2024", "2025", "2026"])
                all1, alln, all2, allf = generar_combo(rname, rlastname, num, combo_option)
            elif menu == "8":
                num = random.choice(["111", "222", "333", "444", "555", "666", "777", "888", "999"])
                all1, alln, all2, allf = generar_combo(rname, rlastname, num, combo_option)
            elif menu == "9":
                num = random.choice(["123", "1234", "12345", "321", "4321", "54321"])
                all1, alln, all2, allf = generar_combo(rname, rlastname, num, combo_option)
            elif menu == "10":
                numbers1 = random.choice(["123", "1234", "12345", "123456", "1234567", "12345678", "4321", "54321", "654321","102030"])
                numbers2 = random.choice(["123", "1234", "12345", "123456", "1234567", "12345678", "4321", "54321", "654321", "102030"])
                all1 = f"{rname}:{numbers1}"
                all2 = f"{rlastname}:{numbers2}"
                alln = all1
                allf = all2

            lines = [f"{alln}\n", f"{allf}\n"]
            random.shuffle(lines)
            for line in lines:
                if line not in lines_set and len(lines_set) < hwm:
                    lines_set.add(line)
                    batch.append(line)
                    pbar.update(1)
                    break

            if len(batch) >= 100:
                with open(output_file, "a+", encoding="utf-8") as f:
                    f.writelines(batch)
                batch = []

    if batch:
        with open(output_file, "a+", encoding="utf-8") as f:
            f.writelines(batch)

    print(f"\n\033[32mArchivo de combo guardado como: {output_file}\033[0m")
    return True

def multifuncion_combos():
    def print_menu():
        # Menú de la multifunción para combos
        print("\n\033[32mPython duplicas/unidor/divisor de combos\033[0m\n")
        print("\033[93m╔══════════════════════════\033[0m       ")
        print("\033[93m║\033[0m     \033[93mMENÚ MULTIFUNCIÓN\033[0m   \033[93m║\033[0m   ")
        print("\033[93m║\033[0m1. Eliminar duplicados   \033[93m║\033[0m     ")
        print("\033[93m║\033[0m2. Unir combos           \033[93m║\033[0m     ")
        print("\033[93m║\033[0m3. Dividir archivos      \033[93m║\033[0m    ")
        print("\033[93m║\033[0m4. Salir                 \033[93m║\033[0m     ")
        print("\033[93m╚══════════════════════════\033[0m      ")

    def unir_combos():
        # Une archivos de combos
        print("\n\033[43;30m\033[1m\033[97m UNIR ARCHIVOS DE LA CARPETA 'combo'\033[0m")
        folder_path = '/sdcard/combo'
        print("\nArchivos disponibles en la carpeta:\n")
        files = os.listdir(folder_path)
        for i, file in enumerate(files):
            print(f"{i+1}. {file}")
        selected_files = input("\nSelecciona los archivos que deseas unir (ingresa los números separados por comas): ")
        selected_files_indices = [int(index) - 1 for index in selected_files.split(',')]
        total_lines = sum(len(open(os.path.join(folder_path, files[index]), encoding='utf-8').readlines()) for index in selected_files_indices)
        print("\nUniendo archivos...")
        combined_lines = []
        for index in selected_files_indices:
            file_path = os.path.join(folder_path, files[index])
            with open(file_path, 'r') as file:
                lines = file.readlines()
                combined_lines.extend(lines)
        unique_combined_lines = list(set(combined_lines))
        print(f"\n\nNúmero de líneas originales en los archivos: {total_lines}")
        print(f"Número de líneas en el archivo combinado: {len(unique_combined_lines)}")
        output_file_name = input("Nombre para guardar los resultados: ") + ".txt"
        output_file_path = os.path.join(folder_path, output_file_name)
        with open(output_file_path, 'w') as file:
            file.writelines(unique_combined_lines)
        print(f"\nArchivo guardado como '{output_file_name}'")
        print("Proceso de unión de combos terminado.")

    def eliminar_duplicados_combos():
        # Elimina duplicados de un archivo de combos
        print("\n\033[43;30m\033[1m\033[97m ELIMINAR DUPLICADOS DE LOS COMBOS\033[0m")
        folder_path = '/sdcard/combo'
        print("\nArchivos disponibles en la carpeta de combos:\n")
        files = os.listdir(folder_path)
        for i, file in enumerate(files):
            print(f"{i + 1}. {file}")
        selected_file = int(input("\nSelecciona un archivo de combo (ingresa el número): "))
        file_name = files[selected_file - 1]
        file_path = os.path.join(folder_path, file_name)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nLeyendo archivo \033[92m'{file_name}'\033[0m para quitar duplicados")
        with open(file_path, 'r') as file:
            lines = file.readlines()
        unique_lines = list(set(lines))
        num_duplicates = len(lines) - len(unique_lines)
        print(f"\n\033[43;30m\033[1m\033[97m Resumen del archivo: '{file_name}'\033[0m")
        print(f"---------------------------------------------")
        print(f"Archivo que usaste: \033[92m{file_name}\033[0m")
        print(f"Total de líneas: \033[92m{len(lines)}\033[0m")
        print(f"Número de líneas duplicadas: \033[92m{num_duplicates}\033[0m")
        print(f"Lineas que se eliminaron: \033[92m{num_duplicates}\033[0m")
        print(f"Número de líneas únicas: \033[92m{len(unique_lines)}\033[0m")
        print(f"Total de lineas que quedaron: \033[92m{len(unique_lines)}\033[0m")
        print(f"--------------------------------------------\n")
        output_file_name = input(f"Nombre para guardar los resultados: ") + ".txt"
        output_file_path = os.path.join(folder_path, output_file_name)
        with open(output_file_path, 'w') as file:
            file.writelines(unique_lines)
        print(f"\nGuardando archivo '{output_file_name}'...")
        print(f"Archivo guardado como '{output_file_name}'")
        print(f"Proceso terminado.")

    def dividir_archivos():
        # Divide un archivo de combos en varias partes
        print("\n\033[43;30m\033[1m\033[97m DIVIDIR ARCHIVOS EN VARIAS PARTES\033[0m")
        folder_path = '/sdcard/combo'
        print("\nArchivos disponibles en la carpeta de combos:\n")
        files = os.listdir(folder_path)
        for i, file in enumerate(files):
            print(f"{i + 1}. {file}")
        selected_file = int(input("\nSelecciona un archivo de combo para dividir (ingresa el número): "))
        file_name = files[selected_file - 1]
        file_path = os.path.join(folder_path, file_name)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nDividiendo archivo \033[92m'{file_name}'\033[0m en varias partes")
        parts_number = int(input("\n¿En cuántas partes quieres dividir el archivo?: "))
        with open(file_path, 'r') as file:
            lines = file.readlines()
        lines_per_part = len(lines) // parts_number
        if len(lines) % parts_number != 0:
            parts_number += 1
        print(f"\nDividiendo archivo en \033[93m{parts_number}\033[0m partes...")
        for i in range(parts_number):
            start_idx = i * lines_per_part
            end_idx = min((i + 1) * lines_per_part, len(lines))
            output_file_name = f"{file_name}_{i+1}.txt"
            output_file_path = os.path.join(folder_path, output_file_name)
            with open(output_file_path, 'w') as output_file:
                output_file.writelines(lines[start_idx:end_idx])
        print("\nProceso de división de archivos terminado.")
        print("\nArchivos guardado en la ruta sdcard/combo.")

    while True:
        print_menu()
        opcion = input("\nSelecciona una opción del menú: ")
        if opcion == '1':
            eliminar_duplicados_combos()
        elif opcion == '2':
            unir_combos()
        elif opcion == '3':
            dividir_archivos()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

def menu_principal():
    # Menú principal del programa
    carpeta_resultados = os.path.join('/sdcard', 'Resultados_combinaciones')
    if not os.path.exists(carpeta_resultados):
        os.makedirs(carpeta_resultados)

    carpeta_combos_user = os.path.join('/sdcard', 'combos_user')
    if not os.path.exists(carpeta_combos_user):
        os.makedirs(carpeta_combos_user)

    carpeta_combos = os.path.join('/sdcard', 'combo')
    if not os.path.exists(carpeta_combos):
        os.makedirs(carpeta_combos)

    while True:
        print('\n\033[93m+------------------------------------+\033[0m')
        print('\033[93m|\033[0m\033[44m      Menú Principal de combos      \033[0m\033[93m|\033[0m')
        print('\033[93m--------------------------------------\033[0m')
        print('\033[93m|\033[0m 1. Coloque la ruta de nombres      \033[93m|\033[0m')
        print('\033[93m|\033[0m    y ruta de combinaciones         \033[93m|\033[0m')
        print('\033[93m|\033[0m 2. Seleccionar archivo de nombres  \033[93m|\033[0m')
        print('\033[93m|\033[0m    de su carpeta "combos_user"     \033[93m|\033[0m')
        print('\033[93m|\033[0m 3. Generador de nombres            \033[93m|\033[0m')
        print('\033[93m|\033[0m 4. Generador de combos             \033[93m|\033[0m')
        print('\033[93m|\033[0m 5. Multifunción para combos        \033[93m|\033[0m')
        print('\033[93m|\033[0m 6. Generador de correos            \033[93m|\033[0m')
        print('\033[93m|\033[0m 7. Mega Generador Mac              \033[93m|\033[0m')
        print('\033[93m+------------------------------------+\033[0m')
        opcion = input('\n\033[32mIngresa el número de opción:\033[0m ')

        try:
            opcion = int(opcion)
        except ValueError:
            print('Opción inválida. Intenta de nuevo.')
            continue

        if opcion == 1:
            nombres_archivo = input('\n\033[93mIngresa tu ruta del archivo de nombres (ej./sdcard/nombres.txt):\033[0m ')
            combos_archivo = input('\n\033[93mIngresa la ruta del archivo de combinaciones (ej./sdcard/comb.txt):\033[0m ')
            resultados, num_combinaciones, num_omitidas = generar_combinaciones(nombres_archivo, combos_archivo)
            nombre_archivo = input('\n\033[93mIngresa el nombre del archivo para guardar los resultados:\033[0m ')
            print("\nProcesando archivo...")
            progress_bar(5)
            now = datetime.datetime.now()
            fecha_hora_actual = now.strftime('%Y-%m-%d %H:%M:%S')
            archivo_resultados = os.path.join(carpeta_resultados, f'{nombre_archivo}.txt')
            with open(archivo_resultados, 'w') as f:
                f.write('\n'.join(resultados))
            print(f'\n\033[93m+------------------------------------+\033[0m')
            print(f'Los resultados se han guardado en: {archivo_resultados}')
            print(f'\033[93m+------------------------------------+\033[0m')
            print(f'Resultados obtenidos según la combinación y nombres ')
            print(f'Número de combinaciones: \033[32m{num_combinaciones}\033[0m')
            print(f'Combinaciones omitidas: \033[32m{num_omitidas}\033[0m')
            print(f'Fecha y hora: \033[32m{fecha_hora_actual}\033[0m')
            print(f'\033[93m+------------------------------------+\033[0m')
        elif opcion == 2:
            archivos_combos = os.listdir(carpeta_combos_user)
            print(' ')
            print('\033[93mArchivos en la carpeta\033[0m "combos_user":  ')
            print(' ')
            for i, archivo in enumerate(archivos_combos, 1):
                print(f' {i}. {archivo}  ')
            print(' ')
            seleccion_nombres = int(input('\033[32mSelecciona el archivo de nombres (1-{}):\033[0m '.format(len(archivos_combos))))
            seleccion_combos = int(input('\n\033[32mSelecciona el archivo de combinaciones (1-{}):\033[0m '.format(len(archivos_combos))))
            nombres_archivo = os.path.join(carpeta_combos_user, archivos_combos[seleccion_nombres - 1])
            combos_archivo = os.path.join(carpeta_combos_user, archivos_combos[seleccion_combos - 1])
            resultados, num_combinaciones, num_omitidas = generar_combinaciones(nombres_archivo, combos_archivo)
            nombre_archivo = input('\n\033[93mIngresa el nombre del archivo para guardar los resultados:\033[0m ')
            print("\nProcesando archivo...")
            progress_bar(5)
            now = datetime.datetime.now()
            fecha_hora_actual = now.strftime('%Y-%m-%d %H:%M:%S')
            archivo_resultados = os.path.join(carpeta_resultados, f'{nombre_archivo}.txt')
            with open(archivo_resultados, 'w') as f:
                f.write('\n'.join(resultados))
            print(f'\n\033[93m+------------------------------------+\033[0m')
            print(f'Los resultados se han guardado en: {archivo_resultados}')
            print(f'\033[93m+------------------------------------+\033[0m')
            print(f'Resultados obtenidos según la combinación y nombres ')
            print(f'Número de combinaciones: \033[32m{num_combinaciones}\033[0m')
            print(f'Combinaciones omitidas: \033[32m{num_omitidas}\033[0m')
            print(f'Fecha y hora: \033[32m{fecha_hora_actual}\033[0m')
            print(f'\033[93m+------------------------------------+\033[0m')
        elif opcion == 3:
            generador_nombres()
            respuesta = input('\n\033[93m¿Desea continuar en el menú principal? (s/n):\033[0m ')
            if respuesta.lower() == 'n':
                break
            continue
        elif opcion == 4:
            continuar = generador_combos()
            if not continuar:
                break
            respuesta = input('\n\033[93m¿Desea continuar en el menú principal? (s/n):\033[0m ')
            if respuesta.lower() == 'n':
                break
            continue
        elif opcion == 5:
            multifuncion_combos()
            respuesta = input('\n\033[93m¿Desea continuar en el menú principal? (s/n):\033[0m ')
            if respuesta.lower() == 'n':
                break
            continue
        elif opcion == 6:
            generador_correos()
            respuesta = input('\n\033[93m¿Desea continuar en el menú principal? (s/n):\033[0m ')
            if respuesta.lower() == 'n':
                break
            continue
        elif opcion == 7:
            prefijos_mac = (
                'D4:CF:F9:', 'D5:CB:B3:', 'D3:FC:F9:', 'D9:CC:BF:', 'A0:BB:3E:', 
                'E7:CF:F9:', 'E3:DF:D2:', 'D8:A1:A9:', 'E9:FE:F6:', '55:93:EA:', 
                '55:92:F9:', '70:CF:B9:', '04:D6:AA:', '11:33:01:', '00:1C:19:', 
                '1A:00:6A:', '1A:00:FB:', '00:A1:79:', '00:1B:79:', '00:2A:79:', 
                '00:1A:79:', '33:44:CF:', '10:27:BE:', '00:1D:E0:', '10:2F:6B:', 
                '00:04:4B:', '74:E5:F9:', '48:B0:2D:', '00:0A:95:', '00:26:5A:', 
                '00:50:E4:', '04:A0:DE:', '12:E0:4D:', '01:E0:32:', '00:12:F0:', 
                '40:1A:2A:', '02:1D:BA:', '00:B4:8D:', '70:A6:8C:', '00:E0:8A:', 
                '17:1A:90:', '90:C8:6D:', '00:D3:7C:', '18:F9:5D:', '30:F9:5D:', 
                '18:F7:6D:', '90:F9:8D:', 'A0:01:2E:', 'A3:02:5E:', 'A8:B4:9E:', 
                'C0:BB:3E:', '00:2A:01:', '00:2A:04:', '00:2A:05:', '00:2B:06:', 
                '10:2C:01:', '03:2A:09:', '00:2A:80:', '00:1A:81:', '19:1C:79:', 
                '03:1A:39:', '00:1D:79:', '00:1E:90:', '14:6E:49:', 'B4:1C:12:', 
                '06:1C:13:', '9D:1A:14:', '08:7A:56:', '00:9C:17:', '03:8F:19:', 
                '06:7F:90:', '02:7C:17:', '19:4C:18:', '06:3D:80:', 'A4:2B:8C:', 
                'B0:4E:26:', 'C8:3D:F2:', 'F0:9E:4A:', '88:5A:92:', '2C:54:CF:', 
                '3C:22:FB:', '5C:F3:FC:', '6C:5E:7A:', '7C:9E:BD:', '8C:FA:BA:', 
                '9C:1D:58:', 'AC:3F:A4:', 'BC:6A:29:', 'CC:2D:83:', 'DC:4F:22:', 
                'EC:1F:72:', 'FC:3D:93:', '0C:5B:8F:', '1C:6F:65:', '20:4A:7B:', 
                '24:5B:8C:', '28:6C:9D:', '2C:7D:AE:', '30:8E:BF:', '34:9F:C0:', 
                '38:A0:D1:', '3C:B1:E2:', '40:C2:F3:', '44:D3:04:', '48:E4:15:', 
                '4C:F5:26:', '50:06:37:', '54:17:48:', '58:28:59:', '5C:39:6A:', 
                '60:4A:7B:', '64:5B:8C:', '68:6C:9D:', '6C:7D:AE:', '70:8E:BF:', 
                '74:9F:C0:', '78:A0:D1:', '7C:B1:E2:', '80:C2:F3:', '84:D3:04:', 
                '88:E4:15:', '8C:F5:26:', '90:06:37:', '94:17:48:', '98:28:59:', 
                '9C:39:6A:', 'A0:4A:7B:', 'A4:5B:8C:', 'A8:6C:9D:', 'AC:7D:AE:', 
                'B0:8E:BF:', 'B4:9F:C0:', 'B8:A0:D1:', 'BC:B1:E2:', 'C0:C2:F3:', 
                'C4:D3:04:', 'C8:E4:15:', 'CC:F5:26:', 'D0:06:37:', 'D4:17:48:', 
                'D8:28:59:', 'DC:39:6A:', 'E0:4A:7B:', 'E4:5B:8C:', 'E8:6C:9D:', 
                'EC:7D:AE:', 'F0:8E:BF:', 'F4:9F:C0:', 'F8:A0:D1:', 'FC:B1:E2:'
            )
            # Función para limpiar la pantalla
            subprocess.run(["clear", ""])

            titulo = """
\033[1;35;40m
════════════════════════════════════════════
         🌟 \033[1;33;40mGENERADOR MEGA COMBOS 🌟 \033[0m
         🚀 \033[1;32;40mQPYTHON - COMBINACIONES MAC 🚀 \033[0m
         🎨 \033[1;35;40mCREADO POR ANGEL EXSPECTRUS 🎨 \033[0m
\033[1;35;40m════════════════════════════════════════════
\033[0m
 
 """

            print(titulo)

            # Mostrar tipos de direcciones MAC disponibles
            print("\033[1;34;40m📋 TIPOS DE DIRECCIONES MAC DISPONIBLES:\033[0m\n")
            total_prefijos = len(prefijos_mac)
            for i in range(total_prefijos):
                print(f"\033[1;36m{i+1} - {prefijos_mac[i]}\033[0m")

            # Preguntar si desea usar todos los tipos de MAC o uno específico
            opcion = input("""
\033[1;34;40m🔧 ¿QUÉ TIPO DE MAC DESEA USAR?
\033[1;32m[T] Todos los tipos \033[0m\033[1;31mo \033[1;36m[E] Específico\033[0m
\033[1;33mSeleccione (T/E): \033[0m""").upper()

            # Si elige un tipo específico, mostrar opciones nuevamente
            if opcion.startswith('E'):
                print("\n\033[1;34;40m📋 TIPOS DE MAC DISPONIBLES:\033[0m\n")
                for i in range(total_prefijos):
                    print(f"\033[1;36m{i+1} - {prefijos_mac[i]}\033[0m")
                tipo_seleccionado = input("\033[1;31;40m🔢 Escoja un tipo de MAC: \033[0m")
            else:
                tipo_seleccionado = None

            # Entrada del usuario para el nombre del archivo (después de seleccionar el tipo de MAC)
            nombre_archivo = input("""
\033[1;31;40m📝 INGRESE EL NOMBRE PARA SU COMBO:
\033[1;33mNombre del combo: \033[0m""")

            # Entrada para la cantidad de MACs a generar
            cantidad = input("""
\033[1;34;40m🔢 ¿CUÁNTAS DIRECCIONES MAC DESEA CREAR?
\033[1;33mCantidad: \033[0m""")

            # Validar entrada numérica
            try:
                cantidad = int(cantidad)
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser mayor que 0.")
            except ValueError:
                print("\033[1;31;40m❌ Error: Ingrese un número válido y mayor que 0.\033[0m")
                exit()

            # Ruta del archivo de salida
            ruta_archivo = f"/sdcard/{nombre_archivo}_Mac_ae.txt"

            # Función para guardar direcciones MAC
            def guardar_direccion(direccion):
                with open(ruta_archivo, 'a+') as archivo:
                    archivo.write(direccion + "\n")

            # Generación de direcciones MAC con indicador de progreso
            print("\n\033[1;32;40m🔄 GENERANDO DIRECCIONES MAC...\033[0m")
            contador = 0
            while contador < cantidad:
                direccion_aleatoria = "%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                direccion_aleatoria = direccion_aleatoria.replace('100', '10')
                
                if opcion.startswith('E'):
                    try:
                        direccion = prefijos_mac[int(tipo_seleccionado)-1] + direccion_aleatoria
                    except (IndexError, ValueError):
                        print("\033[1;31;40m❌ Error: Tipo de MAC inválido.\033[0m")
                        exit()
                else:
                    direccion = random.choice(prefijos_mac) + direccion_aleatoria
                
                print(f"\033[1;35m🔍 {direccion}  \033[1;33m[{contador+1}/{cantidad}]\033[0m")
                guardar_direccion(direccion)
                contador += 1
                time.sleep(0.05)  

            # Mensaje de finalización
            print(f"""
\033[1;32;40m✅ OPERACIÓN COMPLETADA
📂 Combo guardado en: {ruta_archivo}
🙌 ¡Gracias por usar el Mega Generador Angel Exspectrus! 😎\033[0m
""")
            respuesta = input('\n\033[93m¿Desea continuar en el menú principal? (s/n):\033[0m ')
            if respuesta.lower() == 'n':
                break
            continue
        else:
            print('Opción inválida. Intenta de nuevo.')
            continue

if __name__ == '__main__':
    menu_principal()