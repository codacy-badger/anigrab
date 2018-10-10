from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, SelectField


class aniForm(FlaskForm):
    keyword = StringField(label="keyword", validators=[
                          validators.required("input your keyword, please ..!!!")])
    option = [
        ("random", "random"),
        ("animesave", "animesave"),
        ("meguminime", "meguminime"),
        ("drivenime", "drivenime"),
        ("bakacan", "bakacan"),
        ("meownime", "meownime"),
        ("wibudesu", "wibudesu"),
        ("kusonime", "kusonime"),
        ("awbatch", "awbatch"),
        ("meowbatch", "meowbatch")
    ]
    listSite = SelectField(label="daftar website", choices=option)
    btnCari = SubmitField(label="search")
