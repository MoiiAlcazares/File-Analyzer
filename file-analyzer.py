from collections import Counter
import string

STOPWORDS = {
    "the", "and", "is", "in", "to", "a", "of", "for", "on", "with", "this",
    "that", "it", "as", "are", "was", "but", "be", "at", "by", "an"
}

def limpiar_texto(texto):
    texto = texto.lower()
    texto = texto.translate(str.maketrans("", "", string.punctuation))
    palabras = texto.split()
    palabras = [p for p in palabras if p not in STOPWORDS]
    return palabras

def analizar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as file:
            contenido = file.read()

        lineas = contenido.splitlines()
        palabras = limpiar_texto(contenido)

        contador = Counter(palabras)

        total_lineas = len(lineas)
        total_palabras = len(palabras)
        total_caracteres = len(contenido)

        top_palabras = contador.most_common(10)

        resultado = []
        resultado.append("\n📊 FILE ANALYZER PRO REPORT\n")
        resultado.append(f"Líneas: {total_lineas}")
        resultado.append(f"Palabras (limpias): {total_palabras}")
        resultado.append(f"Caracteres: {total_caracteres}\n")

        resultado.append("🔥 Top 10 palabras más usadas:")
        for palabra, cant in top_palabras:
            resultado.append(f"{palabra}: {cant}")

        # Mostrar en pantalla
        print("\n".join(resultado))

        # Guardar en archivo
        with open("reporte_analisis.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(resultado))

        print("\n✅ Reporte guardado como 'reporte_analisis.txt'")

    except FileNotFoundError:
        print("❌ Archivo no encontrado.")

def main():
    print("===================================")
    print("📂 FILE ANALYZER PRO")
    print("===================================\n")

    archivo = input("Ingresa el archivo (.txt): ")
    analizar_archivo(archivo)

if __name__ == "__main__":
    main()