import os

from MLAZ.MLAZAPI import app

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 1313))
    app.run(host=host, port=port)
