# Credit to Rob Marshall at Red Hat (rmarshall@redhat.com) for helping me to
# # understand how to stand up simple Flask environments. Hopefully, one day,
# # I'll be able to sprout my wings and fly.
#
# This program is an for an exercise in a class called Software Systems at
# # Gordon College with Dr. Tuck.

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello World!</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
