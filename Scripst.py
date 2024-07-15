# Importamos todas las bibliotecas necesarias:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carga del archivo:
df_kpi_inc = pd.read_csv(r"df_kpi_inc.csv")
df_kpi_megas = pd.read_csv(r"df_kpi_megas.csv")

# Vamos a realizar una funcion que si por parametro escribimos una provincia, nos devolvera un grafico el cual tiene todos los años con sus respectivos trimestres y el valor de KPI que tienen.
def grafico_kpi_por_provincia(provincia):
    global df_kpi_inc  # Usar el dataframe global
    
    # Filtramos el dataframe por la provincia especificada
    df_provincia = df_kpi_inc[df_kpi_inc['Provincia'] == provincia]
    
    # Ordenamos por Año y Trimestre
    df_provincia = df_provincia.sort_values(by=['Año', 'Trimestre'])
    
    # Calculamos el KPI por trimestre
    df_provincia['KPI'] = ((df_provincia['nuevo_acceso'] - df_provincia['acceso_actual']) / df_provincia['acceso_actual']) * 100
    df_provincia['KPI'] = df_provincia['KPI'].round(2)
    
    # Definimos colores y paleta
    colores_trimestres = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    sns.set_palette(sns.color_palette('Set2'))
    
    # Graficamos el KPI por trimestre con barras y línea del 2%
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(x='Año', y='KPI', hue='Trimestre', data=df_provincia, palette=colores_trimestres)
    
    # Estilo y ajustes
    plt.title(f'KPI por Trimestre para {provincia}', fontsize=18)
    plt.xlabel('Año', fontsize=14)
    plt.ylabel('KPI (%)', fontsize=14)
    plt.axhline(y=2, color='gray', linestyle='--', linewidth=2, alpha=0.6)
    plt.grid(True, axis='y', linestyle='--', alpha=0.6)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    ax.legend(title='Trimestre', title_fontsize='14', fontsize='12', loc='upper left')
    
    # Ajustes de la leyenda fuera del gráfico
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    
    # Ajustar diseño general
    sns.despine(trim=True)
    plt.tight_layout()
    
    # Mostramos el gráfico
    plt.show()

    ###########################################################################################################################################################################

# Creamos una función para generar el gráfico del crecimiento de acceso a internet por provincia
def graficar_crecimiento_acceso(provincia):
    df_provincia = df_kpi_megas[df_kpi_megas['Provincia'] == provincia]
    
    if df_provincia.empty:
        print(f"No se encontraron datos para la provincia: {provincia}")
        return
    
    plt.figure(figsize=(10, 6))
    plt.plot(df_provincia['Año'].astype(str) + '-T' + df_provincia['Trimestre'].astype(str), 
             df_provincia['CrecimientoAcceso'], marker='o')
    
    plt.title(f'Crecimiento del Acceso a Internet en {provincia}')
    plt.xlabel('Tiempo (Año-Trimestre)')
    plt.ylabel('Crecimiento del Acceso (%)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    ###########################################################################################################################################################################
