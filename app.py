from flask import Flask, render_template, request

app = Flask(__name__)

# Diccionario de versículos organizados por categoría
versiculos = {
    "Fe": [
        ("Hebreos 11:1", "Es, pues, la fe la certeza de lo que se espera, la convicción de lo que no se ve."),
        ("Mateo 17:20", "Si tenéis fe como un grano de mostaza, diréis a este monte: Pásate de aquí allá, y se pasará; y nada os será imposible."),
    ],
    "Amor": [
        ("1 Corintios 13:4-5", "El amor es sufrido, es benigno; el amor no tiene envidia, el amor no es jactancioso, no se envanece; no hace nada indebido, no busca lo suyo, no se irrita, no guarda rencor."),
        ("Juan 3:16", "Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna."),
    ],
    "Esperanza": [
        ("Romanos 15:13", "Y el Dios de esperanza os llene de todo gozo y paz en el creer, para que abundéis en esperanza por el poder del Espíritu Santo."),
        ("Jeremías 29:11", "Porque yo sé los pensamientos que tengo acerca de vosotros, dice Jehová, pensamientos de paz, y no de mal, para daros el fin que esperáis."),
    ],
    "Paz": [
        ("Filipenses 4:7", "Y la paz de Dios, que sobrepasa todo entendimiento, guardará vuestros corazones y vuestros pensamientos en Cristo Jesús."),
        ("Juan 14:27", "La paz os dejo, mi paz os doy; yo no os la doy como el mundo la da. No se turbe vuestro corazón, ni tenga miedo."),
    ],
    "Fuerza": [
        ("Isaías 40:31", "Pero los que esperan a Jehová tendrán nuevas fuerzas; levantarán alas como las águilas; correrán, y no se cansarán; caminarán, y no se fatigarán."),
        ("Filipenses 4:13", "Todo lo puedo en Cristo que me fortalece."),
    ],
}

@app.route('/')
def index():
    return render_template('index.html', categorias=versiculos.keys())

@app.route('/buscar', methods=['POST'])
def buscar():
    categoria = request.form.get('categoria')
    resultados = versiculos.get(categoria, [])
    return render_template('index.html', categorias=versiculos.keys(), resultados=resultados, categoria=categoria)

if __name__ == '__main__':
    app.run(debug=True)