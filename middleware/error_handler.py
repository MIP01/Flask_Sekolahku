from flask import jsonify

def error_handler(app):
    @app.errorhandler(Exception)
    def handle_exception(error):
        # Ambil status code dari exception, jika ada
        status_code = getattr(error, 'code', 500)
        # Tentukan pesan default untuk kesalahan
        message = str(error) if status_code != 500 else 'Internal server error'
        
        # Menyusun response error
        response = {
            'message': message,
            'error': str(error) if app.config['DEBUG'] else None # Detail error hanya ditampilkan saat DEBUG
        }
        return jsonify(response), status_code