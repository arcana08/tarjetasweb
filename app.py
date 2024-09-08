from flask import Flask, render_template, request, redirect, url_for, flash
from dao.TarjetasDao import TarjetasDao

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/tarjetas-index')
def tarjetas_index():
    tarjetasdao= TarjetasDao()
    lista_tarjetas = tarjetasdao.getTarjetas()
    return render_template('tarjetas-index.html',lista_tarjetas=lista_tarjetas)


@app.route('/tarjetas')
def tarjetas():
    return render_template('tarjetas.html')

@app.route('/guardar-tarjeta',methods=['POST'])
def guardarTarjeta():
    
    tarjeta = request.form.get('txt_tarjeta').strip()
    if tarjeta == None or len(tarjeta) < 1:
        flash('Debe escribir nombre de la tarjeta', 'warning')

        return redirect(url_for('tarjetas'))
    Tarjetasdao = TarjetasDao()
    Tarjetasdao.guardarTarjetas(tarjeta.upper())
    
    flash('guardado exitoso','success')
    
    return redirect(url_for('tarjetas_index'))

@app.route('/tarjetas-editar/<id>')
def tarjetasEditar(id):
    tarjetasdao = TarjetasDao()
    return render_template('tarjetas-editar.html', tarjetas=tarjetasdao.getTarjetasById(id))

@app.route('/actualizar-tarjeta', methods=['POST'])
def actualizarTarjeta():
    id = request.form.get('txtId')
    descripcion = request.form.get('txtDescripcion').strip()

    if descripcion == None or len(descripcion) == 0:
        flash('No debe estar vacia la descripcion')
        return redirect(url_for('tarjetasEditar', id=id))

    tarjetasdado=TarjetasDao()
    tarjetasdado.updateTarjetas(id, descripcion.upper())

    return redirect(url_for('tarjetas_index'))

@app.route('/tarjetas-eliminar/<id>')
def tarjetasEliminar(id):
    tarjetasdao=TarjetasDao()
    tarjetasdao.deleteTarjetas(id)
    return redirect(url_for('tarjetas_index'))

if __name__=='__main__':
    app.run(debug=True)