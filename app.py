"""Dashboard Streamlit – Atividade 06 (visualização de dados).

Execução (dentro da pasta do projeto, junto com os arquivos .png):
    streamlit run app.py
"""
from pathlib import Path

import streamlit as st



NOME_ALUNO = "Seu Nome Completo"
NUMERO_CHAMADA = "00"
TURMA = "Sua Turma"

AQUI = Path(__file__).parent


GRAFICOS = [
    {
        "titulo": "1. Evolução diária das vendas",
        "arquivo": "01_linhas.png",
        "analise": (
            "As vendas crescem de forma contínua ao longo do trimestre: a média diária "
            "passa de cerca de **R$ 122 em janeiro** para **R$ 173 em fevereiro** e "
            "**R$ 225 em março**, uma alta de aproximadamente R$ 1,70 por dia. A Loja B "
            "tem média levemente superior (≈ R$ 179 contra ≈ R$ 168 da Loja A). O "
            "menor valor foi R$ 93 (14/01) e o maior, R$ 260 (24/03)."
        ),
    },
    {
        "titulo": "2. Vendas médias por categoria e região",
        "arquivo": "02_barras.png",
        "analise": (
            "A região **Oeste** lidera, com média de ≈ R$ 225, enquanto o **Norte** tem "
            "o pior desempenho (≈ R$ 103). **Livros** é a categoria com maior média "
            "geral (≈ R$ 187), e a combinação Livros × Oeste é o ponto mais alto "
            "(R$ 284). Eletrônicos foge ao padrão: vende melhor no Leste (R$ 259) e "
            "pior no Sul (R$ 73)."
        ),
    },
    {
        "titulo": "3. Faturamento por canal de venda",
        "arquivo": "03_pizza.png",
        "analise": (
            "Do faturamento total de **R$ 120 mil**, o **Site** responde por 37,5% e a "
            "Loja Física por 26,7%. Somados, Site e Aplicativo (17,5%) representam "
            "55% das vendas, o que mostra a força dos canais digitais. O Telefone é o "
            "canal menos relevante, com apenas 6,7%."
        ),
    },
    {
        "titulo": "4. Relação entre altura e peso",
        "arquivo": "04_dispersao.png",
        "analise": (
            "Há **correlação positiva forte** (r ≈ 0,85): quanto maior a altura, maior "
            "tende a ser o peso. Os dois grupos se sobrepõem bastante e têm médias "
            "muito próximas (altura ≈ 170 cm; peso ≈ 62 kg no feminino e ≈ 63 kg no "
            "masculino), então, nesta amostra, o sexo pouco diferencia a relação."
        ),
    },
    {
        "titulo": "5. Regressão: renda × gasto mensal",
        "arquivo": "05_regressao.png",
        "analise": (
            "A reta **y = 0,568x + 421,25** tem **R² = 0,98**, ou seja, a renda explica "
            "cerca de 98% da variação do gasto. A cada R$ 1,00 a mais de renda, o gasto "
            "sobe ≈ R$ 0,57. Em média, as famílias gastam ≈ 63% do que ganham "
            "(renda média ≈ R$ 8,9 mil; gasto médio ≈ R$ 5,5 mil)."
        ),
    },
    {
        "titulo": "6. Distribuição salarial por departamento",
        "arquivo": "06_boxplot.png",
        "analise": (
            "**Vendas** (mediana ≈ R$ 7,1 mil) e **TI** (≈ R$ 6,6 mil) pagam bem mais "
            "que RH e Marketing (≈ R$ 4,2 mil). TI tem a maior dispersão (IQR ≈ R$ 2,9 "
            "mil). Cada departamento apresenta 2 outliers acima do limite superior, e "
            "as médias ficam acima das medianas, indicando assimetria à direita."
        ),
    },
    {
        "titulo": "7. Distribuição da idade dos clientes",
        "arquivo": "07_distribuicao.png",
        "analise": (
            "A média (**33,6 anos**) é maior que a mediana (**29 anos**), sinal de "
            "assimetria à direita. A maior concentração está entre 22 e 30 anos "
            "(≈ 40% dos 200 clientes), com um segundo grupo menor em torno de 46–50 "
            "anos. Clientes acima de 58 anos são raros."
        ),
    },
    {
        "titulo": "8. Frequência por tipo de atendimento",
        "arquivo": "08_frequencia.png",
        "analise": (
            "Dos 300 chamados, **Dúvida** é o tipo mais comum (116; 38,7%), seguido por "
            "Reclamação (73; 24,3%) e Bug (49; 16,3%). Reclamações, bugs e "
            "cancelamentos somam 155 chamados (≈ 52%), contra apenas 29 elogios "
            "(9,7%), o que indica espaço para melhorar produto e atendimento."
        ),
    },
    {
        "titulo": "9. Movimento de clientes por dia e horário",
        "arquivo": "09_heatmap.png",
        "analise": (
            "O fim de semana concentra o maior fluxo: **Domingo** tem a maior média "
            "(≈ 119 clientes) e o pico absoluto às 12h (199), seguido de Sábado "
            "(≈ 111). **Quinta-feira** é o dia mais fraco (≈ 44), com o mínimo às 16h "
            "(22). Por horário, o meio-dia é o mais movimentado (média ≈ 90)."
        ),
    },
]


st.set_page_config(
    page_title="Dashboard – Atividade 06",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded", 
)


with st.sidebar:
    st.header("👤 Informações do aluno")
    st.markdown(f"**Nome:** {NOME_ALUNO}")
    st.markdown(f"**Nº da chamada:** {NUMERO_CHAMADA}")
    st.markdown(f"**Turma:** {TURMA}")
    st.divider()
    st.caption("Atividade 06 – Visualização de dados")


def localizar_imagem(nome):
    """Procura o PNG na pasta do app e, se não achar, nas subpastas."""
    direto = AQUI / nome
    if direto.exists():
        return direto
    achados = list(AQUI.rglob(nome))
    return achados[0] if achados else None


def mostrar_imagem(nome):
    """Exibe a imagem ocupando a largura da coluna, em qualquer versão do Streamlit."""
    caminho = localizar_imagem(nome)
    if caminho is None:
        st.error(
            f"Imagem **{nome}** não encontrada. Copie os arquivos .png dos gráficos "
            f"para a mesma pasta do app.py:\n\n`{AQUI}`"
        )
        return
    try:
        st.image(str(caminho), width="stretch")          
    except TypeError:
        try:
            st.image(str(caminho), use_container_width=True)
        except TypeError:
            st.image(str(caminho), use_column_width=True)     



st.title("📊 Dashboard de Visualização de Dados")
st.caption("Atividade 06 · Todos os gráficos gerados com Matplotlib, organizados três a três.")

-
POR_LINHA = 3

for inicio in range(0, len(GRAFICOS), POR_LINHA):
    linha = GRAFICOS[inicio:inicio + POR_LINHA]

    st.divider()

    # Gráficos
    colunas = st.columns(POR_LINHA, gap="medium")
    for col, g in zip(colunas, linha):
        with col:
            st.subheader(g["titulo"], anchor=False)
            mostrar_imagem(g["arquivo"])

    # Análises (abaixo dos gráficos, alinhadas por coluna)
    colunas = st.columns(POR_LINHA, gap="medium")
    for col, g in zip(colunas, linha):
        with col:
            with st.container(border=True):
                st.markdown(f"**📝 Análise – {g['titulo'].split('. ', 1)[1]}**")
                st.markdown(g["analise"].replace("$", "\\$"))  # escapa o $ (senão vira fórmula)
